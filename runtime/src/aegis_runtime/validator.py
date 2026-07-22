"""Registry validation services."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable, Mapping
from pathlib import Path
import re
from typing import Any

from .models import RegistryDocument, ValidationReport


class RegistryValidator:
    """Validates normalized Aegis registry documents."""

    _ASSET_ID_PATTERN = re.compile(
        r"^[a-z][a-z0-9-]*(?:\.[a-z0-9][a-z0-9-]*)+$"
    )
    _ENTRY_KEYS = (
        "entries", "assets", "skills", "playbooks", "patterns", "templates",
        "documents", "releases", "domains", "tags",
    )
    _SUPPORTED_SCHEMA_VERSIONS = {"0.1.0"}

    def __init__(
        self,
        repo_root: str | Path,
        *,
        unresolved_related_as_error: bool = False,
        strict_schema: bool = False,
    ) -> None:
        self.repo_root = Path(repo_root).resolve()
        self.unresolved_related_as_error = unresolved_related_as_error
        self.strict_schema = strict_schema

    def validate(self, documents: Iterable[RegistryDocument]) -> ValidationReport:
        document_list = list(documents)
        assets = [asset for document in document_list for asset in document.assets]
        report = ValidationReport(
            registry_count=len(document_list),
            asset_count=len(assets),
        )

        for document in document_list:
            for error in document.errors:
                report.add("error", "yaml_error", error, source_file=document.path)

            for code, message in self._document_schema_issues(document):
                report.add(
                    "error" if self.strict_schema else "warning",
                    code,
                    message,
                    source_file=document.path,
                )

        for asset in assets:
            if not asset.id:
                report.add(
                    "error",
                    "missing_id",
                    "Registry entry has no identifier.",
                    source_file=asset.source_file,
                )
            elif not self._ASSET_ID_PATTERN.fullmatch(asset.id):
                report.add(
                    "error",
                    "invalid_asset_id",
                    "Identifier must use lower-case dot notation: "
                    "for example, engineering.review-api-security.",
                    source_file=asset.source_file,
                    asset_id=asset.id,
                )

        counts = Counter(asset.id for asset in assets if asset.id)
        for asset_id, count in sorted(counts.items()):
            if count > 1:
                report.add(
                    "error",
                    "duplicate_id",
                    f"Identifier is declared {count} times.",
                    asset_id=asset_id,
                )

        declared_ids = {asset.id for asset in assets if asset.id}
        for asset in assets:
            if asset.path:
                resolved_path = self._resolve_asset_path(asset.path)
                if not self._is_safe_repository_path(resolved_path):
                    report.add(
                        "error",
                        "unsafe_path",
                        "Declared path must resolve inside the repository: "
                        f"{asset.path}",
                        source_file=asset.source_file,
                        asset_id=asset.id or None,
                    )
                    continue
                if not resolved_path.exists():
                    report.add(
                        "error",
                        "missing_path",
                        f"Declared path does not exist: {asset.path}",
                        source_file=asset.source_file,
                        asset_id=asset.id or None,
                    )

            for related_id in asset.related_assets:
                if related_id in declared_ids:
                    continue
                severity = "error" if self.unresolved_related_as_error else "warning"
                report.add(
                    severity,
                    "unresolved_related_asset",
                    f"Related asset is not registered: {related_id}",
                    source_file=asset.source_file,
                    asset_id=asset.id or None,
                )

        return report

    def _document_schema_issues(
        self,
        document: RegistryDocument,
    ) -> list[tuple[str, str]]:
        """Return structural diagnostics for a loaded YAML registry document."""

        raw = document.raw
        if raw is None:
            return []
        if not isinstance(raw, Mapping):
            return [("invalid_registry_document", "Registry document must be a YAML mapping.")]

        issues: list[tuple[str, str]] = []
        metadata = raw.get("registry")
        if not isinstance(metadata, Mapping):
            return [("missing_registry_metadata", "Registry metadata mapping 'registry' is required.")]

        for field in ("id", "name", "schema_version"):
            value = metadata.get(field)
            if not isinstance(value, str) or not value.strip():
                issues.append(
                    (
                        "invalid_registry_metadata",
                        f"Registry metadata field '{field}' must be a non-empty string.",
                    )
                )

        schema_version = metadata.get("schema_version")
        if (
            isinstance(schema_version, str)
            and schema_version.strip()
            and schema_version not in self._SUPPORTED_SCHEMA_VERSIONS
        ):
            issues.append(
                (
                    "unsupported_schema_version",
                    f"Unsupported registry schema version: {schema_version}.",
                )
            )

        collection_keys = [key for key in self._ENTRY_KEYS if key in raw]
        if not collection_keys:
            issues.append(
                (
                    "missing_registry_entries",
                    "Registry must contain one supported entries collection.",
                )
            )
            return issues

        for key in collection_keys:
            entries: Any = raw[key]
            if not isinstance(entries, list):
                issues.append(
                    (
                        "invalid_registry_entries",
                        f"Registry collection '{key}' must be a list.",
                    )
                )
                continue
            for index, entry in enumerate(entries, start=1):
                if not isinstance(entry, Mapping):
                    issues.append(
                        (
                            "invalid_registry_entry",
                            f"Registry collection '{key}' entry {index} must be a mapping.",
                        )
                    )

        return issues

    def _resolve_asset_path(self, declared_path: str) -> Path:
        path = Path(declared_path)
        return path if path.is_absolute() else self.repo_root / path

    def _is_safe_repository_path(self, path: Path) -> bool:
        """Return whether a resolved asset path remains within this repository."""

        try:
            path.resolve().relative_to(self.repo_root)
        except (OSError, ValueError):
            return False
        return True
