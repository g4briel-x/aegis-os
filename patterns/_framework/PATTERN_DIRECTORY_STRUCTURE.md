## FILE: `patterns/_framework/PATTERN_DIRECTORY_STRUCTURE.md`

# Pattern Directory Structure

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This document defines how Patterns are organized inside Aegis OS.

---

# 2. Root Structure

```text
patterns/
  _framework/
  architecture/
  security/
  product/
  engineering/
  operations/
  business/
  design/
```

---

# 3. Pattern Folder Structure

Each Pattern should use this layout:

```text
patterns/<domain>/<pattern-id>/
  README.md
  PATTERN.md
  metadata.yaml
  context.md
  solution.md
  trade-offs.md
  checklists.md
  examples/
    examples.md
```

---

# 4. Naming Rules

Pattern folder names should:

- use lowercase;
- use hyphen-separated words;
- describe the reusable solution;
- avoid vague names;
- avoid version numbers in folder names.

Good examples:

```text
saas-modular-monolith
rbac-permission-model
api-error-handling
feature-flag-rollout
```

---

# 5. Final Principle

> Pattern structure should make reusable solutions easy to discover and compare.
