## FILE: `playbooks/security/design-auth-rbac/steps.md`

# Design Auth RBAC — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Define Identity and Authentication Model

Clarify how users are identified and authenticated.

Review:

- login method;
- account type;
- identity provider;
- session model;
- token model;
- passwordless or MFA needs;
- user lifecycle;
- invitation flow.

Output:

```text
Authentication model
```

---

# 2. Step 2 — Identify Protected Resources

List everything that requires access control.

Examples:

- user profile;
- organization;
- workspace;
- project;
- file;
- invoice;
- review;
- comment;
- dashboard;
- API key;
- admin setting.

Output:

```text
Protected resource catalog
```

---

# 3. Step 3 — Define Roles and Role Hierarchy

Define the roles that exist in the system.

Examples:

```text
owner
admin
manager
member
viewer
reviewer
client
external_partner
support_admin
```

Capture:

- role purpose;
- scope;
- default permissions;
- escalation risk;
- who can assign the role.

Output:

```text
Role catalog
```

---

# 4. Step 4 — Define Permissions and Actions

Define actions that can be allowed or denied.

Examples:

```text
create
read
update
delete
invite
approve
reject
submit
archive
export
manage_billing
manage_settings
```

Output:

```text
Permission catalog
```

---

# 5. Step 5 — Map Roles to Permissions

Create a role-permission matrix.

For each role, define:

- allowed actions;
- denied actions;
- conditional actions;
- resource scope;
- tenant scope;
- approval requirements.

Output:

```text
Permission matrix
```

---

# 6. Step 6 — Define Ownership and Tenant Boundaries

Clarify access based on ownership and customer separation.

Review:

- tenant entity;
- workspace or organization membership;
- record owner;
- shared resources;
- cross-tenant restrictions;
- support access;
- external partner boundaries.

Output:

```text
Ownership and tenant isolation rules
```

---

# 7. Step 7 — Define API Authorization Rules

Map permissions to API endpoints.

For each endpoint, define:

- required authentication;
- required role;
- required permission;
- ownership check;
- tenant check;
- denied cases;
- audit need.

Output:

```text
API authorization rule table
```

---

# 8. Step 8 — Define Audit and Logging Needs

Identify security-relevant events.

Audit events may include:

- login;
- failed login;
- role change;
- permission change;
- file access;
- billing change;
- admin action;
- data export;
- API key creation;
- sensitive record update.

Output:

```text
Audit event list
```

---

# 9. Step 9 — Define Permission Tests

Create tests that prove access behavior.

Test:

- allowed access;
- denied access;
- cross-tenant access;
- ownership restrictions;
- admin-only behavior;
- role assignment rules;
- unauthenticated access.

Output:

```text
Permission test matrix
```

---

# 10. Step 10 — Produce Security Handoff

Assemble the final RBAC design.

Include:

- authentication model;
- roles;
- permissions;
- tenant rules;
- endpoint authorization;
- audit needs;
- tests;
- open questions.

Output:

```text
Auth RBAC security handoff
```

---

# 11. Final Principle

> RBAC design steps should make access rules enforceable, reviewable and testable.
