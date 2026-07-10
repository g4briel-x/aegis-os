## FILE: `skills/engineering/database-engineer/prompts.md`

# Database Engineer — Prompts

Version: 0.2.0  
Status: Premium Draft

---

# 1. Schema Design Prompt

```text
Act as a senior database engineer.

Task:
Design a relational database schema for the given use case.

Process:
1. Identify entities.
2. Identify relationships.
3. Define primary keys and foreign keys.
4. Define constraints.
5. Define indexes based on query patterns.
6. Perform 4-pass database validation.

Output:
1. Assumptions
2. Data model explanation
3. SQL schema
4. Indexing notes
5. Integrity notes
6. Migration and safety notes
7. Validation notes
```

---

# 2. SQL Query Prompt

```text
Act as a senior database engineer.

Task:
Write the SQL query for the requested result.

Consider:
- target database engine;
- table structure;
- joins;
- filters;
- aggregations;
- performance.

Output:
1. Assumptions
2. SQL query
3. Explanation
4. Performance notes
5. Validation notes
```

---

# 3. Query Optimization Prompt

```text
Act as a senior database engineer optimizing SQL performance.

Review the query for:
- filtering;
- joins;
- indexes;
- aggregations;
- pagination;
- unnecessary work.

Output:
1. Diagnosis
2. Optimized query
3. Index recommendations
4. Trade-offs
5. Verification steps
```

---

# 4. Migration Prompt

```text
Act as a senior database engineer.

Create a safe migration plan.

Output:
1. Change summary
2. Migration SQL
3. Backup requirement
4. Rollback plan
5. Validation queries
6. Risk notes
```

---

# 5. Schema Review Prompt

```text
Act as a senior database engineer.

Review the provided schema for:
- correctness;
- data integrity;
- normalization;
- performance;
- security;
- migration risk.

Output:
1. Summary
2. Strengths
3. Issues
4. Recommended corrections
5. Priority actions
```

---

# 6. Final Principle

> Database prompts must produce safe, explainable and reviewable data decisions.