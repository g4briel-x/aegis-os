## FILE: `cli/CLI_INSTALLATION.md`

# Aegis OS — CLI Installation Guide

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This guide explains how to install the Aegis OS CLI locally in PowerShell.

The goal is to allow the user to run:

```powershell
aegis help
```

instead of:

```powershell
.\cli\aegis.ps1 help
```

---

# 2. Install

Run from the Aegis OS repository root:

```powershell
powershell -ExecutionPolicy Bypass -File install\install-aegis-cli.ps1
```

Then restart PowerShell.

---

# 3. Test

After restarting PowerShell:

```powershell
aegis help
aegis doctor
aegis registry:list
aegis asset:find security
```

---

# 4. Check Installation

```powershell
powershell -ExecutionPolicy Bypass -File install\check-aegis-cli.ps1
```

---

# 5. Uninstall

```powershell
powershell -ExecutionPolicy Bypass -File install\uninstall-aegis-cli.ps1
```

Then restart PowerShell.

---

# 6. How It Works

The installer adds a function to the current user's PowerShell profile:

```powershell
function aegis {
    param(
        [Parameter(ValueFromRemainingArguments = $true)]
        [string[]]$Args
    )

    & "path\to\aegis-os\cli\aegis.ps1" @Args
}
```

This keeps the CLI linked to the local repository.

---

# 7. Important Notes

If the repository is moved to another folder, reinstall the CLI:

```powershell
powershell -ExecutionPolicy Bypass -File install\install-aegis-cli.ps1
```

If PowerShell blocks scripts, run commands using:

```powershell
powershell -ExecutionPolicy Bypass -File <script-path>
```

---

# 8. Final Principle

> A local CLI should be simple to install, simple to remove and transparent in how it works.