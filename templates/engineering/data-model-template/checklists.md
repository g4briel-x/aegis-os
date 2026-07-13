## FILE: `templates/engineering/data-model-template/checklists.md`

# Data Model Template — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Completeness Checklist

```text
[ ] Model name is defined
[ ] Business context is clear
[ ] Entities are listed
[ ] Fields are defined
[ ] Relationships are defined
[ ] Tenant boundary is defined
[ ] Ownership rule is defined
[ ] Constraints are listed
[ ] Lifecycle states are defined
[ ] Migration impact is reviewed
```

---

# 2. Data Integrity Checklist

```text
[ ] Required fields are justified
[ ] Foreign keys are reviewed
[ ] Unique constraints are reviewed
[ ] Invalid state transitions are blocked
[ ] Delete behavior is explicit
[ ] Backfill needs are identified
```

---

# 3. Security Checklist

```text
[ ] Tenant isolation is defined
[ ] Cross-tenant access rules are clear
[ ] Sensitive fields are marked
[ ] Permissions are mapped to actions
[ ] Audit events are defined for sensitive actions
[ ] Retention and deletion rules are reviewed
```

---

# 4. Engineering Readiness Checklist

```text
[ ] APIs using the model are listed
[ ] Screens using the model are listed
[ ] Background jobs using the model are listed
[ ] Indexes match expected queries
[ ] Migration plan is defined if needed
[ ] Validation queries are included if needed
```

---

# 5. Final Principle

> Data model checklists should prevent hidden ambiguity from becoming production data risk.
