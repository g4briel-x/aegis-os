## FILE: `patterns/_framework/PATTERN_VERSIONING.md`

# Pattern Versioning

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This document defines how Pattern versions are managed.

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
MINOR for new sections, examples or compatible improvements
MAJOR for breaking conceptual changes or replacement of the recommended solution
```

---

# 4. Deprecation

A Pattern may be deprecated when:

- a better Pattern replaces it;
- the solution is no longer recommended;
- the context is obsolete;
- the risks are too high.

Deprecation should include:

```text
replacement pattern
reason
migration note
date
owner
```

---

# 5. Final Principle

> Pattern versioning should preserve trust in reusable architectural and operational guidance.
