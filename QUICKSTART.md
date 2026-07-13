## FILE: `QUICKSTART.md`

# Aegis OS — Quickstart

Version: 0.5.0  
Status: Ready for Local Use

---

# 1. Open Repository

From PowerShell:

```powershell
cd "C:\Users\SE Pictures\Desktop\aegis-os"
```

---

# 2. Check Project Status

```powershell
.\cli\aegis.ps1 status
```

---

# 3. Show Available Commands

```powershell
.\cli\aegis.ps1 help
```

---

# 4. Run Full Doctor

```powershell
.\cli\aegis.ps1 doctor
```

The doctor checks:

```text
repository structure
required indexes
Git status
registry validation
report generation
```

---

# 5. Run Tests

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
```

---

# 6. Validate Registries

```powershell
.\cli\aegis.ps1 validate
```

---

# 7. Generate Reports

```powershell
.\cli\aegis.ps1 report
```

Generated reports should appear under:

```text
reports/registry/
```

---

# 8. Find Assets

Search by keyword:

```powershell
.\cli\aegis.ps1 asset:find security
```

Show one asset:

```powershell
.\cli\aegis.ps1 asset:show engineering.senior-developer
```

Show asset path:

```powershell
.\cli\aegis.ps1 asset:path business.pricing-strategy-template
```

---

# 9. Install CLI Alias

```powershell
powershell -ExecutionPolicy Bypass -File install\install-aegis-cli.ps1
```

Restart PowerShell.

Then run:

```powershell
aegis help
aegis doctor
aegis status
```

---

# 10. Commit Routine

```powershell
git status
git add .
git commit -m "docs: update aegis os foundation"
git push
```

---

# Final Principle

> Start with status, run doctor, validate, test, then commit.
