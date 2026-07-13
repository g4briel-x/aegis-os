## FILE: `reports/README.md`

# Aegis OS — Reports

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This folder contains generated reports produced from Aegis OS registries.

Reports are human-readable summaries of machine-readable registry data.

---

# 2. Generated Report Types

```text
reports/registry/REGISTRY_SUMMARY.md
reports/registry/ASSET_MAP.md
reports/registry/DOMAIN_REPORT.md
reports/registry/RELEASE_REPORT.md
```

---

# 3. Rule

Reports should not replace registries.

```text
registry/*.yaml = source of truth for systems
reports/*.md = generated view for humans
```

---

# 4. Final Principle

> Reports make registry information easier to audit, review and communicate.
