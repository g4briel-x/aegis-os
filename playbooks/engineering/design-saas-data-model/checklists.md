## FILE: `playbooks/engineering/design-saas-data-model/checklists.md`

# Design SaaS Data Model — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. Entity Checklist

```text
[ ] Core business entities identified
[ ] Entity purpose defined
[ ] Entity owner defined
[ ] Entity lifecycle considered
[ ] Entity relationships mapped
[ ] Entity permissions considered
[ ] Entity reporting needs considered
```

---

# 2. Relationship Checklist

```text
[ ] Relationship type defined
[ ] Foreign keys identified
[ ] Many-to-many relationships reviewed
[ ] Ownership relationships defined
[ ] Cascade behavior considered
[ ] Orphan record risk considered
[ ] Relationship constraints documented
```

---

# 3. Tenant and Permission Checklist

```text
[ ] Tenant or workspace boundary defined
[ ] User ownership defined
[ ] Admin access reviewed
[ ] Cross-tenant access blocked
[ ] Object-level authorization considered
[ ] Sensitive data access reviewed
[ ] Audit needs identified
```

---

# 4. Field and Constraint Checklist

```text
[ ] Field names defined
[ ] Data types selected
[ ] Required fields marked
[ ] Optional fields justified
[ ] Unique constraints reviewed
[ ] Defaults defined
[ ] Validation rules documented
[ ] Index candidates identified
```

---

# 5. Migration Checklist

```text
[ ] Migration order defined
[ ] Backfill needs reviewed
[ ] Rollback constraints documented
[ ] Seed data needs identified
[ ] Validation queries defined
[ ] Production risk reviewed
[ ] Database review requested if needed
```

---

# 6. Final Principle

> Data model checklists protect the system from unclear ownership, weak constraints and unsafe schema changes.