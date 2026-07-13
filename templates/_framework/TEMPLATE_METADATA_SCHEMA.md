## FILE: `templates/_framework/TEMPLATE_METADATA_SCHEMA.md`

# Template Metadata Schema

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This document defines the standard `metadata.yaml` schema for Aegis OS Templates.

---

# 2. Required Schema

```yaml
template:
  id: domain.template-id
  name: Template Name
  version: 0.1.0
  status: draft
  domain: product
  category: deliverable
  maturity: experimental
  owner: aegis-os
  description: Short description of the template.
  purpose: What this template helps produce.
  inputs:
    - input_name
  variables:
    - variable_name
  outputs:
    - output_name
  related_skills:
    - domain.skill-id
  related_playbooks:
    - domain.playbook-id
  related_patterns:
    - domain.pattern-id
  tags:
    - tag
```

---

# 3. Status Values

Recommended values:

```text
draft
review
approved
deprecated
```

---

# 4. Maturity Values

Recommended values:

```text
experimental
usable
recommended
standard
deprecated
```

---

# 5. Final Principle

> Template metadata should make reusable deliverables searchable, governable and automation-ready.