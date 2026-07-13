## FILE: `registry/_framework/REGISTRY_METADATA_SCHEMA.md`

# Registry Metadata Schema

Version: 0.1.0  
Status: Draft

---

# 1. Core Entry Schema

```yaml
id: string
name: string
type: string
domain: string
category: string
status: string
maturity: string
version: string
path: string
owner: string
summary: string
tags:
  - string
related_assets:
  - id: string
    relationship: string
```

---

# 2. Field Definitions

## `id`

Unique identifier.

Example:

```yaml
id: engineering.senior-developer
```

---

## `type`

Asset type.

Example:

```yaml
type: skill
```

---

## `domain`

Functional domain.

Example:

```yaml
domain: engineering
```

---

## `path`

Repository path.

Example:

```yaml
path: skills/engineering/senior-developer
```

---

## `related_assets`

Relationship list.

Example:

```yaml
related_assets:
  - id: engineering.implement-feature-from-prd
    relationship: supports
  - id: engineering.api-contract-template
    relationship: uses
```

---

# 3. Optional Fields

```yaml
inputs:
  - string

outputs:
  - string

quality_gates:
  - string

requires:
  - string

generates:
  - string

deprecated_by: string
```

---

# 4. Validation Rules

```text
id must be unique
path must exist
type must be allowed
status must be allowed
maturity must be allowed
related assets should exist
version must follow semantic versioning when applicable
```

---

# 5. Final Principle

> Metadata should be strict enough for automation and clear enough for maintainers.
