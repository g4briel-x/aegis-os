## FILE: `cli/CLI_USAGE.md`

# Aegis OS — CLI Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Main Command

Run from the repository root:

```powershell
.\cli\aegis.ps1 help
```

---

# 2. Available Commands

```powershell
.\cli\aegis.ps1 help
.\cli\aegis.ps1 validate
.\cli\aegis.ps1 doctor
.\cli\aegis.ps1 report
.\cli\aegis.ps1 registry:list
.\cli\aegis.ps1 asset:find security
```

---

# 3. Command Roles

## `help`

```text
Shows available CLI commands.
```

## `validate`

```text
Runs Aegis OS validation checks.
```

## `doctor`

```text
Runs repository health checks, validation and report generation.
```

## `report`

```text
Generates human-readable registry reports.
```

## `registry:list`

```text
Lists available registry YAML files.
```

## `asset:find`

```text
Searches registry files for a keyword such as security, api, pricing or ux.
```

---

# 4. Recommended Local Workflow

```powershell
.\cli\aegis.ps1 doctor
git status
git add .
git commit -m "..."
git push
```

---

# 5. Final Principle

> A CLI should reduce repeated manual commands without hiding what it does.
