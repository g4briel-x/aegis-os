## FILE: `playbooks/engineering/optimize-database-performance/outputs.md`

# Optimize Database Performance — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. Performance Diagnosis

Purpose:

Summarize the performance issue.

Required sections:

```text
Affected workflow:
Symptom:
Expected performance:
Actual performance:
Impact:
Likely bottleneck:
```

---

# 2. Query Analysis

Purpose:

Document query-level findings.

Required sections:

```text
Query:
Purpose:
Issue:
Evidence:
Risk:
Recommended change:
```

---

# 3. Execution Plan Notes

Purpose:

Capture how the database executes the query.

Required sections:

```text
Plan summary:
Bottleneck:
Index usage:
Row estimate issue:
Cost driver:
Observation:
```

---

# 4. Index Recommendation

Purpose:

Define index changes when justified.

Required sections:

```text
Index:
Table:
Columns:
Reason:
Expected benefit:
Write overhead:
Migration risk:
```

---

# 5. Optimization Plan

Purpose:

Define the selected correction.

Required sections:

```text
Optimization:
Reason:
Owner:
Risk:
Rollback:
Verification:
```

---

# 6. Verification Result

Purpose:

Measure improvement.

Required sections:

```text
Before:
After:
Metric:
Result:
Correctness status:
Decision:
```

---

# 7. Prevention Actions

Purpose:

Reduce recurrence.

Required sections:

```text
Action:
Owner:
Priority:
Reason:
Due:
```

---

# 8. Final Principle

> Database performance outputs must make the diagnosis, correction and proof of improvement visible.