## FILE: `scripts/testing/CI_TESTING_GUIDE.md`

# Aegis OS — CI Testing Guide

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This guide explains how Aegis OS testing is expected to run locally and in continuous integration.

---

# 2. CI Test Layers

```text
CLI smoke tests
registry validation
report generation
GitHub Actions workflow checks
```

---

# 3. Local Test Commands

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
powershell -ExecutionPolicy Bypass -File scripts\reports\generate-all-reports.ps1
```

---

# 4. GitHub Actions Workflows

```text
.github/workflows/aegis-validation.yml
.github/workflows/aegis-cli-smoke-tests.yml
```

---

# 5. Recommended Pre-Push Routine

```powershell
.\cli\aegis.ps1 doctor
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
git status
git add .
git commit -m "..."
git push
```

---

# 6. CI Failure Policy

A CI failure should block merging when:

```text
CLI command routing fails
registry validation fails
required repository files are missing
asset paths are invalid
duplicate ids exist
related assets are unknown
report generation fails
```

---

# 7. Final Principle

> CI should protect the repository from silent structural breakage.