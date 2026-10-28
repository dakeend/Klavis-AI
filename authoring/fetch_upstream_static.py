"""Fetch the exact official static-check snapshot used in the packaged report."""
import argparse
import concurrent.futures
import hashlib
import io
from pathlib import Path
import re
import tarfile
import urllib.request

COMMIT = "6964e9252c90227fc1cfa26cbc59aee4134792e4"
TOOL_SHA = "88845bfbe4918596f00eb77ebeec8a0826026c9b24bcc83053cae48402e95ea6"


def download(url):
    with urllib.request.urlopen(url, timeout=60) as response:
        return response.read()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(".runtime/upstream-static"))
    root = parser.parse_args().output.resolve()
    base = "https://raw.githubusercontent.com/harbor-framework/terminal-bench/" + COMMIT + "/"
    workflow = download(base + ".github/workflows/static-checks.yml")
    scripts = re.findall(r'\|([^|"\n]+\.sh)"', workflow.decode())
    paths = ["scripts/checks/" + n for n in scripts] + ["scripts/checks/check-cpu-threads.py", "docs/TAXONOMY.yaml", "LICENSE"]
    def fetch(path):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(download(base + path))
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        list(pool.map(fetch, paths))
    (root / "UPSTREAM_COMMIT").write_text(COMMIT + "\n")
    tool = download("https://github.com/azu/dockerfile-pin/releases/download/v1.5.0/dockerfile-pin_linux_amd64.tar.gz")
    if hashlib.sha256(tool).hexdigest() != TOOL_SHA:
        raise ValueError("dockerfile-pin checksum mismatch")
    binary = root / "bin/dockerfile-pin"
    binary.parent.mkdir(exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(tool)) as archive:
        binary.write_bytes(archive.extractfile("dockerfile-pin").read())
    binary.chmod(0o755)
    print(str(root), COMMIT, len(scripts), "official scripts")


if __name__ == "__main__":
    main()
