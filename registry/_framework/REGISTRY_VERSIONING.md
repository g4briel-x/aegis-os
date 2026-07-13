## FILE: `registry/_framework/REGISTRY_VERSIONING.md`

# Registry Versioning

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

Registry versioning defines how registry structure and registry entries evolve over time.

---

# 2. Registry Schema Version

Each registry file should include:

```yaml
schema_version: 0.1.0
```

---

# 3. Registry Entry Version

Each asset entry should include:

```yaml
version: 0.1.0
```

---

# 4. Change Types

```text
patch: fix typo, summary or metadata
minor: add new fields or entries without breaking compatibility
major: change schema rules or required fields
```

---

# 5. Deprecation Rule

Deprecated entries should include:

```yaml
status: deprecated
deprecated_reason: string
deprecated_by: string
```

---

# 6. Compatibility Rule

Registry changes should not break automation without a version change.

---

# 7. Final Principle

> Registry versioning protects automation from silent metadata changes.
