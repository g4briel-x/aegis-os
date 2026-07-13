## FILE: `scripts/doctor/README.md`

# Aegis OS — Doctor Scripts

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

Doctor scripts perform a quick health check of the Aegis OS repository.

They are designed to answer:

```text
Is the repository structure present?
Are required indexes present?
Are registry folders present?
Are validation scripts present?
Is Git available?
Is the working tree clean?
Can validation and report scripts run?
```

---

# 2. Main Command

Run from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\doctor\aegis-doctor.ps1
```

---

# 3. Difference Between Doctor and Validation

```text
Validation checks registry correctness.
Doctor checks repository health.
Reports generate human-readable summaries.
```

---

# 4. Final Principle

> Doctor scripts should quickly identify what is missing before deeper automation fails.
