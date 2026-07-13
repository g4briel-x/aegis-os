## FILE: `.github/workflows/CLI_SMOKE_TEST_WORKFLOW.md`

# Aegis OS — CLI Smoke Test Workflow

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This workflow runs Aegis OS CLI smoke tests automatically in GitHub Actions.

It ensures that the CLI command layer remains usable after changes to:

```text
cli/aegis.ps1
cli/commands
registry files
scripts/testing
scripts/validation
scripts/reports
```

---

# 2. Workflow File

```text
.github/workflows/aegis-cli-smoke-tests.yml
```

---

# 3. Trigger Events

The workflow runs on:

```text
push to main
pull request to main
manual workflow dispatch
```

---

# 4. What It Checks

The workflow checks:

```text
CLI entrypoint exists
CLI smoke test entrypoint exists
CLI smoke tests pass
registry validation passes
registry reports can be generated
```

---

# 5. Failure Meaning

## Missing CLI Entrypoint

Meaning:

```text
cli/aegis.ps1 is missing or was renamed without updating the workflow.
```

Fix:

```text
Restore cli/aegis.ps1 or update the workflow path.
```

## Smoke Test Failure

Meaning:

```text
One or more CLI commands failed.
```

Fix:

```text
Run scripts\testing\test-cli-smoke.ps1 locally and inspect the failing command.
```

## Registry Validation Failure

Meaning:

```text
Registry metadata has missing paths, duplicate ids or invalid related assets.
```

Fix:

```text
Run scripts\validation\validate-all.ps1 locally and fix the reported registry issue.
```

---

# 6. Local Equivalent

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
powershell -ExecutionPolicy Bypass -File scripts\reports\generate-all-reports.ps1
```

---

# 7. Final Principle

> A CLI should not be considered reliable until its command wiring is tested automatically.