# Aegis Skill Authoring Standard

## Mandatory requirements

Every skill must have a directory whose name exactly matches the `name` field in the `SKILL.md` frontmatter.

`SKILL.md` must:

- begin with YAML frontmatter;
- define `name` and `description`;
- use a lowercase identifier containing only letters, digits, and hyphens, with a maximum length of 64 characters;
- provide a description between 1 and 1024 characters that explains both capability and trigger conditions;
- remain below 500 lines;
- explicitly reference supporting resources.

## Minimum Aegis structure

```text
skill-name/
├── SKILL.md
├── manifest.json
├── LICENSE.txt
├── references/
├── templates/
├── examples/
└── evals/
```

## Progressive disclosure

1. Frontmatter supports discovery and triggering.
2. The `SKILL.md` body contains the primary operating workflow.
3. References, templates, examples, and evaluations are loaded only when needed.

## Quality rules

- Instructions must be imperative, testable, and proportionate to risk.
- No unverifiable claims of real employment or internal access.
- No secret, personal, or confidential data.
- No destructive or surprising automation.
- Trigger and quality tests must be defined in `evals/evals.json`.
