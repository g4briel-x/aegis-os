## FILE: `playbooks/engineering/design-saas-data-model/outputs.md`

# Design SaaS Data Model — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. Entity List

Purpose:

Define the core data objects.

Required sections:

```text
Entity:
Purpose:
Owner:
Lifecycle:
Sensitivity:
```

---

# 2. Relationship Map

Purpose:

Clarify how entities connect.

Required sections:

```text
Source entity:
Target entity:
Relationship type:
Foreign key:
Constraint:
Notes:
```

---

# 3. Tenant Model

Purpose:

Define data isolation boundaries.

Required sections:

```text
Tenant entity:
Scoped entities:
Global entities:
Access rule:
Cross-tenant restriction:
```

---

# 4. Field Definitions

Purpose:

Prepare implementation-ready schema details.

Required sections:

```text
Entity:
Field:
Type:
Required:
Default:
Constraint:
Validation:
```

---

# 5. Lifecycle State Model

Purpose:

Define allowed data state transitions.

Required sections:

```text
Entity:
State:
Allowed transition:
Actor:
Timestamp:
Audit need:
```

---

# 6. Index Candidate List

Purpose:

Prepare performance-aware schema design.

Required sections:

```text
Table:
Columns:
Query supported:
Expected benefit:
Write overhead:
Priority:
```

---

# 7. Migration Plan

Purpose:

Plan safe implementation of schema changes.

Required sections:

```text
Migration:
Order:
Risk:
Rollback:
Validation:
Owner:
```

---

# 8. Open Data Questions

Purpose:

Track unresolved data model decisions.

Required sections:

```text
Question:
Impact:
Owner:
Decision needed by:
Status:
```

---

# 9. Final Principle

> Data model outputs must be clear enough for schema implementation, API design and security review.
