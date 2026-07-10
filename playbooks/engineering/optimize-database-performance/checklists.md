## FILE: `playbooks/engineering/optimize-database-performance/checklists.md`

# Optimize Database Performance — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. Performance Intake Checklist

```text
[ ] Affected workflow identified
[ ] Expected performance defined
[ ] Actual performance measured
[ ] User impact described
[ ] Time window captured
[ ] Environment identified
[ ] Recent changes reviewed
```

---

# 2. Query Review Checklist

```text
[ ] Slow query captured
[ ] Query purpose understood
[ ] Filters reviewed
[ ] Joins reviewed
[ ] Sorting reviewed
[ ] Aggregations reviewed
[ ] Result size reviewed
[ ] N+1 pattern checked
```

---

# 3. Execution Plan Checklist

```text
[ ] Execution plan collected
[ ] Sequential scans reviewed
[ ] Index usage reviewed
[ ] Join strategy reviewed
[ ] Estimated versus actual rows reviewed
[ ] Sort cost reviewed
[ ] Temporary file usage checked
[ ] Bottleneck identified
```

---

# 4. Index and Schema Checklist

```text
[ ] Existing indexes reviewed
[ ] Missing index candidates identified
[ ] Composite index order reviewed
[ ] Write overhead considered
[ ] Unused index risk considered
[ ] Foreign keys reviewed
[ ] Table size considered
[ ] Migration risk reviewed
```

---

# 5. Operational Checklist

```text
[ ] Locks reviewed
[ ] Long transactions reviewed
[ ] Connection pool reviewed
[ ] CPU reviewed
[ ] Memory reviewed
[ ] I/O reviewed
[ ] Backup or rollback considered
```

---

# 6. Verification Checklist

```text
[ ] Before metric captured
[ ] After metric captured
[ ] Correctness verified
[ ] Tests run
[ ] Execution plan compared
[ ] Monitoring configured
[ ] Prevention action defined
```

---

# 7. Final Principle

> Database performance checklists prevent optimization from becoming guesswork.