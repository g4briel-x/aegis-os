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
