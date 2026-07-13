## FILE: `templates/_framework/TEMPLATE_DIRECTORY_STRUCTURE.md`

# Template Directory Structure

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This document defines how Templates are organized inside Aegis OS.

---

# 2. Root Structure

```text
templates/
  _framework/
  product/
  engineering/
  security/
  operations/
  business/
  design/
  management/
  architecture/
```

---

# 3. Template Folder Structure

Each Template should use this layout:

```text
templates/<domain>/<template-id>/
  README.md
  TEMPLATE.md
  metadata.yaml
  variables.md
  usage.md
  checklists.md
  examples/
    examples.md
```

---

# 4. Naming Rules

Template folder names should:

- use lowercase;
- use hyphen-separated words;
- describe the output;
- avoid vague names;
- avoid version numbers in folder names.

Good examples:

```text
prd-template
api-contract-template
postmortem-template
incident-report-template
test-plan-template
```

Bad examples:

```text
template1
new-doc
final-template-v2
misc
```

---

# 5. Final Principle

> Template structure should make reusable outputs easy to find, fill and review.
