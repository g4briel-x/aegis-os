from pathlib import Path

from aegis_skills.discovery import discover_skills
from aegis_skills.validation import validate_repository

ROOT = Path(__file__).resolve().parents[1]


def test_skill_count() -> None:
    assert len(discover_skills(ROOT)) == 37


def test_repository_is_valid() -> None:
    result = validate_repository(ROOT, strict=True)
    assert result.is_valid, result.issues
    assert not result.warnings, result.issues


def test_no_powershell_files() -> None:
    assert not list(ROOT.rglob("*.ps1"))


def test_no_embedded_git_directory() -> None:
    assert not [path for path in ROOT.rglob(".git") if path.is_dir()]
