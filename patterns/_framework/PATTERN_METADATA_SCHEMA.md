## FILE: `patterns/_framework/PATTERN_METADATA_SCHEMA.md`

# Pattern Metadata Schema

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This document defines the standard `metadata.yaml` schema for Aegis OS Patterns.

---

# 2. Required Schema

```yaml
pattern:
  id: domain.pattern-id
  name: Pattern Name
  version: 0.1.0
  status: draft
  domain: architecture
  category: reusable-solution
  maturity: experimental
  owner: aegis-os
  description: Short description of the pattern.
  problem: Problem this pattern solves.
  context:
    - context_condition
  recommended_when:
    - condition
  avoid_when:
    - condition
  outputs:
    - output_name
  related_skills:
    - domain.skill-id
  related_playbooks:
    - domain.playbook-id
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

> Pattern metadata should make the pattern searchable, governable and reviewable.
