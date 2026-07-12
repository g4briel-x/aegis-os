## FILE: `patterns/engineering/database-migration-safety/PATTERN.md`

# Database Migration Safety Pattern

Version: 0.1.0  
Status: Draft

---

# 1. Problem

A SaaS product evolves its database over time.

Changes may include:

- adding columns;
- renaming columns;
- dropping columns;
- adding indexes;
- changing constraints;
- migrating tenant data;
- backfilling computed values;
- splitting tables;
- changing relationships;
- updating seed or reference data.

A poorly planned migration can cause downtime, data loss, broken deployments or tenant data exposure.

---

# 2. Context

This Pattern applies when database changes affect:

```text
production schema
customer data
tenant-scoped records
large tables
critical workflows
billing data
permissions
audit logs
background jobs
reporting
```

It is especially important for SaaS applications with real customers and shared multi-tenant databases.

---

# 3. Forces

Key forces:

```text
speed versus data safety
schema evolution versus backward compatibility
deployment simplicity versus rollback complexity
data correction versus auditability
large table changes versus uptime
strict constraints versus existing dirty data
```

---

# 4. Recommended Model

Use a migration safety model:

```text
Migration Intent
Risk Level
Schema Change
Data Change
Compatibility Strategy
Execution Plan
Rollback or Recovery Plan
Validation Plan
Monitoring Plan
Approval
```

Each migration should be reviewed against this model before production deployment.

---

# 5. Migration Types

Classify migration type before execution.

Common types:

```text
additive_schema_change
destructive_schema_change
data_backfill
index_change
constraint_change
table_split
table_merge
tenant_data_correction
permission_data_change
billing_data_change
```

Additive changes are usually safer. Destructive and data migrations require stronger controls.

---

# 6. Expand and Contract Strategy

For risky schema changes, use the expand-and-contract approach.

Example sequence:

```text
1. Add new nullable column
2. Deploy application code that writes both old and new fields
3. Backfill existing rows
4. Read from new field after validation
5. Stop writing old field
6. Drop old field in a later release
```

This avoids breaking older application versions during deployment.

---

# 7. Data Backfill Strategy

Backfills should be:

```text
batched
idempotent
observable
interruptible
tenant-aware
validated
restartable
```

Avoid large unbounded updates in one transaction on production tables.

---

# 8. Validation

Every migration should include validation before and after execution.

Examples:

```text
row counts
null checks
foreign key consistency
tenant boundary checks
duplicate checks
sample record verification
application health checks
critical workflow checks
```

---

# 9. Rollback and Recovery

Not every migration can be truly rolled back.

Define one of:

```text
rollback migration
forward fix
restore from backup
manual recovery procedure
feature flag disablement
application rollback plus schema compatibility
```

For destructive migrations, backup and recovery planning is mandatory.

---

# 10. Final Principle

> Database migration safety depends on compatibility, validation and recovery more than on the migration file itself.
