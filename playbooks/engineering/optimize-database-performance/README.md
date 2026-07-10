## FILE: `playbooks/engineering/optimize-database-performance/README.md`

# Optimize Database Performance Playbook

Version: 0.1.0  
Status: Premium Draft  
Domain: Engineering  
Category: Database Performance

---

# 1. Purpose

The Optimize Database Performance Playbook provides a structured procedure for diagnosing, improving and validating database performance in SaaS applications.

It helps teams investigate slow queries, missing indexes, inefficient joins, excessive load, lock contention, connection issues and database-related production degradation.

---

# 2. Trigger

Use this Playbook when:

- API latency increases because of database queries;
- dashboards or reports load slowly;
- database CPU, memory or I/O usage is high;
- slow query logs show repeated issues;
- a release introduces database regression;
- a query times out;
- users experience degraded workflows;
- database performance must be reviewed before scale.

---

# 3. Scope

This Playbook covers:

- performance symptom definition;
- slow query analysis;
- execution plan review;
- indexing review;
- schema and relationship review;
- N+1 query detection;
- lock and transaction review;
- connection pool review;
- mitigation planning;
- verification and monitoring.

This Playbook does not replace full database architecture design, but it provides a repeatable optimization process.

---

# 4. Related Skills

```text
engineering.database-engineer
engineering.senior-debugger
engineering.software-architect
infrastructure.devops-engineer
infrastructure.cloud-architect
```

---

# 5. Final Principle

> Database optimization is successful when performance improves measurably without damaging correctness, safety or maintainability.
