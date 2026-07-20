# Contributing to Aegis Skills

## Authoring rules

1. Create or modify a skill under `skills/<category>/<skill-name>/`.
2. Keep the same identifier in the directory name, `SKILL.md` frontmatter, `manifest.json`, and both registries.
3. Keep `SKILL.md` concise and move detailed material into `references/`, `templates/`, `examples/`, or `evals/`.
4. Add or update trigger and quality evaluations.
5. Preserve stable file names, schema keys, paths, and CLI contracts unless a versioned migration is explicitly approved.
6. Document user-visible changes in `CHANGELOG.md`.
7. Run validation, tests, and a clean build before committing.

## Required checks

```bash
python -m aegis_skills validate --root . --strict
python -m pytest
python -m aegis_skills build --root . --clean
python -m aegis_skills validate --root . --strict --check-dist
```

## Automation policy

Do not add PowerShell automation. Repository automation is implemented in Python so that Aegis Skills remains aligned with the Python-based Aegis OS runtime and works across Windows, macOS, and Linux.

## Content quality

- Use precise, testable, imperative instructions.
- Separate facts, assumptions, decisions, and residual risk.
- Do not claim unverifiable employment, certifications, research, metrics, or test results.
- Prefer official and primary references for unstable technical information.
- Write all user-facing content in English for this edition.
