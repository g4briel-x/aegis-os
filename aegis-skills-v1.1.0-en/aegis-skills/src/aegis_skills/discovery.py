from __future__ import annotations

import json
from pathlib import Path

from .frontmatter import parse_frontmatter_file
from .models import SkillRecord


def discover_skills(root: Path) -> list[SkillRecord]:
    skills_root = root / "skills"
    records: list[SkillRecord] = []
    for skill_file in sorted(skills_root.glob("*/*/SKILL.md")):
        metadata, _ = parse_frontmatter_file(skill_file)
        manifest_path = skill_file.parent / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
        records.append(
            SkillRecord(
                name=str(metadata.get("name", "")),
                description=str(metadata.get("description", "")),
                directory=skill_file.parent,
                skill_file=skill_file,
                manifest=manifest,
            )
        )
    return records
