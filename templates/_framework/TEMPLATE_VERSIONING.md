## FILE: `templates/_framework/TEMPLATE_VERSIONING.md`

# Template Versioning

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This document defines how Template versions are managed.

---

# 2. Version Format

Use semantic versioning:

```text
MAJOR.MINOR.PATCH
```

Example:

```text
0.1.0
```

---

# 3. Version Rules

Use:

```text
PATCH for typo, formatting or small clarification
MINOR for new optional sections, variables or examples
MAJOR for required section changes, incompatible variable changes or output structure redesign
```

---

# 4. Deprecation

A Template may be deprecated when:

- a better Template replaces it;
- the output format is obsolete;
- the domain process changes;
- the Template creates poor outputs.

Deprecation should include:

```text
replacement template
reason
migration note
date
owner
```

---

# 5. Final Principle

> Template versioning should preserve trust in reusable output formats.
