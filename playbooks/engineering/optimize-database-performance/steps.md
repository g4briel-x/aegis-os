## FILE: `playbooks/engineering/optimize-database-performance/steps.md`

# Optimize Database Performance — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Define the Performance Symptom

Clarify the exact issue.

Capture:

- affected endpoint or workflow;
- expected performance;
- actual performance;
- frequency;
- user impact;
- time window;
- environment.

Output:

```text
Performance symptom summary
```

---

# 2. Step 2 — Identify Affected Queries

Find the queries connected to the symptom.

Review:

- application logs;
- slow query logs;
- ORM-generated SQL;
- database monitoring;
- query fingerprints;
- affected background jobs;
- affected reports.

Output:

```text
Affected query list
```

---

# 3. Step 3 — Collect Metrics and Evidence

Gather evidence before changing query or schema.

Collect:

- latency;
- query duration;
- row counts;
- table sizes;
- CPU usage;
- memory usage;
- I/O usage;
- locks;
- connection count;
- error rates.

Output:

```text
Database performance evidence
```

---

# 4. Step 4 — Review Query Structure

Inspect the query for inefficiency.

Check:

- unnecessary columns;
- missing filters;
- unbounded result sets;
- expensive joins;
- repeated subqueries;
- sorting on large datasets;
- aggregation cost;
- pagination strategy;
- N+1 query patterns.

Output:

```text
Query structure findings
```

---

# 5. Step 5 — Review Execution Plan

Analyze how the database executes the query.

Check:

- sequential scans;
- index scans;
- join strategy;
- sort cost;
- filter selectivity;
- estimated versus actual rows;
- temporary files;
- nested loops;
- full table scans.

Output:

```text
Execution plan analysis
```

---

# 6. Step 6 — Review Indexes and Schema

Check whether the schema supports the workload.

Review:

- existing indexes;
- missing indexes;
- unused indexes;
- composite index order;
- foreign keys;
- data types;
- constraints;
- denormalization need;
- partitioning need.

Output:

```text
Index and schema review
```

---

# 7. Step 7 — Check Locks, Transactions and Connections

Identify operational database pressure.

Review:

- long-running transactions;
- lock waits;
- deadlocks;
- connection pool saturation;
- idle transactions;
- transaction isolation issues;
- queue or worker behavior.

Output:

```text
Lock and connection review
```

---

# 8. Step 8 — Select Optimization Strategy

Choose the safest effective correction.

Possible strategies:

- rewrite query;
- add index;
- adjust composite index;
- limit selected columns;
- add pagination;
- precompute or cache results;
- reduce N+1 queries;
- split expensive workflow;
- tune connection pool;
- schedule heavy jobs off-peak.

Output:

```text
Optimization plan
```

---

# 9. Step 9 — Validate Improvement

Measure before and after.

Validate:

- query duration;
- endpoint latency;
- execution plan change;
- CPU or I/O reduction;
- correctness;
- regression risk;
- production safety.

Output:

```text
Performance verification result
```

---

# 10. Step 10 — Document Prevention

Define how to avoid recurrence.

Examples:

- query performance tests;
- index review before release;
- slow query alerting;
- pagination policy;
- ORM query review;
- dashboard monitoring;
- migration review checklist.

Output:

```text
Database performance prevention actions
```

---

# 11. Final Principle

> Database optimization steps should improve the bottleneck, not blindly add complexity.