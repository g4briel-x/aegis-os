## FILE: `playbooks/security/design-auth-rbac/examples/examples.md`

# Design Auth RBAC — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — Audiovisual Financing SaaS Roles

## Trigger

A platform needs access control for creators, reviewers, investors and admins.

## Expected Execution

The Playbook should guide the team to:

- define creator, reviewer, investor and admin roles;
- protect project records by owner;
- restrict reviewer access to assigned projects;
- restrict investors to approved public deal rooms;
- audit project approval and document access.

## Expected Output

```text
Authentication model
Role catalog
Permission matrix
Tenant isolation rules
API authorization rules
Permission test matrix
```

---

# 2. Example — Workspace SaaS RBAC

## Trigger

A workspace product needs owner, admin, member and viewer roles.

## Expected Execution

The Playbook should guide the team to:

- define workspace membership;
- map roles to project actions;
- prevent cross-workspace reads;
- restrict billing to owner/admin roles.

---

# 3. Example — Client Portal Permissions

## Trigger

A client portal allows clients to view invoices and documents.

## Expected Execution

The Playbook should guide the team to:

- define client organization boundary;
- restrict invoice access;
- define document visibility;
- audit downloads.

---

# 4. Example — Internal Support Access

## Trigger

Support team needs limited access to customer records for troubleshooting.

## Expected Execution

The Playbook should guide the team to:

- define time-bound support access;
- require approval;
- log access events;
- restrict sensitive fields.

---

# 5. Final Principle

> Examples show how RBAC connects roles, resources, tenants and enforcement points.
