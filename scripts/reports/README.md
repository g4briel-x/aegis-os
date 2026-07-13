## FILE: `scripts/reports/README.md`

# Aegis OS — Report Scripts

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This folder contains scripts that generate human-readable reports from machine-readable registry files.

---

# 2. Main Command

Run from repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\reports\generate-all-reports.ps1
```

---

# 3. Generated Outputs

```text
reports/registry/REGISTRY_SUMMARY.md
reports/registry/ASSET_MAP.md
reports/registry/DOMAIN_REPORT.md
reports/registry/RELEASE_REPORT.md
```

---

# 4. Final Principle

> Registry reports make Aegis OS easier to inspect before deeper automation is introduced.
