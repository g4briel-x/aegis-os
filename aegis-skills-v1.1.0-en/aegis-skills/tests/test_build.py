from pathlib import Path
from zipfile import ZipFile

from aegis_skills.builder import build_archives
from aegis_skills.discovery import discover_skills

ROOT = Path(__file__).resolve().parents[1]


def test_build_archives(tmp_path: Path) -> None:
    # Build uses the repository dist directory; verify each ZIP has one skill root.
    archives = build_archives(ROOT, clean=True)
    assert len(archives) == len(discover_skills(ROOT))
    for archive in archives:
        with ZipFile(archive) as bundle:
            names = bundle.namelist()
            assert any(name.endswith("/SKILL.md") for name in names)
            roots = {name.split("/", 1)[0] for name in names}
            assert len(roots) == 1
