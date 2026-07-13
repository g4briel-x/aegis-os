## FILE: `cli/CLI_METADATA_COMMANDS.md`

# Aegis OS — CLI Metadata Commands

Version: 0.1.0  
Status: Draft  
Domain: CLI  
Category: Metadata Commands

---

# 1. Purpose

This document defines basic CLI commands for showing Aegis OS metadata and repository status.

---

# 2. Commands

```powershell
.\cli\aegis.ps1 version
.\cli\aegis.ps1 info
.\cli\aegis.ps1 status
```

---

# 3. Command Roles

## `version`

```text
Shows the current Aegis OS CLI version.
```

## `info`

```text
Shows project identity, repository folders and core entrypoints.
```

## `status`

```text
Runs a lightweight repository status check without executing the full doctor workflow.
```

---

# 4. Difference Between `status` and `doctor`

```text
status = quick overview
doctor = deeper health check + validation + reports
```

---

# 5. Final Principle

> Metadata commands help users understand the local Aegis OS repository before running heavier automation.