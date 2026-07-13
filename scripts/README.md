## FILE: `scripts/README.md`

# Aegis OS — Scripts

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This folder contains automation and validation scripts for Aegis OS.

The first script layer focuses on registry validation.

---

# 2. Script Categories

```text
scripts/validation
```

Purpose:

```text
Validates machine-readable registry files, asset paths, ids, duplicate entries and relationships.
```

---

# 3. Recommended Execution

Run from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
```

---

# 4. Final Principle

> Scripts should make Aegis OS easier to verify before future automation, CLI and runtime layers are added.
