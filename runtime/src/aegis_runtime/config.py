"""Repository and runtime configuration discovery."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    result = dict(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


@dataclass(slots=True)
class AegisConfig:
    """Resolved Aegis repository paths and merged YAML configuration."""

    repo_root: Path
    registry_root: Path
    config_root: Path
    values: dict[str, Any] = field(default_factory=dict)
    loaded_files: list[Path] = field(default_factory=list)

    @classmethod
    def discover(cls, start: str | Path | None = None) -> "AegisConfig":
        repo_root = cls.find_repo_root(start)
        config = cls(
            repo_root=repo_root,
            registry_root=repo_root / "registry",
            config_root=repo_root / "config",
        )
        config.load()
        return config

    @staticmethod
    def find_repo_root(start: str | Path | None = None) -> Path:
        candidates: list[Path] = []
        env_home = os.environ.get("AEGIS_HOME")
        if env_home:
            candidates.append(Path(env_home).expanduser())
        candidates.append(Path(start).expanduser() if start else Path.cwd())
        candidates.append(Path(__file__).resolve())

        visited: set[Path] = set()
        for candidate in candidates:
            candidate = candidate.resolve()
            if candidate.is_file():
                candidate = candidate.parent
            for current in (candidate, *candidate.parents):
                if current in visited:
                    continue
                visited.add(current)
                if (current / "registry").is_dir():
                    return current

        raise FileNotFoundError(
            "Unable to locate the Aegis OS repository. "
            "Use --repo-root or set AEGIS_HOME."
        )

    def load(self) -> dict[str, Any]:
        merged: dict[str, Any] = {}
        self.loaded_files.clear()
        filenames = (
            "aegis.config.example.yaml",
            "aegis.config.yaml",
            "aegis.config.local.yaml",
        )

        for filename in filenames:
            path = self.config_root / filename
            if not path.is_file():
                continue
            content = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            if not isinstance(content, dict):
                raise ValueError(f"Configuration root must be a mapping: {path}")
            merged = _deep_merge(merged, content)
            self.loaded_files.append(path)

        self.values = merged
        return merged
