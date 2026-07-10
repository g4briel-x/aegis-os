## FILE: `playbooks/engineering/design-saas-data-model/examples/examples.md`

# Design SaaS Data Model — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — Audiovisual Project Financing SaaS

## Trigger

A platform needs a data model for creators submitting film, series and documentary projects for financing review.

## Expected Execution

The Playbook should guide the team to:

- define user, organization, project, document, review and investor entities;
- model project ownership;
- define submission lifecycle states;
- define reviewer permissions;
- identify sensitive documents;
- plan file metadata and audit events.

## Expected Output

```text
Entity list
Relationship map
Tenant model
Field definitions
Lifecycle state model
Index candidates
Migration plan
Open data questions
```

---

# 2. Example — Client Portal Data Model

## Trigger

A client portal requires projects, invoices, documents and users.

## Expected Execution

The Playbook should guide the team to:

- define client organization boundary;
- model documents and invoice visibility;
- define admin and viewer permissions;
- add audit needs for invoice access.

---

# 3. Example — Team Workspace SaaS

## Trigger

A SaaS product needs workspaces, members and roles.

## Expected Execution

The Playbook should guide the team to:

- define workspace entity;
- create membership join entity;
- model role assignments;
- prevent cross-workspace access.

---

# 4. Example — Dashboard Metrics Data Model

## Trigger

A dashboard needs metrics from projects, tasks and user activity.

## Expected Execution

The Playbook should guide the team to:

- identify source tables;
- define aggregation model;
- decide between live query and precomputed metrics;
- identify indexes and freshness needs.

---

# 5. Final Principle

> Examples show how data modeling connects product workflows to reliable database structure.
