from __future__ import annotations

import json
import py_compile
import re
from pathlib import Path
from urllib.parse import unquote
from zipfile import ZipFile

from jsonschema import Draft202012Validator

from .discovery import discover_skills
from .frontmatter import FrontmatterError, parse_frontmatter_file
from .models import ValidationIssue, ValidationResult
from .registry import load_registry

_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
_XML = re.compile(r"<[^>]+>")
_RESERVED = {"anthropic", "claude"}


def _issue(result: ValidationResult, severity: str, code: str, path: Path | str, message: str) -> None:
    result.issues.append(ValidationIssue(severity, code, str(path), message))


def _validate_json_schema(root: Path, instance_path: Path, schema_path: Path, result: ValidationResult) -> None:
    try:
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        _issue(result, "error", "json-invalid", instance_path, str(exc))
        return
    for error in sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda item: list(item.path)):
        location = "/".join(str(part) for part in error.path)
        _issue(result, "error", "schema-invalid", instance_path, f"{location}: {error.message}")


def validate_repository(root: Path, *, check_dist: bool = False, strict: bool = False) -> ValidationResult:
    root = root.resolve()
    result = ValidationResult()
    required = [
        "README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md", "pyproject.toml",
        "registry/skills.registry.yaml", "schemas/skill-manifest.schema.json",
        "schemas/skills-registry.schema.json", "schemas/evals.schema.json",
    ]
    for relative in required:
        path = root / relative
        if not path.exists():
            _issue(result, "error", "required-missing", relative, "required repository file is missing")

    for forbidden in root.rglob("*"):
        if forbidden.name == ".git" and forbidden.is_dir():
            _issue(result, "error", "embedded-git", forbidden.relative_to(root), "embedded .git directory must not be packaged")
        if forbidden.suffix.lower() == ".ps1":
            _issue(result, "error", "powershell-forbidden", forbidden.relative_to(root), "PowerShell automation is not allowed in this Python repository")

    try:
        registry = load_registry(root)
    except Exception as exc:
        _issue(result, "error", "registry-invalid", "registry/skills.registry.yaml", str(exc))
        registry = {"skills": []}

    registry_schema = root / "schemas" / "skills-registry.schema.json"
    if registry_schema.exists() and (root / "registry/skills.registry.json").exists():
        _validate_json_schema(root, root / "registry/skills.registry.json", registry_schema, result)

    registry_entries = registry.get("skills", []) if isinstance(registry, dict) else []
    by_id: dict[str, dict] = {}
    for entry in registry_entries:
        if not isinstance(entry, dict):
            _issue(result, "error", "registry-entry-invalid", "registry/skills.registry.yaml", "entry is not a mapping")
            continue
        skill_id = str(entry.get("id", ""))
        if skill_id in by_id:
            _issue(result, "error", "registry-duplicate-id", "registry/skills.registry.yaml", skill_id)
        by_id[skill_id] = entry
        path = root / str(entry.get("path", ""))
        if not path.is_dir():
            _issue(result, "error", "registry-path-missing", entry.get("path", ""), "skill directory does not exist")

    discovered = []
    for skill_file in sorted((root / "skills").glob("*/*/SKILL.md")):
        result.skills_checked += 1
        try:
            metadata, body = parse_frontmatter_file(skill_file)
        except FrontmatterError as exc:
            _issue(result, "error", "frontmatter-invalid", skill_file.relative_to(root), str(exc))
            continue
        name = metadata.get("name")
        description = metadata.get("description")
        if not isinstance(name, str) or not _NAME.fullmatch(name) or len(name) > 64:
            _issue(result, "error", "name-invalid", skill_file.relative_to(root), "name must be <=64 chars and use lowercase letters, digits and hyphens")
        elif any(token in _RESERVED for token in name.split("-")):
            _issue(result, "error", "name-reserved", skill_file.relative_to(root), "name contains a reserved word")
        elif skill_file.parent.name != name:
            _issue(result, "error", "folder-name-mismatch", skill_file.parent.relative_to(root), f"folder must match name {name!r}")
        if not isinstance(description, str) or not 1 <= len(description) <= 1024 or _XML.search(description):
            _issue(result, "error", "description-invalid", skill_file.relative_to(root), "description must be 1..1024 chars and contain no XML tags")
        line_count = skill_file.read_text(encoding="utf-8").count("\n") + 1
        if line_count > 500:
            severity = "error" if strict else "warning"
            _issue(result, severity, "skill-too-long", skill_file.relative_to(root), f"SKILL.md has {line_count} lines; keep it under 500")
        if not body.strip():
            _issue(result, "error", "skill-body-empty", skill_file.relative_to(root), "SKILL.md body is empty")

        manifest_path = skill_file.parent / "manifest.json"
        evals_path = skill_file.parent / "evals" / "evals.json"
        if not manifest_path.exists():
            _issue(result, "error", "manifest-missing", manifest_path.relative_to(root), "manifest.json is required by Aegis")
            manifest = {}
        else:
            _validate_json_schema(root, manifest_path, root / "schemas/skill-manifest.schema.json", result)
            try:
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                manifest = {}
        if manifest:
            if manifest.get("id") != name:
                _issue(result, "error", "manifest-id-mismatch", manifest_path.relative_to(root), "manifest id differs from frontmatter name")
            entry = by_id.get(str(name))
            if entry is None:
                _issue(result, "error", "registry-entry-missing", skill_file.relative_to(root), "skill is not registered")
            else:
                expected_path = skill_file.parent.relative_to(root).as_posix()
                if entry.get("path") != expected_path:
                    _issue(result, "error", "registry-path-mismatch", skill_file.relative_to(root), f"registry path must be {expected_path}")
                if entry.get("version") != manifest.get("version"):
                    _issue(result, "error", "version-mismatch", manifest_path.relative_to(root), "registry and manifest versions differ")
        if evals_path.exists():
            _validate_json_schema(root, evals_path, root / "schemas/evals.schema.json", result)
        else:
            _issue(result, "warning", "evals-missing", evals_path.relative_to(root), "no evals file")

        for markdown in skill_file.parent.rglob("*.md"):
            text = markdown.read_text(encoding="utf-8")
            for target in _LINK.findall(text):
                target = unquote(target.split("#", 1)[0].strip())
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                resolved = (markdown.parent / target).resolve()
                try:
                    resolved.relative_to(skill_file.parent.resolve())
                except ValueError:
                    _issue(result, "error", "link-escapes-skill", markdown.relative_to(root), target)
                    continue
                if not resolved.exists():
                    _issue(result, "error", "link-missing", markdown.relative_to(root), target)
        discovered.append(str(name))

    missing_discovery = sorted(set(by_id) - set(discovered))
    for skill_id in missing_discovery:
        _issue(result, "error", "registered-not-discovered", "registry/skills.registry.yaml", skill_id)

    for python_file in root.rglob("*.py"):
        if any(part in {".venv", "dist", "build"} for part in python_file.parts):
            continue
        try:
            py_compile.compile(str(python_file), doraise=True)
        except py_compile.PyCompileError as exc:
            _issue(result, "error", "python-syntax", python_file.relative_to(root), str(exc))

    if check_dist:
        dist = root / "dist" / "skills"
        for entry in registry_entries:
            name = entry.get("id")
            version = entry.get("version")
            archive = dist / f"{name}-{version}.zip"
            if not archive.exists():
                _issue(result, "error", "dist-missing", archive.relative_to(root), "skill archive is missing")
                continue
            with ZipFile(archive) as bundle:
                names = bundle.namelist()
                expected = f"{name}/SKILL.md"
                if expected not in names:
                    _issue(result, "error", "dist-structure", archive.relative_to(root), f"missing {expected}")
                roots = {item.split("/", 1)[0] for item in names if item}
                if roots != {name}:
                    _issue(result, "error", "dist-root", archive.relative_to(root), f"archive roots are {sorted(roots)}")
    return result
