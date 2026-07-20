from __future__ import annotations

import hashlib
import shutil
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from .discovery import discover_skills


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def build_archives(root: Path, *, clean: bool = False) -> list[Path]:
    root = root.resolve()
    dist = root / "dist" / "skills"
    if clean and dist.parent.exists():
        shutil.rmtree(dist.parent)
    dist.mkdir(parents=True, exist_ok=True)
    archives: list[Path] = []
    checksums: list[str] = []
    for record in discover_skills(root):
        version = str(record.manifest["version"])
        archive = dist / f"{record.name}-{version}.zip"
        with ZipFile(archive, "w", ZIP_DEFLATED) as bundle:
            for path in sorted(record.directory.rglob("*")):
                if path.is_file() and "__pycache__" not in path.parts:
                    arcname = Path(record.name) / path.relative_to(record.directory)
                    bundle.write(path, arcname.as_posix())
        archives.append(archive)
        checksums.append(f"{_sha256(archive)}  {archive.name}")
    (dist.parent / "checksums.sha256").write_text(
        "\n".join(checksums) + "\n",
        encoding="utf-8",
    )
    return archives
