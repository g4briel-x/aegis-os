## FILE: `V0_5_RELEASE_CHECKLIST.md`

# Aegis OS v0.5 — Release Checklist

Release: v0.5.0  
Name: CLI + Automation Foundation  
Status: Final Checklist

---

# 1. Documentation Checklist

Required files:

```text
README.md
QUICKSTART.md
PROJECT_STATUS.md
CHANGELOG.md
RELEASE_NOTES_v0.5.md
V0_5_CLOSURE_REPORT.md
V0_5_RELEASE_CHECKLIST.md
```

Checklist:

```text
[ ] README.md exists
[ ] QUICKSTART.md exists
[ ] PROJECT_STATUS.md exists
[ ] CHANGELOG.md exists
[ ] RELEASE_NOTES_v0.5.md exists
[ ] V0_5_CLOSURE_REPORT.md exists
[ ] V0_5_RELEASE_CHECKLIST.md exists
```

---

# 2. CLI Checklist

Required commands:

```text
help
version
info
status
doctor
validate
report
registry:list
skill:list
playbook:list
pattern:list
template:list
domain:list
tag:list
docs:list
release:status
asset:find
asset:show
asset:related
asset:path
asset:open
domain:assets
tag:assets
config:path
config:check
config:show
```

Checklist:

```text
[ ] CLI entrypoint exists
[ ] Help command works
[ ] Metadata commands work
[ ] Registry commands work
[ ] Asset commands work
[ ] Config commands work
[ ] Doctor command works
[ ] Validation command works
[ ] Report command works
```

---

# 3. Automation Checklist

Required folders:

```text
scripts/validation
scripts/reports
scripts/doctor
scripts/testing
.github/workflows
```

Checklist:

```text
[ ] Validation scripts exist
[ ] Report scripts exist
[ ] Doctor scripts exist
[ ] Testing scripts exist
[ ] GitHub workflows exist
```

---

# 4. Registry Checklist

Required registries:

```text
registry/skills/skills.registry.yaml
registry/playbooks/playbooks.registry.yaml
registry/patterns/patterns.registry.yaml
registry/templates/templates.registry.yaml
registry/docs/docs.registry.yaml
registry/domains/domains.registry.yaml
registry/tags/tags.registry.yaml
registry/releases/releases.registry.yaml
```

Checklist:

```text
[ ] Skills registry exists
[ ] Playbooks registry exists
[ ] Patterns registry exists
[ ] Templates registry exists
[ ] Docs registry exists
[ ] Domains registry exists
[ ] Tags registry exists
[ ] Releases registry exists
[ ] Registry index exists
```

---

# 5. Local Validation Checklist

Run:

```powershell
.\cli\aegis.ps1 status
.\cli\aegis.ps1 doctor
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
powershell -ExecutionPolicy Bypass -File scripts\reports\generate-all-reports.ps1
```

Checklist:

```text
[ ] Status command passes
[ ] Doctor command passes
[ ] CLI smoke tests pass
[ ] Registry validation passes
[ ] Registry reports generate successfully
```

---

# 6. Git Checklist

Run:

```powershell
git status
git log --oneline -5
```

Checklist:

```text
[ ] Working tree reviewed
[ ] Final v0.5 commit created
[ ] Final v0.5 commit pushed
[ ] GitHub Actions checked
```

---

# 7. Release Decision

If all checklist items are complete:

```text
Aegis OS v0.5 is closed.
```

If any checklist item fails:

```text
Do not close v0.5.
Fix the failing item and rerun validation.
```

---

# 8. Final Declaration

```text
Aegis OS v0.5 can be marked complete when this checklist is fully validated.
```

---

# Final Principle

> A release is not closed because files exist; it is closed because the repository passes its checks.