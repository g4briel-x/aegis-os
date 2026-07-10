## FILE: `playbooks/engineering/optimize-database-performance/PLAYBOOK.md`

# Optimize Database Performance — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured process for identifying and correcting database performance problems.

---

# 2. Trigger

A database-backed workflow, query, API endpoint, report or background job is slow, unstable or resource-intensive.

---

# 3. Inputs

Useful inputs include:

- slow query;
- affected endpoint;
- execution plan;
- schema;
- indexes;
- database engine;
- table sizes;
- logs;
- metrics;
- recent migrations;
- ORM query output;
- production impact;
- expected performance target.

---

# 4. Outputs

Expected outputs include:

- performance diagnosis;
- query analysis;
- execution plan notes;
- index recommendation;
- schema or query correction;
- risk notes;
- verification steps;
- monitoring recommendations;
- prevention actions.

---

# 5. Execution Summary

```text
1. Define the performance symptom
2. Identify affected queries and workflows
3. Collect database metrics and evidence
4. Review query structure
5. Review execution plan
6. Review indexes and schema
7. Check locks, transactions and connections
8. Select safe optimization
9. Validate improvement
10. Document prevention actions
```

---

# 6. Completion Criteria

The Playbook is complete when:

- the slow behavior is defined;
- the likely database cause is documented;
- optimization is selected;
- correctness risk is reviewed;
- performance improvement is verified;
- monitoring or prevention actions are recorded.

---

# 7. Escalation or Fallback

Escalate when:

- data correctness may be affected;
- production database is under active pressure;
- migration or index creation is risky;
- query changes affect financial or critical data;
- locks threaten availability;
- optimization requires architecture change;
- performance evidence is insufficient.

---

# 8. Final Principle

> Database performance work must be evidence-based, measurable and reversible where possible.