"""YAML registry loading and normalization."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

import yaml

from .models import Asset, RegistryDocument


class RegistryLoader:
    """Loads Aegis registry files from a repository."""

    def __init__(self, repo_root: str | Path) -> None:
        self.repo_root = Path(repo_root).resolve()
        self.registry_root = self.repo_root / "registry"

    def registry_files(self) -> list[Path]:
        if not self.registry_root.is_dir():
            return []
        return sorted(
            path
            for path in self.registry_root.rglob("*")
            if path.is_file() and path.suffix.lower() in {".yaml", ".yml"}
        )

    def load_all(self) -> list[RegistryDocument]:
        return [self.load_file(path) for path in self.registry_files()]

    def load_file(self, path: str | Path) -> RegistryDocument:
        source = Path(path).resolve()
        document = RegistryDocument(path=source, name=source.stem)

        try:
            raw = yaml.safe_load(source.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, yaml.YAMLError) as exc:
            document.errors.append(str(exc))
            return document

        document.raw = raw
        entries = self._extract_entries(raw)

        for entry in entries:
            if not isinstance(entry, Mapping):
                document.errors.append(f"Registry entry is not a mapping: {entry!r}")
                continue
            document.assets.append(self._normalize_asset(entry, source))

        return document

    @classmethod
    def _extract_entries(cls, raw: Any) -> list[Mapping[str, Any]]:
        if raw is None:
            return []
        if isinstance(raw, list):
            return [entry for entry in raw if isinstance(entry, Mapping)]
        if not isinstance(raw, Mapping):
            return []

        preferred_keys = (
            "entries",
            "assets",
            "skills",
            "playbooks",
            "patterns",
            "templates",
            "documents",
            "releases",
            "domains",
            "tags",
        )
        for key in preferred_keys:
            value = raw.get(key)
            if isinstance(value, list):
                return [entry for entry in value if isinstance(entry, Mapping)]

        for value in raw.values():
            if isinstance(value, list) and any(
                isinstance(entry, Mapping) and "id" in entry for entry in value
            ):
                return [entry for entry in value if isinstance(entry, Mapping)]

        if "id" in raw:
            return [raw]
        return []

    @classmethod
    def _normalize_asset(cls, entry: Mapping[str, Any], source_file: Path) -> Asset:
        asset_id = cls._clean_scalar(entry.get("id"))
        name = cls._clean_scalar(entry.get("name") or entry.get("title"))
        asset_type = cls._clean_scalar(
            entry.get("type") or entry.get("asset_type") or entry.get("kind")
        )
        domain = cls._clean_scalar(entry.get("domain"))
        path = cls._clean_scalar(entry.get("path"))
        tags = cls._normalize_string_list(entry.get("tags"))
        related = cls._normalize_string_list(
            entry.get("related_assets") or entry.get("related") or entry.get("relations")
        )

        known = {
            "id",
            "name",
            "title",
            "type",
            "asset_type",
            "kind",
            "domain",
            "path",
            "tags",
            "related_assets",
            "related",
            "relations",
        }
        metadata = {key: value for key, value in entry.items() if key not in known}

        return Asset(
            id=asset_id,
            name=name,
            type=asset_type,
            domain=domain,
            path=path,
            tags=tags,
            related_assets=related,
            source_file=source_file,
            metadata=metadata,
        )

    @staticmethod
    def _clean_scalar(value: Any) -> str:
        return "" if value is None else str(value).strip()

    @classmethod
    def _normalize_string_list(cls, value: Any) -> list[str]:
        if value is None:
            return []
        if isinstance(value, str):
            stripped = value.strip()
            return [item.strip() for item in stripped.split(",") if item.strip()]
        if isinstance(value, Iterable) and not isinstance(value, Mapping):
            normalized: list[str] = []
            for item in value:
                candidate = (
                    item.get("id") or item.get("name") or item.get("value")
                    if isinstance(item, Mapping)
                    else item
                )
                cleaned = cls._clean_scalar(candidate)
                if cleaned:
                    normalized.append(cleaned)
            return normalized
        cleaned = cls._clean_scalar(value)
        return [cleaned] if cleaned else []
