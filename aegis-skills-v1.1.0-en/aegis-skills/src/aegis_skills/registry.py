from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_registry(root: Path) -> dict[str, Any]:
    path = root / "registry" / "skills.registry.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("registry must be a mapping")
    return data
