## FILE: `cli/commands/README.md`

# Aegis OS — CLI Commands

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This folder contains PowerShell command wrappers used by `cli/aegis.ps1`.

---

# 2. Commands

```text
help.ps1
validate.ps1
doctor.ps1
report.ps1
registry-list.ps1
asset-find.ps1
```

---

# 3. Rule

Command scripts should be thin wrappers.

Business logic should remain in:

```text
scripts/validation
scripts/reports
scripts/doctor
registry
```

---

# 4. Final Principle

> CLI commands should orchestrate existing scripts instead of duplicating their logic.
