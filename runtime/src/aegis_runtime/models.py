"""Data models used by the Aegis runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping


@dataclass(slots=True)
class Asset:
    """Normalized representation of an Aegis registry asset."""

    id: str
    name: str = ""
    type: str = ""
    domain: str = ""
    path: str = ""
    tags: list[str] = field(default_factory=list)
    related_assets: list[str] = field(default_factory=list)
    source_file: Path | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def searchable_text(self) -> str:
        values = [
            self.id,
            self.name,
            self.type,
            self.domain,
            self.path,
            *self.tags,
            *self.related_assets,
            *self._metadata_search_values(self.metadata),
        ]
        return " ".join(str(value) for value in values if value).lower()

    @classmethod
    def _metadata_search_values(cls, value: Any) -> list[str]:
        """Flatten YAML metadata into stable, searchable text values."""

        if isinstance(value, Mapping):
            values: list[str] = []
            for key, item in value.items():
                values.append(str(key))
                values.extend(cls._metadata_search_values(item))
            return values
        if isinstance(value, list):
            return [item for nested in value for item in cls._metadata_search_values(nested)]
        return [str(value)] if value is not None else []

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "domain": self.domain,
            "path": self.path,
            "tags": list(self.tags),
            "related_assets": list(self.related_assets),
            "source_file": str(self.source_file) if self.source_file else None,
            "metadata": dict(self.metadata),
        }


@dataclass(slots=True)
class RegistryDocument:
    """One YAML registry file and its normalized assets."""

    path: Path
    name: str
    assets: list[Asset] = field(default_factory=list)
    raw: Any = None
    errors: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ValidationIssue:
    """One validation error or warning."""

    severity: str
    code: str
    message: str
    source_file: Path | None = None
    asset_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
            "source_file": str(self.source_file) if self.source_file else None,
            "asset_id": self.asset_id,
        }


@dataclass(slots=True)
class ValidationReport:
    """Aggregate result returned by the runtime validator."""

    issues: list[ValidationIssue] = field(default_factory=list)
    registry_count: int = 0
    asset_count: int = 0

    @property
    def errors(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.severity == "error"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.severity == "warning"]

    @property
    def ok(self) -> bool:
        return not self.errors

    def add(
        self,
        severity: str,
        code: str,
        message: str,
        *,
        source_file: Path | None = None,
        asset_id: str | None = None,
    ) -> None:
        self.issues.append(
            ValidationIssue(
                severity=severity,
                code=code,
                message=message,
                source_file=source_file,
                asset_id=asset_id,
            )
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "registry_count": self.registry_count,
            "asset_count": self.asset_count,
            "error_count": len(self.errors),
            "warning_count": len(self.warnings),
            "issues": [issue.to_dict() for issue in self.issues],
        }
