## FILE: `patterns/engineering/database-migration-safety/checklists.md`

# Database Migration Safety — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Context Fit Checklist

```text
[ ] Production database is affected
[ ] Customer data is affected
[ ] Schema changes are included
[ ] Data changes are included
[ ] Critical workflow may be affected
[ ] Rollback or recovery is needed
```

---

# 2. Migration Design Checklist

```text
[ ] Migration purpose is clear
[ ] Tables affected are listed
[ ] Data affected is listed
[ ] Risk level is assigned
[ ] Compatibility strategy is defined
[ ] Deployment order is defined
[ ] Owner is assigned
```

---

# 3. Safety Checklist

```text
[ ] Destructive changes are delayed or justified
[ ] Backup requirement is reviewed
[ ] Lock risk is reviewed
[ ] Large updates are batched
[ ] Tenant filters are included where needed
[ ] Secrets or sensitive data are not exposed
[ ] Approval is recorded
```

---

# 4. Validation Checklist

```text
[ ] Pre-migration validation queries exist
[ ] Post-migration validation queries exist
[ ] Row count checks exist
[ ] Constraint checks exist
[ ] Tenant boundary checks exist
[ ] Critical workflow check exists
[ ] Monitoring signals are defined
```

---

# 5. Rollback and Recovery Checklist

```text
[ ] Rollback type is defined
[ ] Recovery path is defined
[ ] Backup exists if needed
[ ] Feature flag fallback exists if relevant
[ ] Application rollback compatibility is reviewed
[ ] Manual recovery owner is assigned
```

---

# 6. Cleanup Checklist

```text
[ ] Temporary compatibility code tracked
[ ] Old columns scheduled for removal later
[ ] Dual-write logic cleanup planned
[ ] Documentation update planned
[ ] Data model update planned
[ ] Follow-up task created
```

---

# 7. Final Principle

> Migration checklists exist to protect data when release pressure is high.
