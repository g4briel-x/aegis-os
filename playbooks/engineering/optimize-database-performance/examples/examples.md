## FILE: `playbooks/engineering/optimize-database-performance/examples/examples.md`

# Optimize Database Performance — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — Slow Dashboard Query

## Trigger

A SaaS dashboard takes 12 seconds to load because of a slow aggregate query.

## Expected Execution

The Playbook should guide the team to:

- identify the slow query;
- inspect execution plan;
- review indexes on filter and grouping columns;
- consider precomputed metrics;
- verify endpoint latency after optimization.

## Expected Output

```text
Performance diagnosis
Query analysis
Execution plan notes
Optimization plan
Verification result
Prevention actions
```

---

# 2. Example — N+1 Query in API

## Trigger

An API endpoint loads project records and performs one database query per project.

## Expected Execution

The Playbook should guide the team to:

- identify repeated queries;
- replace N+1 access with eager loading or batched query;
- verify fewer queries and improved latency;
- add regression test.

---

# 3. Example — Missing Index on Search

## Trigger

Search becomes slow as the project table grows.

## Expected Execution

The Playbook should guide the team to:

- review filter and sort columns;
- analyze execution plan;
- recommend appropriate index;
- consider write overhead;
- validate performance improvement.

---

# 4. Example — Lock Contention After Migration

## Trigger

Database writes slow down after a new migration.

## Expected Execution

The Playbook should guide the team to:

- inspect locks;
- identify long transactions;
- review migration behavior;
- define safe correction;
- plan prevention for future migrations.

---

# 5. Final Principle

> Examples show that database performance work must connect symptoms, evidence, change and measurable improvement.
