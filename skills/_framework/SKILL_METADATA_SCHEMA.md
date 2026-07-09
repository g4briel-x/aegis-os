# Aegis OS — Skill Metadata Schema

Version: 0.2  
Status: Skill Standard

---

# 1. Introduction

This document defines the metadata schema for Skills v2.

Metadata allows Skills to be indexed, validated, routed and governed.

---

# 2. Required Metadata

```yaml
skill:
  id:
  name:
  version:
  status:
  domain:
  category:
  maturity:
  owner:
  description:
  inputs:
  outputs:
  dependencies:
  tags:
```

---

# 3. Example

```yaml
skill:
  id: engineering.senior-developer
  name: Senior Developer
  version: 0.2.0
  status: active
  domain: engineering
  category: software-development
  maturity: usable
  owner: aegis-os
  description: Expert software development Skill for producing, reviewing and improving production-grade code.
  inputs:
    - user_request
    - project_context
    - code_context
  outputs:
    - implementation_plan
    - code
    - review_notes
  dependencies:
    - shared.software-engineering.clean-code
    - shared.software-engineering.testing
  tags:
    - coding
    - architecture
    - debugging
```

---

# 4. Final Principle

> Metadata makes Skills machine-readable and ecosystem-ready.