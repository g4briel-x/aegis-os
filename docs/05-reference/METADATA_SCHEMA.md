# Aegis OS — Metadata Schema

Version: 0.1  
Status: Reference Document

---

# 1. Introduction

Metadata defines the descriptive information attached to every Aegis OS component.

Metadata allows the system to:

- identify components;
- manage versions;
- resolve dependencies;
- automate validation;
- support orchestration.

---

# 2. Metadata Philosophy

Aegis OS follows this principle:

> Every intelligent component must describe itself before being executed.

A component without metadata cannot be reliably managed.

---

# 3. General Metadata Structure

All components should contain:

```yaml
metadata:

  identity:

  version:

  classification:

  ownership:

  dependencies:

  lifecycle:

  validation:

  4. Identity Section

Defines component identification.

Example:

identity:
  name: software-architect
  type: skill
  id: skill.engineering.software_architect

Fields:

name

Human-readable name.

type

Component category.

Allowed values:

skill
playbook
pattern
template
agent
workflow
tool
id

Unique machine identifier.

5. Version Section

Defines component version.

Example:

version:
  current: 1.0.0
  schema: 0.1

Fields:

current

Current component version.

schema

Metadata format version.

6. Classification Section

Defines component organization.

Example:

classification:
  category: engineering
  domain: software-development
  maturity: stable
category

Main ecosystem area.

Examples:

engineering
product
design
infrastructure
management
domain

Specific expertise area.

maturity

Lifecycle stage.

Values:

draft
experimental
beta
stable
certified


7. Ownership Section

Defines responsibility.

Example:

ownership:
  maintainer: aegis-team
  contributors:
    - community


8. Dependencies Section

Defines required components.

Example:

dependencies:

  skills:
    - software-engineer

  tools:
    - git

  patterns:
    - clean-architecture


9. Lifecycle Section

Defines evolution state.

Example:

lifecycle:
  status: active
  created: 2026-01-01
  updated: 2026-07-07

Allowed statuses:

active
deprecated
archived


10. Validation Section

Defines quality information.

Example:

validation:

  reviewed: true

  quality_score:
    accuracy: 95
    completeness: 90

11. Complete Skill Example
metadata:

  identity:
    name: software-architect
    type: skill
    id: skill.engineering.software_architect

  version:
    current: 1.0.0
    schema: 0.1

  classification:
    category: engineering
    domain: architecture
    maturity: stable

  ownership:
    maintainer: aegis-team

  dependencies:
    patterns:
      - clean-architecture

  lifecycle:
    status: active

  validation:
    reviewed: true


12. Metadata Validation Rules

Required fields:

[ ] identity
[ ] version
[ ] classification
[ ] lifecycle

Optional but recommended:

[ ] dependencies
[ ] validation
[ ] ownership

13. Metadata Evolution
Schema changes follow versioning:

0.1

 ↓

0.2

 ↓

1.0

Breaking changes require migration.

14. Automation Usage
Metadata enables:
- automatic discovery;
- dependency resolution;
- validation pipelines;
- component indexing.

15. Final Principle
Metadata is the identity layer that allows Aegis OS to understand, organize and operate its intelligence components.