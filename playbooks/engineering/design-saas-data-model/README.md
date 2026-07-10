## FILE: `playbooks/engineering/design-saas-data-model/README.md`

# Design SaaS Data Model Playbook

Version: 0.1.0  
Status: Premium Draft  
Domain: Engineering  
Category: Data Modeling

---

# 1. Purpose

The Design SaaS Data Model Playbook provides a structured procedure for converting SaaS product requirements into a clear, scalable and maintainable data model.

It helps define entities, relationships, ownership, tenant boundaries, lifecycle states, constraints, indexes, audit needs and data risks before implementation.

---

# 2. Trigger

Use this Playbook when:

- a SaaS MVP needs a database model;
- a PRD or UX flow introduces new entities;
- a feature requires schema design;
- multi-tenant data boundaries must be clarified;
- permissions depend on resource ownership;
- reporting or dashboard data needs structure;
- database migrations must be planned safely.

---

# 3. Scope

This Playbook covers:

- entity discovery;
- relationship mapping;
- tenant and ownership modeling;
- lifecycle state definition;
- field and constraint definition;
- indexing considerations;
- audit and history needs;
- data sensitivity review;
- migration planning;
- validation and documentation.

This Playbook does not replace full database performance tuning, but it creates the structural foundation for reliable implementation.

---

# 4. Related Skills

```text
engineering.database-engineer
engineering.software-architect
engineering.senior-developer
security.security-engineer
product.business-analyst
```

---

# 5. Final Principle

> A SaaS data model is strong when it reflects the product domain, protects customer boundaries and supports future change without confusion.
