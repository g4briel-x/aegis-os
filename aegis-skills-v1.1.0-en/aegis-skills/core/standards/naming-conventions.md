# Naming Conventions

## Skill identifiers

- Use lowercase kebab-case.
- Use a stable professional role or capability name.
- Keep identifiers at or below 64 characters.
- Do not include vendor-reserved names as standalone identifier tokens.

## Categories

Categories use a two-digit ordering prefix followed by a kebab-case name, for example `02-engineering`.

## Files and directories

- Required skill entry point: `SKILL.md`.
- Skill metadata: `manifest.json`.
- Evaluations: `evals/evals.json`.
- Detailed knowledge: `references/`.
- Reusable output structures: `templates/`.
- Representative requests: `examples/`.

## Versions

Use semantic versioning. Registry and manifest versions must match exactly.
