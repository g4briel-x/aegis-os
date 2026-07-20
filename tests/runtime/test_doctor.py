import subprocess
from pathlib import Path

from aegis_runtime.doctor import (
    REQUIRED_FILES,
    REQUIRED_FOLDERS,
    check_git_status,
    check_repository_structure,
    check_required_indexes,
    run_all_checks,
)


def _make_complete_repo(tmp_path: Path) -> Path:
    for folder in REQUIRED_FOLDERS:
        (tmp_path / folder).mkdir(parents=True, exist_ok=True)
    for file in REQUIRED_FILES:
        target = tmp_path / file
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("placeholder\n", encoding="utf-8")
    return tmp_path


def test_check_repository_structure_reports_missing_folders(tmp_path: Path) -> None:
    result = check_repository_structure(tmp_path)
    assert not result.ok
    assert "core" in result.failures
    assert "scripts/validation" in result.failures


def test_check_repository_structure_passes_when_complete(tmp_path: Path) -> None:
    _make_complete_repo(tmp_path)
    result = check_repository_structure(tmp_path)
    assert result.ok
    assert not result.failures


def test_check_required_indexes_reports_missing_files(tmp_path: Path) -> None:
    result = check_required_indexes(tmp_path)
    assert not result.ok
    assert "README.md" in result.failures


def test_check_required_indexes_passes_when_complete(tmp_path: Path) -> None:
    _make_complete_repo(tmp_path)
    result = check_required_indexes(tmp_path)
    assert result.ok


def test_check_git_status_reports_failure_outside_git_repo(tmp_path: Path) -> None:
    result = check_git_status(tmp_path)
    assert not result.ok


def test_check_git_status_reports_clean_tree(tmp_path: Path) -> None:
    subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.email", "test@example.com"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Test"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    (tmp_path / "README.md").write_text("test\n", encoding="utf-8")
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "init"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    result = check_git_status(tmp_path)
    assert result.ok
    assert not result.warnings


def test_check_git_status_warns_on_dirty_tree(tmp_path: Path) -> None:
    subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.email", "test@example.com"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Test"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    (tmp_path / "README.md").write_text("uncommitted\n", encoding="utf-8")

    result = check_git_status(tmp_path)
    assert result.ok
    assert result.warnings


def test_run_all_checks_returns_three_checks(tmp_path: Path) -> None:
    checks = run_all_checks(tmp_path)
    assert [check.name for check in checks] == [
        "repository-structure",
        "required-indexes",
        "git-status",
    ]
