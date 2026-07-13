## FILE: `scripts/validation/VALIDATION_GUIDE.md`

# Aegis OS — Validation Guide

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This guide explains how to run and interpret Aegis OS validation checks.

Validation ensures that the repository remains structured, traceable and ready for future CLI, runtime, marketplace and automation layers.

---

# 2. Main Command

Run from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
```

---

# 3. Individual Validation Commands

## YAML Validation

```powershell
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-yaml.ps1
```

Role:

```text
Checks registry YAML files for parse readiness and empty-file issues.
```

---

## Path Validation

```powershell
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-paths.ps1
```

Role:

```text
Checks that every path referenced in registry files exists in the repository.
```

---

## ID Validation

```powershell
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-ids.ps1
```

Role:

```text
Checks that registry ids are not duplicated.
```

---

## Related Assets Validation

```powershell
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-related-assets.ps1
```

Role:

```text
Checks that related asset references point to known registry ids.
```

---

# 4. GitHub Actions Validation

The workflow file is:

```text
.github/workflows/aegis-validation.yml
```

It runs automatically on:

```text
push to main
pull request to main
manual workflow dispatch
```

---

# 5. Failure Meaning

## Missing Path

Meaning:

```text
A registry entry points to a file or folder that does not exist.
```

Typical fix:

```text
Correct the path or create the missing asset.
```

---

## Duplicate ID

Meaning:

```text
Two registry entries use the same id.
```

Typical fix:

```text
Rename one id so every asset has a unique identifier.
```

---

## Unknown Related Asset

Meaning:

```text
A related_assets entry points to an id that is not declared in any registry.
```

Typical fix:

```text
Add the missing registry entry or correct the relationship id.
```

---

# 6. Recommended Workflow

Before committing registry changes:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
git status
git add .
git commit -m "..."
git push
```

---

# 7. Final Principle

> Validation converts Aegis OS from manually organized files into a repository that can be trusted by tools.