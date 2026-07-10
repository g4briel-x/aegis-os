## FILE: `playbooks/engineering/design-saas-data-model/PLAYBOOK.md`

# Design SaaS Data Model — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured process for designing a SaaS data model from product requirements.

---

# 2. Trigger

A SaaS product, feature, PRD or workflow needs a clear database structure before implementation.

---

# 3. Inputs

Useful inputs include:

- product concept;
- PRD;
- UX flow;
- user roles;
- business objects;
- workflows;
- permission model;
- reporting needs;
- integration needs;
- security requirements;
- expected scale;
- existing database schema.

---

# 4. Outputs

Expected outputs include:

- entity list;
- relationship map;
- ownership and tenant model;
- field definitions;
- lifecycle state model;
- constraint list;
- index candidates;
- audit and history notes;
- data sensitivity notes;
- migration plan;
- open data questions.

---

# 5. Execution Summary

```text
1. Understand product domain and workflows
2. Identify core entities
3. Define relationships
4. Define ownership and tenant boundaries
5. Define fields and constraints
6. Define lifecycle states
7. Review permissions and sensitive data
8. Identify indexes and query patterns
9. Plan migration and validation
10. Produce data model handoff
```

---

# 6. Completion Criteria

The Playbook is complete when:

- core entities are defined;
- relationships are clear;
- ownership and tenant boundaries are explicit;
- fields and constraints are documented;
- lifecycle states are known;
- sensitive data is identified;
- initial indexes and query patterns are considered;
- migration and validation notes are prepared.

---

# 7. Escalation or Fallback

Escalate when:

- product rules are unclear;
- tenant boundaries are ambiguous;
- sensitive or regulated data is involved;
- schema changes affect production data;
- reporting needs conflict with normalized design;
- performance risks are significant;
- deletion, retention or audit rules are unclear.

---

# 8. Final Principle

> Data modeling should make the product domain explicit before code turns assumptions into permanent structure.