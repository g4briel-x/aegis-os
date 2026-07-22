## FILE: `registry/_framework/REGISTRY_VALIDATION_MODEL.md`

# Registry Validation Model

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

The Registry Validation Model defines how registry files should be checked for correctness.

---

# 2. Validation Levels

## Level 1 — Structural Validation

Checks:

```text
file exists
YAML is valid
required fields are present
field types are correct
```

---

## Level 2 — Semantic Validation

Checks:

```text
asset type is allowed
status is allowed
maturity is allowed
domain is known
category is meaningful
summary is not empty
```

---

## Level 3 — Repository Validation

Checks:

```text
path exists in repository
referenced related assets exist
duplicate ids do not exist
deprecated assets point to replacement when applicable
```

---

## Level 4 — Governance Validation

Checks:

```text
owner is assigned
review status is accurate
certified assets have review evidence
deprecated assets have reason
release registry is consistent
```

---

# 3. Validation Failure Examples

```text
duplicate asset id
missing path
unknown type
unknown maturity value
related asset not found
certified asset without owner
deprecated asset without replacement
```

---

# 4. Future Automation

The validation model can be implemented as:

```text
Python module
Python CLI command
GitHub Action
Aegis OS runtime validator
```

---

# 5. Final Principle

> A registry that cannot be validated cannot be trusted by automation.
