## FILE: `install/README.md`

# Aegis OS — Install Scripts

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This folder contains local installation scripts for Aegis OS.

The first installation layer focuses on making the CLI easier to run from PowerShell.

---

# 2. Main Goal

Instead of always typing:

```powershell
.\cli\aegis.ps1 help
```

The user can install a local PowerShell function and type:

```powershell
aegis help
aegis doctor
aegis validate
aegis asset:find security
```

---

# 3. Install Command

Run from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File install\install-aegis-cli.ps1
```

Then restart PowerShell.

---

# 4. Check Command

```powershell
powershell -ExecutionPolicy Bypass -File install\check-aegis-cli.ps1
```

---

# 5. Uninstall Command

```powershell
powershell -ExecutionPolicy Bypass -File install\uninstall-aegis-cli.ps1
```

---

# 6. Final Principle

> Installation should make Aegis OS easier to use without hiding the repository structure.