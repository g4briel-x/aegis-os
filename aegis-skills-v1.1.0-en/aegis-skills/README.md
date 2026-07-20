# Aegis Skills

A professional, versioned library of **37 specialized Agent Skills** for Aegis OS, Claude, Claude Code, and systems compatible with the `SKILL.md` convention.

## Design principles

- One independently packageable skill per directory.
- Valid discovery frontmatter with `name` and `description`.
- Progressive disclosure: concise operating instructions in `SKILL.md`, detailed guidance in `references/`.
- Python-only validation, inventory, and packaging automation.
- Reproducible registries, schemas, tests, reports, and standalone ZIP packages.
- Stable identifiers, file names, paths, JSON keys, YAML keys, and CLI contracts.

## Repository structure

```text
aegis-skills/
├── .github/workflows/     # continuous integration
├── core/                  # shared standards and templates
├── registry/              # categories and skill registry
├── schemas/               # JSON validation schemas
├── scripts/               # Python entry points
├── skills/                # source skill directories
├── src/aegis_skills/      # validation and packaging library
├── tests/                 # automated tests
├── reports/               # audit, migration, translation, and validation reports
└── dist/skills/           # standalone Claude-ready ZIP packages
```

## Requirements

- Python 3.11 or later
- Git

## Installation for development

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Validate the repository

```bash
python -m aegis_skills validate --root . --strict --check-dist
```

## Run tests

```bash
python -m pytest
```

## Build standalone skill packages

```bash
python -m aegis_skills build --root . --clean
```

Each archive under `dist/skills/` contains exactly one root directory named after the skill, with `SKILL.md` at the first level.

## Inspect the catalog

```bash
python -m aegis_skills inventory --root .
```

## Install in Claude

Upload the required ZIP from `dist/skills/`. Install only the specialized skills required for the target workflow.

## Install in Claude Code

Copy a skill directory into the project or user-level skills directory used by Claude Code, preserving its internal structure.

## Orchestration

The `aegis-software-studio` skill routes multi-domain work to the relevant specialists, coordinates handoffs, resolves contradictions, and consolidates a traceable result. For a narrow request, activate the specialized skill directly.

## Language edition

- Repository version: `1.1.0`
- Content language: English
- Stable technical identifiers and paths remain unchanged for Aegis OS compatibility.
