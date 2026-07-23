"""Safe discovery and validation of declarative Aegis plugins.

This module deliberately reads manifests only.  Loading a manifest must never
import or execute third-party plugin code.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

_PLUGIN_ID = re.compile(r"^[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*$")
_VERSION = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


@dataclass(frozen=True, slots=True)
class PluginIssue:
    """One manifest diagnostic."""

    code: str
    message: str
    path: Path

    def to_dict(self) -> dict[str, str]:
        return {"code": self.code, "message": self.message, "path": str(self.path)}


@dataclass(frozen=True, slots=True)
class PluginManifest:
    """A validated, declarative plugin manifest."""

    id: str
    name: str
    version: str
    entrypoint: str
    path: Path
    description: str = ""

    def to_dict(self) -> dict[str, str]:
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "entrypoint": self.entrypoint,
            "description": self.description,
            "path": str(self.path),
        }


@dataclass(slots=True)
class PluginReport:
    """The result of scanning the repository's plugin manifests."""

    plugins: list[PluginManifest]
    issues: list[PluginIssue]

    @property
    def ok(self) -> bool:
        return not self.issues

    def to_dict(self) -> dict[str, object]:
        return {
            "plugin_count": len(self.plugins),
            "plugins": [plugin.to_dict() for plugin in self.plugins],
            "errors": [issue.to_dict() for issue in self.issues],
        }


def discover_plugins(repo_root: str | Path) -> PluginReport:
    """Discover plugin manifests under ``plugins/`` without executing them."""

    root = Path(repo_root).resolve()
    plugins_root = root / "plugins"
    if not plugins_root.is_dir():
        return PluginReport(plugins=[], issues=[])

    manifests: list[PluginManifest] = []
    issues: list[PluginIssue] = []
    for path in sorted(plugins_root.rglob("aegis-plugin.yaml")):
        manifest, manifest_issues = _read_manifest(path)
        issues.extend(manifest_issues)
        if manifest is not None:
            manifests.append(manifest)

    duplicate_ids = {plugin.id for plugin in manifests if sum(item.id == plugin.id for item in manifests) > 1}
    for plugin in manifests:
        if plugin.id in duplicate_ids:
            issues.append(PluginIssue("duplicate_plugin_id", f"Plugin id is declared more than once: {plugin.id}", plugin.path))

    return PluginReport(plugins=manifests, issues=issues)


def _read_manifest(path: Path) -> tuple[PluginManifest | None, list[PluginIssue]]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return None, [PluginIssue("yaml_error", str(exc), path)]

    if not isinstance(data, dict):
        return None, [PluginIssue("invalid_manifest", "Plugin manifest root must be a mapping.", path)]

    issues: list[PluginIssue] = []
    fields: dict[str, str] = {}
    for name in ("id", "name", "version", "entrypoint"):
        value = data.get(name)
        if not isinstance(value, str) or not value.strip():
            issues.append(PluginIssue("missing_field", f"Plugin manifest requires a non-empty '{name}' field.", path))
        else:
            fields[name] = value.strip()

    if "id" in fields and not _PLUGIN_ID.fullmatch(fields["id"]):
        issues.append(PluginIssue("invalid_plugin_id", "Plugin id must use lowercase letters, digits, dots or hyphens.", path))
    if "version" in fields and not _VERSION.fullmatch(fields["version"]):
        issues.append(PluginIssue("invalid_version", "Plugin version must use semantic version format (for example 1.0.0).", path))
    if "entrypoint" in fields and (fields["entrypoint"].count(":") != 1 or any(not part for part in fields["entrypoint"].split(":"))):
        issues.append(PluginIssue("invalid_entrypoint", "Plugin entrypoint must use module:function syntax.", path))

    if issues:
        return None, issues

    description = data.get("description", "")
    if not isinstance(description, str):
        issues.append(PluginIssue("invalid_description", "Plugin description must be a string.", path))
        return None, issues

    return PluginManifest(path=path, description=description.strip(), **fields), issues
