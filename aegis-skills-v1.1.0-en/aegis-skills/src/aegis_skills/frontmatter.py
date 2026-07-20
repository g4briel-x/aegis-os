from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


class FrontmatterError(ValueError):
    pass


def parse_frontmatter_text(text: str) -> tuple[dict[str, Any], str]:
    match = _FRONTMATTER.match(text.replace("\r\n", "\n"))
    if not match:
        raise FrontmatterError("SKILL.md must start with YAML frontmatter")
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise FrontmatterError(f"invalid YAML frontmatter: {exc}") from exc
    if not isinstance(data, dict):
        raise FrontmatterError("frontmatter must be a mapping")
    return data, text[match.end():]


def parse_frontmatter_file(path: Path) -> tuple[dict[str, Any], str]:
    return parse_frontmatter_text(path.read_text(encoding="utf-8"))
