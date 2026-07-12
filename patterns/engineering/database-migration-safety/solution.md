## FILE: `patterns/engineering/database-migration-safety/solution.md`

# Database Migration Safety — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Solution Overview

Use a disciplined migration lifecycle:

```text
1. Classify migration
2. Assess risk
3. Design compatibility strategy
4. Write migration
5. Test on realistic data
6. Define validation queries
7. Define rollback or recovery
8. Deploy with monitoring
9. Validate after deployment
10. Clean up later if needed
```

---

# 2. Risk Classification

Classify risk as:

```text
low
medium
high
critical
```

Low risk:

```text
add nullable column
add small lookup table
add non-critical index safely
```

High risk:

```text
drop column
rewrite large table
change permission data
change billing records
rename critical column
add blocking constraint
```

---

# 3. Compatibility Strategy

Use backward-compatible changes where possible.

Recommended:

```text
add before use
write both before read new
read new after backfill
stop old writes before remove old
remove old in separate release
```

Avoid:

```text
renaming columns and deploying code simultaneously without compatibility
dropping fields still used by old code
changing enum values without application support
```

---

# 4. Migration Plan

A migration plan should include:

```text
purpose
tables affected
columns affected
data affected
expected duration
lock risk
deployment order
owner
approval
```

---

# 5. Validation Queries

Define validation queries before running the migration.

Examples:

```sql
-- Check rows needing backfill
SELECT COUNT(*) FROM projects WHERE readiness_score IS NULL;

-- Check tenant scope
SELECT workspace_id, COUNT(*) FROM projects GROUP BY workspace_id;

-- Check duplicate risk
SELECT slug, COUNT(*) FROM projects GROUP BY slug HAVING COUNT(*) > 1;
```

---

# 6. Backfill Execution

For large backfills:

```text
run in batches
commit between batches
track progress
support resume
limit lock duration
throttle if needed
monitor database load
```

Consider background job processing for long-running backfills.

---

# 7. Rollback or Recovery Plan

Define recovery type.

Examples:

```text
rollback SQL migration
restore table from backup
disable feature flag
deploy forward fix
run corrective migration
pause background job
```

Do not claim rollback exists if the migration destroys data.

---

# 8. Monitoring During Deployment

Monitor:

```text
database CPU
lock waits
query latency
error rate
migration duration
replication lag
application health
critical workflow metrics
```

---

# 9. Post-Migration Cleanup

After successful migration:

```text
remove old code path
remove unused columns later
remove dual-write logic
update documentation
update data model diagrams
close migration task
```

---

# 10. Final Principle

> The safest migration is the one that can be deployed, verified and recovered without surprise.
