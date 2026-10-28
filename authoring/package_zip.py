"""Create a portable task bundle and per-file integrity inventory."""
import hashlib
from pathlib import Path
import zipfile

PACKAGE = Path(__file__).resolve().parents[1]


def main():
    files = sorted(p for p in PACKAGE.rglob("*") if p.is_file() and not p.is_symlink()
                   and not any(part in {"__pycache__", ".runtime", ".venv", ".git", "jobs"} for part in p.relative_to(PACKAGE).parts)
                   and p.suffix != ".pyc" and p.name != "SHA256SUMS")
    inventory = PACKAGE / "SHA256SUMS"
    inventory.write_text("".join(hashlib.sha256(p.read_bytes()).hexdigest() + "  " + p.relative_to(PACKAGE).as_posix() + "\n" for p in files), encoding="utf-8", newline="\n")
    archive = PACKAGE.parent / "prefect-monitor-submission.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zipped:
        for path in [*files, inventory]:
            zipped.write(path, arcname="prefect-monitor-submission/" + path.relative_to(PACKAGE).as_posix())
    with zipfile.ZipFile(archive) as zipped:
        assert zipped.testzip() is None
    print(str(archive), "bytes=", archive.stat().st_size, "sha256=", hashlib.sha256(archive.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
