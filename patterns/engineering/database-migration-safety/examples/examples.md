## FILE: `patterns/engineering/database-migration-safety/examples/examples.md`

# Database Migration Safety — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Add Readiness Score to Projects

## Context

An audiovisual financing SaaS needs to add a `readiness_score` field to projects.

## Safe Approach

```text
add nullable readiness_score column
deploy application that can handle null score
backfill scores in batches
validate all submitted projects have score
start reading score in UI
later make field required if justified
```

## Validation

```sql
SELECT COUNT(*) FROM projects
WHERE status = 'submitted'
AND readiness_score IS NULL;
```

---

# 2. Example — Rename Column Safely

## Unsafe Approach

```text
rename project_status to status and deploy code at the same time
```

## Safer Approach

```text
add new status column
dual-write project_status and status
backfill status
read from status after validation
stop writing project_status
drop project_status in later release
```

---

# 3. Example — Tenant Data Correction

## Context

A workspace has incorrect project ownership metadata.

## Safety Rules

```text
limit update by workspace_id
preview affected rows
take backup or export affected rows
run update
validate affected rows
audit correction if needed
```

## Safer Query Shape

```sql
UPDATE projects
SET owner_id = :new_owner_id
WHERE workspace_id = :workspace_id
AND id IN (:project_ids);
```

---

# 4. Example — Add Unique Constraint

## Steps

```text
check duplicates
resolve duplicate records
add unique index safely
validate application behavior
add constraint if needed
```

## Duplicate Check

```sql
SELECT workspace_id, slug, COUNT(*)
FROM projects
GROUP BY workspace_id, slug
HAVING COUNT(*) > 1;
```

---

# 5. Final Principle

> Examples show that safe migrations split risk into small, verifiable and recoverable steps.
