"""Portable behavioral check; explicitly not a Harbor isolation or /cheat run."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import time

PACKAGE = Path(__file__).resolve().parents[1]
TASK = PACKAGE / "tasks/prefect-monitor"
ROOT = PACKAGE.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_info(source):
    helper = load("build_info", source / "tools/write_build_info.py")
    helper.write_build_info(source, {"version": "3.6.24+nogit", "build_date": "2026-10-28T00:00:00Z"}, {"path": "src/prefect/_build_info.py"})


def extract(source):
    source.mkdir(parents=True)
    with tarfile.open(TASK / "environment/data/baseline.tar.gz") as archive:
        for member in archive:
            if not (member.isfile() or member.isdir()) or not (source / member.name).resolve().is_relative_to(source.resolve()):
                raise ValueError("Unsafe baseline member")
        archive.extractall(source)
    build_info(source)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["oracle", "nop"], required=True)
    parser.add_argument("--python", type=Path, required=True)
    parser.add_argument("--groups", default="behavior,retry,compatibility,reliability")
    parser.add_argument("--report-name")
    args = parser.parse_args()
    python = args.python.resolve()
    run = PACKAGE / ".runtime" / ("package-" + args.mode + "-" + time.strftime("%H%M%S"))
    baseline, source, runtime = run / "baseline", run / "source", run / "runtime"
    extract(baseline)
    shutil.copytree(baseline, source)
    if args.mode == "oracle":
        subprocess.run(["git", "apply", "--check", str(TASK / "solution/solution.patch")], cwd=source, check=True)
        subprocess.run(["git", "apply", str(TASK / "solution/solution.patch")], cwd=source, check=True)
    shutil.copytree(TASK / "tests/overlay", source, dirs_exist_ok=True)
    runtime.mkdir()
    out = PACKAGE / "reports" / (args.report_name or "local-" + args.mode)
    out.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env.update(PATH=str(python.parent) + os.pathsep + env.get("PATH", ""),
               PYTHONPATH=str(source / "src"), PREFECT_HOME=str(runtime / "home"),
               PREFECT_SERVER_DATABASE_CONNECTION_URL="sqlite+aiosqlite:///" + (runtime / "test.db").as_posix(),
               PREFECT_SERVER_ANALYTICS_ENABLED="false", PYTHONDONTWRITEBYTECODE="1", PYTHONUNBUFFERED="1",
               NO_PROXY="localhost,127.0.0.1,::1", TMP=str(runtime), TEMP=str(runtime))
    for key in list(env):
        if key.lower() in {"http_proxy", "https_proxy", "all_proxy"}:
            env.pop(key)
    grade = load("grade", TASK / "tests/grade.py")
    groups = {
        "behavior": (["tests/events/server/triggers/test_incident_completed_run.py",
                      "tests/events/server/triggers/test_early_expect_events.py",
                      "tests/events/server/triggers/test_proactive_terminal_events.py"], 36),
        "retry": (["tests/server/orchestration/test_core_policy.py", "-k", grade.RETRY], 4),
        "compatibility": (["tests/events/server/triggers/test_basics.py", "-k", grade.COMPAT], 3),
    }
    result = {"mode": args.mode, "kind": "portable behavioral check, not Harbor CI",
              "python": str(python), "source": str(source), "groups": {}, "isolation_verified": False}
    for name, (targets, expected) in groups.items():
        if name not in args.groups.split(","):
            continue
        xml = out / (name + ".xml")
        command = [str(python), "-m", "pytest", *targets, "-q", "--tb=short", "--junitxml=" + str(xml),
                   "-o", "cache_dir=" + str(runtime / "cache"), "--basetemp=" + str(runtime / ("tmp-" + name))]
        print("Running", args.mode, name, flush=True)
        with (out / (name + ".log")).open("wb") as stream:
            child = subprocess.run(command, cwd=source, env=env, stdout=stream, stderr=subprocess.STDOUT, timeout=1200)
        result["groups"][name] = {"exit_code": child.returncode, "passed": grade.report_passed(xml, child.returncode, expected), "expected_tests": expected}
        print(result["groups"][name], flush=True)
    def portable_child(command, cwd, env, log, timeout):
        command[0] = str(python)
        with log.open("wb") as stream:
            return subprocess.run(command, cwd=cwd, env=env, stdout=stream, stderr=subprocess.STDOUT, timeout=timeout).returncode
    reliability = load("reliability", TASK / "tests/reliability.py")
    result["requested_groups"] = args.groups
    if "reliability" in args.groups.split(","):
        try:
            reliability.check(source, env, runtime, out, portable_child, baseline=baseline)
            result["reliability"] = {"passed": True}
        except Exception as exc:
            result["reliability"] = {"passed": False, "error": str(exc)}
    result["requested_groups_passed"] = all(g["passed"] for g in result["groups"].values()) and result.get("reliability", {"passed": True})["passed"]
    result["all_passed"] = set(args.groups.split(",")) == {"behavior", "retry", "compatibility", "reliability"} and result["requested_groups_passed"]
    (out / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
