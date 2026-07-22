"""Safe, deterministic generators for Aegis OS assets."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

import yaml


GENERATED_FILES = (
    "SKILL.md",
    "README.md",
    "expertise.md",
    "workflows.md",
    "checklists.md",
    "prompts.md",
    "examples/examples.md",
)


@dataclass(frozen=True, slots=True)
class SkillDefinition:
    """Validated input used to generate one skill directory."""

    name: str
    category: str
    path: Path
    role: str
    mission: str
    responsibilities: str
    expertise: str


@dataclass(frozen=True, slots=True)
class GenerationResult:
    """Summary of one generated skill."""

    name: str
    definition_path: Path
    output_path: Path
    files: tuple[Path, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "definition_path": str(self.definition_path),
            "output_path": str(self.output_path),
            "files": [str(path) for path in self.files],
        }


def _required_text(values: Mapping[str, Any], key: str, source: Path) -> str:
    value = values.get(key)
    text = "" if value is None else str(value).strip()
    if not text:
        raise ValueError(f"Missing '{key}' field in skill definition: {source}")
    return text


def load_skill_definition(path: str | Path) -> SkillDefinition:
    """Load and validate one YAML skill definition."""

    source = Path(path).resolve()
    try:
        values = yaml.safe_load(source.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise FileNotFoundError(f"Skill definition file not found: {source}") from None
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise ValueError(f"Could not read skill definition {source}: {exc}") from exc

    if not isinstance(values, Mapping):
        raise ValueError(f"Skill definition must be a YAML mapping: {source}")

    relative_path = Path(_required_text(values, "path", source))
    if relative_path.is_absolute() or ".." in relative_path.parts:
        raise ValueError(
            "Skill definition path must stay below the skills directory: "
            f"{relative_path}"
        )

    return SkillDefinition(
        name=_required_text(values, "name", source),
        category=_required_text(values, "category", source),
        path=relative_path,
        role=_required_text(values, "role", source),
        mission=_required_text(values, "mission", source),
        responsibilities=_required_text(values, "responsibilities", source),
        expertise=_required_text(values, "expertise", source),
    )


def _render_skill(definition: SkillDefinition) -> dict[str, str]:
    return {
        "SKILL.md": f"""# {definition.name}

## Category

{definition.category}

## Mission

{definition.mission}

## Role

{definition.role}

## Responsibilities

{definition.responsibilities}

## Principles

- Quality first
- Evidence-based reasoning
- Continuous improvement
""",
        "README.md": f"""# {definition.name}

Professional expert module of Aegis OS.

## Mission

{definition.mission}

## Usage

Activated by the Aegis OS orchestration engine.
""",
        "expertise.md": f"""# Expertise

## {definition.name}

{definition.expertise}
""",
        "workflows.md": """# Workflows

## Standard workflow

1. Analyze
2. Investigate
3. Execute
4. Validate
5. Document
""",
        "checklists.md": """# Checklists

- [ ] Requirement understood
- [ ] Evidence collected
- [ ] Solution validated
- [ ] Documentation completed
""",
        "prompts.md": f"""# Activation prompt

Activate the {definition.name} skill and apply its professional methodology.
""",
        "examples/examples.md": f"""# Examples

Practical examples for {definition.name}.
""",
    }


def generate_skill(
    repo_root: str | Path,
    definition_path: str | Path,
    *,
    force: bool = False,
) -> GenerationResult:
    """Generate one skill without overwriting files unless explicitly allowed."""

    root = Path(repo_root).resolve()
    source = Path(definition_path)
    if not source.is_absolute():
        source = root / source
    definition = load_skill_definition(source)
    skills_root = (root / "skills").resolve()
    output = (skills_root / definition.path).resolve()
    if not output.is_relative_to(skills_root):
        raise ValueError(
            "Resolved skill path must stay below the skills directory: "
            f"{output}"
        )
    rendered = _render_skill(definition)
    targets = tuple(output / relative_path for relative_path in GENERATED_FILES)
    existing = [path for path in targets if path.exists()]

    if existing and not force:
        listed = ", ".join(str(path.relative_to(root)) for path in existing)
        raise FileExistsError(
            "Generation would overwrite existing files. "
            f"Use --force to allow it: {listed}"
        )

    for relative_path, content in rendered.items():
        target = output / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8", newline="\n")

    return GenerationResult(
        name=definition.name,
        definition_path=source.resolve(),
        output_path=output,
        files=targets,
    )


def generate_skills(
    repo_root: str | Path,
    definitions_dir: str | Path = "generators",
    *,
    force: bool = False,
) -> list[GenerationResult]:
    """Generate every YAML skill definition in deterministic filename order."""

    root = Path(repo_root).resolve()
    definitions = Path(definitions_dir)
    if not definitions.is_absolute():
        definitions = root / definitions
    if not definitions.is_dir():
        raise FileNotFoundError(f"Definitions directory not found: {definitions}")

    sources = sorted(
        path
        for path in definitions.iterdir()
        if path.is_file() and path.suffix.lower() in {".yaml", ".yml"}
    )
    if not sources:
        raise FileNotFoundError(f"No YAML definitions found in: {definitions}")

    return [generate_skill(root, source, force=force) for source in sources]
