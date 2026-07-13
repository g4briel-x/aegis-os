## FILE: `cli/COMMANDS.md`

# Aegis OS — CLI Commands Reference

Version: 0.1.0  
Status: Draft  
Domain: CLI  
Category: Command Reference

---

# 1. Purpose

This file is the human-readable reference for all Aegis OS CLI commands.

The CLI entrypoint is:

```powershell
.\cli\aegis.ps1
```

---

# 2. Core Commands

## `help`

Role:

```text
Displays all available CLI commands and usage examples.
```

Command:

```powershell
.\cli\aegis.ps1 help
```

---

## `validate`

Role:

```text
Runs validation checks for YAML registries, paths, ids and related asset references.
```

Command:

```powershell
.\cli\aegis.ps1 validate
```

---

## `doctor`

Role:

```text
Runs repository health checks, validation scripts and report generation.
```

Command:

```powershell
.\cli\aegis.ps1 doctor
```

---

## `report`

Role:

```text
Generates human-readable registry reports.
```

Command:

```powershell
.\cli\aegis.ps1 report
```

---

# 3. Registry Listing Commands

## `registry:list`

Role:

```text
Lists all registry YAML files.
```

Command:

```powershell
.\cli\aegis.ps1 registry:list
```

---

## `skill:list`

Role:

```text
Lists all registered skills.
```

Command:

```powershell
.\cli\aegis.ps1 skill:list
```

---

## `playbook:list`

Role:

```text
Lists all registered playbooks.
```

Command:

```powershell
.\cli\aegis.ps1 playbook:list
```

---

## `pattern:list`

Role:

```text
Lists all registered patterns.
```

Command:

```powershell
.\cli\aegis.ps1 pattern:list
```

---

## `template:list`

Role:

```text
Lists all registered templates.
```

Command:

```powershell
.\cli\aegis.ps1 template:list
```

---

## `domain:list`

Role:

```text
Lists all registered domains.
```

Command:

```powershell
.\cli\aegis.ps1 domain:list
```

---

## `tag:list`

Role:

```text
Lists all registered tags.
```

Command:

```powershell
.\cli\aegis.ps1 tag:list
```

---

## `docs:list`

Role:

```text
Lists all registered documentation sections.
```

Command:

```powershell
.\cli\aegis.ps1 docs:list
```

---

## `release:status`

Role:

```text
Displays release versions, statuses and maturity levels.
```

Command:

```powershell
.\cli\aegis.ps1 release:status
```

---

# 4. Asset Inspection Commands

## `asset:find`

Role:

```text
Searches registry files by keyword.
```

Command:

```powershell
.\cli\aegis.ps1 asset:find security
```

---

## `asset:show`

Role:

```text
Displays the registry metadata block for one asset id.
```

Command:

```powershell
.\cli\aegis.ps1 asset:show engineering.senior-developer
```

---

## `asset:related`

Role:

```text
Displays related assets declared for one asset.
```

Command:

```powershell
.\cli\aegis.ps1 asset:related security.security-review-template
```

---

## `asset:path`

Role:

```text
Displays the repository path of one asset.
```

Command:

```powershell
.\cli\aegis.ps1 asset:path business.pricing-strategy-template
```

---

## `asset:open`

Role:

```text
Opens the repository path of one asset in the local file explorer.
```

Command:

```powershell
.\cli\aegis.ps1 asset:open design.ux-flow-template
```

---

## `domain:assets`

Role:

```text
Lists assets that belong to a specific domain.
```

Command:

```powershell
.\cli\aegis.ps1 domain:assets security
```

---

## `tag:assets`

Role:

```text
Lists assets that use a specific tag.
```

Command:

```powershell
.\cli\aegis.ps1 tag:assets api
```

---

# 5. Recommended Daily Workflow

```powershell
.\cli\aegis.ps1 doctor
git status
git add .
git commit -m "..."
git push
```

---

# 6. Final Principle

> The command reference keeps the CLI understandable as Aegis OS grows.