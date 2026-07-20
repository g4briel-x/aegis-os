"""Repository health checks (Python port of scripts/doctor/*.ps1)."""

from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class DoctorCheckResult:
    """Result of one doctor check."""

    name: str
    ok: bool
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "ok": self.ok,
            "failures": list(self.failures),
            "warnings": list(self.warnings),
        }


REQUIRED_FOLDERS = (
    "core",
    "shared",
    "docs",
    "skills",
    "playbooks",
    "patterns",
    "templates",
    "registry",
    "scripts",
    "scripts/validation",
    "scripts/reports",
    "scripts/doctor",
    "scripts/testing",
    "cli",
    "cli/commands",
    "config",
    "reports",
    "install",
    ".github",
    ".github/workflows",
)

REQUIRED_FILES = (
    "README.md",
    "QUICKSTART.md",
    "PROJECT_STATUS.md",
    "CHANGELOG.md",
    "RELEASE_NOTES_v0.5.md",
    "V0_5_CLOSURE_REPORT.md",
    "V0_5_RELEASE_CHECKLIST.md",
    "MANIFEST.md",
    "docs/INDEX.md",
    "skills/INDEX.md",
    "playbooks/INDEX.md",
    "patterns/INDEX.md",
    "templates/INDEX.md",
    "registry/INDEX.md",
    "reports/README.md",
    "scripts/README.md",
    "cli/COMMANDS.md",
    "cli/CLI_USAGE.md",
    "config/README.md",
)


def check_repository_structure(repo_root: Path) -> DoctorCheckResult:
    """Verify that required repository folders exist."""

    failures = [
        folder
        for folder in REQUIRED_FOLDERS
        if not (repo_root / folder).is_dir()
    ]
    return DoctorCheckResult(
        name="repository-structure",
        ok=not failures,
        failures=failures,
    )


def check_required_indexes(repo_root: Path) -> DoctorCheckResult:
    """Verify that required index/manifest files exist."""

    failures = [
        file
        for file in REQUIRED_FILES
        if not (repo_root / file).is_file()
    ]
    return DoctorCheckResult(
        name="required-indexes",
        ok=not failures,
        failures=failures,
    )


def check_git_status(repo_root: Path) -> DoctorCheckResult:
    """Verify Git availability and report working tree status."""

    failures: list[str] = []
    warnings: list[str] = []

    git = shutil.which("git")
    if git is None:
        return DoctorCheckResult(
            name="git-status",
            ok=False,
            failures=["Git is not available on PATH."],
        )

    def _run(*args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [git, *args],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=False,
        )

    inside = _run("rev-parse", "--is-inside-work-tree")
    if inside.returncode != 0 or inside.stdout.strip() != "true":
        failures.append(
            "Current folder is not inside a Git working tree."
        )
        return DoctorCheckResult(
            name="git-status",
            ok=False,
            failures=failures,
        )

    branch = _run("branch", "--show-current")
    if branch.returncode != 0 or not branch.stdout.strip():
        warnings.append("Branch name unavailable or detached HEAD.")

    status = _run("status", "--short")
    if status.returncode != 0:
        failures.append("Could not read Git status.")
    elif status.stdout.strip():
        warnings.append("Working tree has uncommitted changes.")
        warnings.extend(
            line
            for line in status.stdout.splitlines()
            if line.strip()
        )

    return DoctorCheckResult(
        name="git-status",
        ok=not failures,
        failures=failures,
        warnings=warnings,
    )


def run_all_checks(repo_root: Path) -> list[DoctorCheckResult]:
    """Run every doctor check, in the same order as aegis-doctor.ps1."""

    return [
        check_repository_structure(repo_root),
        check_required_indexes(repo_root),
        check_git_status(repo_root),
    ]
