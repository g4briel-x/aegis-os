# Aegis OS — GitHub Workflows

Version: 0.6.0
Status: Active

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

## Aegis CLI Smoke Tests

```text
.github/workflows/aegis-cli-smoke-tests.yml
```

Runs the PowerShell CLI smoke tests, registry validation, and report generation
on Windows.

## Aegis Python Runtime Tests

```text
.github/workflows/aegis-runtime-tests.yml
```

Installs the Python 3.11 runtime, runs the unit test suite, and exercises the
registry, asset, and validation commands that protect the main runtime path.

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
