## FILE: `playbooks/engineering/design-saas-data-model/steps.md`

# Design SaaS Data Model — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Understand Product Domain and Workflows

Start with the business process, not tables.

Review:

- user roles;
- main workflows;
- business objects;
- required actions;
- lifecycle events;
- reporting needs;
- external integrations.

Output:

```text
Domain and workflow summary
```

---

# 2. Step 2 — Identify Core Entities

List the main objects the system must store.

Examples:

- user;
- organization;
- workspace;
- project;
- file;
- invoice;
- payment;
- comment;
- review;
- notification;
- audit event.

Output:

```text
Core entity list
```

---

# 3. Step 3 — Define Relationships

Map how entities connect.

Relationship types include:

- one-to-one;
- one-to-many;
- many-to-many;
- parent-child;
- ownership;
- membership;
- approval or review relationship.

Output:

```text
Relationship map
```

---

# 4. Step 4 — Define Ownership and Tenant Boundaries

Clarify who owns each record and how customer data is separated.

Review:

- tenant entity;
- workspace or organization boundary;
- user ownership;
- shared resources;
- admin access;
- cross-tenant restrictions.

Output:

```text
Ownership and tenant model
```

---

# 5. Step 5 — Define Fields and Constraints

Define fields for each entity.

Capture:

- field name;
- type;
- required or optional;
- uniqueness;
- default value;
- validation rule;
- foreign key;
- business constraint.

Output:

```text
Field definition table
```

---

# 6. Step 6 — Define Lifecycle States

Identify how entities move through states.

Examples:

```text
draft
submitted
in_review
approved
rejected
archived
deleted
```

Review:

- allowed transitions;
- actor allowed to transition;
- timestamp fields;
- audit requirements.

Output:

```text
Lifecycle state model
```

---

# 7. Step 7 — Review Permissions and Sensitive Data

Check security and privacy implications.

Review:

- sensitive fields;
- personal data;
- payment data;
- private files;
- role-based access;
- object-level authorization;
- audit needs;
- retention requirements.

Output:

```text
Data security and permission notes
```

---

# 8. Step 8 — Identify Query Patterns and Index Candidates

Design for expected access patterns.

Review:

- list views;
- filters;
- search;
- dashboard queries;
- reporting;
- joins;
- sorting;
- pagination;
- high-volume tables.

Output:

```text
Query pattern and index candidate list
```

---

# 9. Step 9 — Plan Migration and Validation

Define how the schema will be implemented safely.

Capture:

- migration order;
- seed data;
- backfill need;
- rollback constraints;
- validation queries;
- test data needs;
- production risk.

Output:

```text
Migration and validation plan
```

---

# 10. Step 10 — Produce Data Model Handoff

Assemble the data model for engineering review.

Include:

- entities;
- fields;
- relationships;
- tenant model;
- lifecycle states;
- constraints;
- indexes;
- risks;
- open questions.

Output:

```text
Data model handoff
```

---

# 11. Final Principle

> Data modeling steps should preserve domain meaning while preparing for safe implementation.