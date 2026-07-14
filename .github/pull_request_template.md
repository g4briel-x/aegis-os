## FILE: `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
# Pull Request

## Summary

Describe what this pull request changes.

## Change Type

Select one:

```text
docs
feat
fix
test
ci
chore
refactor
security
```

## Affected Areas

Select all that apply:

```text
[ ] docs
[ ] skills
[ ] playbooks
[ ] patterns
[ ] templates
[ ] registry
[ ] scripts
[ ] cli
[ ] config
[ ] reports
[ ] github-actions
[ ] root files
```

## Role of the Change

Explain the role of the new or modified files.

```text

```

## Validation

Commands run:

```powershell
.\cli\aegis.ps1 status
.\cli\aegis.ps1 doctor
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
powershell -ExecutionPolicy Bypass -File scripts\reports\generate-all-reports.ps1
```

## Checklist

```text
[ ] Files are in the correct folders
[ ] File roles are documented
[ ] Registry updated if needed
[ ] CLI command map updated if needed
[ ] Smoke tests updated if needed
[ ] Validation passes
[ ] Reports generate successfully
[ ] Documentation updated
```

## Notes

```text
Optional.
```
```

---

## Final Principle

> Standard GitHub files make Aegis OS easier to review, contribute to, secure and maintain.