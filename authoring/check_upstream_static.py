"""Run a downloaded, pinned official check snapshot; preserve every result."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess

PACKAGE = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checks-dir", type=Path, required=True)
    args = parser.parse_args()
    snapshot = args.checks_dir.resolve()
    commit = (snapshot / "UPSTREAM_COMMIT").read_text().strip()
    checks = sorted((snapshot / "scripts/checks").glob("*.sh"))
    env = os.environ.copy()
    env.update(PATH=str(snapshot / "bin") + os.pathsep + env.get("PATH", ""),
               FIX_DIRS="", BASE_DIR=str(snapshot), TASK_DIRS="tasks/prefect-monitor")
    out = PACKAGE / "reports/upstream-static"
    out.mkdir(parents=True, exist_ok=True)
    result = {"upstream_commit": commit, "executed_at": datetime.now(timezone.utc).isoformat(),
              "scope": "official static scripts executed locally; not hosted CI or LLM quality review", "checks": []}
    for check in checks:
        code = subprocess.run(["bash", str(check), "tasks/prefect-monitor"], cwd=PACKAGE,
                              env=env, capture_output=True, text=True, timeout=90)
        log = code.stdout + code.stderr
        (out / (check.stem + ".log")).write_text(log, encoding="utf-8")
        result["checks"].append({"name": check.name, "exit_code": code.returncode,
                                  "sha256": hashlib.sha256(check.read_bytes()).hexdigest()})
        print(check.name, code.returncode, log[-800:] if code.returncode else "", flush=True)
    result["all_passed"] = all(c["exit_code"] == 0 for c in result["checks"])
    (out / "result.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
