"""Re-export the pinned server snapshot without the original author workspace."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

PACKAGE = Path(__file__).resolve().parents[1]
TASK = PACKAGE / "tasks/prefect-monitor"
BASE = "71d1906204dfca1bd2dff36b57bcfc46dd7a2dd8"
PATHS = ["src", "tests", "tools", "docs/contribute", "pyproject.toml", "uv.lock", "hatch_build.py", "README.md", "LICENSE", ".gitignore", "AGENTS.md"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True, help="Existing local Prefect clone containing the pinned commit")
    repo = parser.parse_args().repository.resolve()
    expected = json.loads((PACKAGE / "manifest.json").read_text("utf-8"))["baseline_gzip_sha256"]
    with tempfile.TemporaryDirectory() as temporary:
        tar = Path(temporary) / "source.tar"
        subprocess.run(["git", "-c", "safe.directory=" + repo.as_posix(), "-c", "core.autocrlf=false",
                        "-C", str(repo), "archive", "--format=tar", "--output=" + str(tar), BASE, *PATHS], check=True)
        compressed = Path(temporary) / "baseline.tar.gz"
        with tar.open("rb") as source, compressed.open("wb") as raw, gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as destination:
            shutil.copyfileobj(source, destination)
        digest = hashlib.sha256(compressed.read_bytes()).hexdigest()
        if digest != expected:
            raise ValueError(f"Export differs from frozen input: {digest}; original task files were not overwritten")
        for context in ["environment", "tests"]:
            shutil.copyfile(compressed, TASK / context / "data/baseline.tar.gz")
    print("Reproduced frozen input:", digest)


if __name__ == "__main__":
    main()
