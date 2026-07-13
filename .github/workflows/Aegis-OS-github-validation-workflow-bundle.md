# Aegis OS — GitHub Validation Workflow Bundle

Ce fichier regroupe les documents pour automatiser la validation Aegis OS dans GitHub Actions :

- `.github/workflows/README.md`
- `.github/workflows/aegis-validation.yml`
- `scripts/validation/VALIDATION_GUIDE.md`

---

## FILE: `.github/workflows/README.md`

# Aegis OS — GitHub Workflows

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This folder contains GitHub Actions workflows for Aegis OS.

The first workflow runs validation checks against the repository registry layer and automation scripts.

---

# 2. Workflows

## Aegis Validation

```text
.github/workflows/aegis-validation.yml
```

Role:

```text
Runs Aegis OS validation checks automatically when changes are pushed or pull requests are opened.
```

It validates:

```text
registry files
registry paths
duplicate ids
related asset references
PowerShell validation scripts
```

---

# 3. Execution Context

The workflow is designed to run on:

```text
push
pull_request
manual dispatch
```

---

# 4. Final Principle

> Validation should run before broken metadata reaches the main branch.

---

## FILE: `.github/workflows/aegis-validation.yml`

```yaml
name: Aegis OS Validation

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

jobs:
  validate:
    name: Validate Aegis OS Repository
    runs-on: windows-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Show PowerShell version
        shell: pwsh
        run: |
          $PSVersionTable

      - name: Validate repository structure
        shell: pwsh
        run: |
          if (-not (Test-Path "registry")) {
            throw "Missing registry directory."
          }

          if (-not (Test-Path "scripts\validation")) {
            throw "Missing scripts\validation directory."
          }

          if (-not (Test-Path "scripts\validation\validate-all.ps1")) {
            throw "Missing validate-all.ps1."
          }

          Write-Host "Repository structure validation passed."

      - name: Run Aegis validation scripts
        shell: pwsh
        run: |
          powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1

      - name: Validation summary
        shell: pwsh
        run: |
          Write-Host "Aegis OS validation completed successfully."
```

---

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
