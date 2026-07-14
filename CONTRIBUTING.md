## FILE: `CONTRIBUTING.md`

# Contributing to Aegis OS

Thank you for contributing to Aegis OS.

Aegis OS is a structured AI operating framework. Contributions should preserve clarity, governance, validation and repository consistency.

---

## 1. Contribution Areas

Contributions may include:

```text
documentation
skills
playbooks
patterns
templates
registries
validation scripts
report scripts
CLI commands
tests
GitHub workflows
```

---

## 2. Before Contributing

Run these checks locally:

```powershell
.\cli\aegis.ps1 status
.\cli\aegis.ps1 doctor
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
```

---

## 3. File Standards

Every new asset should include:

```text
clear purpose
role of the file
expected usage
quality checklist
examples when useful
metadata when required
```

---

## 4. Registry Updates

When adding a new asset, update the relevant registry:

```text
registry/skills/skills.registry.yaml
registry/playbooks/playbooks.registry.yaml
registry/patterns/patterns.registry.yaml
registry/templates/templates.registry.yaml
registry/docs/docs.registry.yaml
```

Registry entries should include:

```text
id
name
domain
path
tags
status
maturity
related_assets when useful
```

---

## 5. Commit Style

Recommended commit examples:

```text
docs: add root documentation for v0.5
feat(cli): add registry exploration commands
test(cli): add metadata command tests
ci(cli): add cli smoke test workflow
chore: close aegis os v0.5 foundation
```

---

## 6. Pull Request Checklist

Before opening a pull request:

```text
[ ] Files are placed in the correct folder
[ ] Documentation explains the role of the file
[ ] Registry updated if an asset was added
[ ] CLI command map updated if a command was added
[ ] Smoke tests updated if a command was added
[ ] Validation passes
[ ] Reports generate successfully
```

---

## 7. Final Principle

> Contributions should make Aegis OS more structured, reusable, testable and governable.
