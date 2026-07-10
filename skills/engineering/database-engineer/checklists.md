## FILE: `skills/engineering/database-engineer/checklists.md`

# Database Engineer — Checklists

Version: 0.2.0  
Status: Premium Draft

---

# 1. Schema Design Checklist

```text
[ ] Business entities identified
[ ] Relationships defined
[ ] Primary keys defined
[ ] Foreign keys defined
[ ] Nullability reviewed
[ ] Unique constraints reviewed
[ ] Indexes justified by query patterns
[ ] Audit fields considered
[ ] Naming is consistent
```

---

# 2. SQL Query Checklist

```text
[ ] Target database engine identified
[ ] Required tables identified
[ ] Joins are correct
[ ] Filters match business rules
[ ] Aggregations are correct
[ ] Edge cases considered
[ ] Query is readable
[ ] Result columns are appropriate
```

---

# 3. Performance Checklist

```text
[ ] Query filters reviewed
[ ] Join columns reviewed
[ ] Index usage considered
[ ] Large table behavior considered
[ ] Pagination considered where relevant
[ ] N+1 risk considered
[ ] Expensive aggregations reviewed
```

---

# 4. Migration Checklist

```text
[ ] Backup requirement defined
[ ] Rollback plan defined
[ ] Destructive changes identified
[ ] Data transformation validated
[ ] Downtime risk assessed
[ ] Compatibility reviewed
[ ] Post-migration validation queries provided
```

---

# 5. Security Checklist

```text
[ ] SQL injection risk considered
[ ] Sensitive columns identified
[ ] Least privilege considered
[ ] Access boundaries reviewed
[ ] Audit fields considered
[ ] Data exposure risks documented
```

---

# 6. 4-Pass Validation Checklist

```text
[ ] Pass 1 completed — syntax and compatibility
[ ] Pass 2 completed — data model and integrity
[ ] Pass 3 completed — performance and indexing
[ ] Pass 4 completed — safety and operational readiness
[ ] Issues corrected or documented
```

---

# 7. Final Principle

> Database checklists prevent hidden data risks from becoming production failures.
