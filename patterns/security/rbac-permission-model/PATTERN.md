## FILE: `patterns/security/rbac-permission-model/PATTERN.md`

# RBAC Permission Model Pattern

Version: 0.1.0  
Status: Draft

---

# 1. Problem

A SaaS system needs to control what users can do across resources, organizations, workspaces or tenants.

Naive authorization often looks like:

```text
if user.is_admin:
  allow
else:
  deny
```

This becomes unsafe when the product grows.

Problems appear when:

- users have multiple roles;
- resources belong to organizations;
- users can belong to several workspaces;
- admin power differs by scope;
- support users need temporary access;
- API and UI rules drift apart;
- tests only cover happy paths.

---

# 2. Context

This Pattern applies to SaaS products with:

```text
multiple roles
organization or workspace accounts
shared resources
protected API endpoints
private files or records
admin settings
billing or sensitive data
```

It is especially useful in B2B SaaS, marketplaces, client portals, collaboration tools and enterprise products.

---

# 3. Forces

Key forces:

```text
security versus usability
least privilege versus operational convenience
simple roles versus flexible permissions
tenant isolation versus shared workflows
admin power versus auditability
implementation speed versus long-term governance
```

---

# 4. Recommended Model

Use this structure:

```text
User
Role
Permission
Resource
Scope
Policy
Enforcement Point
Audit Event
```

Example:

```text
Role: workspace_admin
Resource: project
Permission: project.update
Scope: workspace
Condition: user must be a member of the same workspace
Audit: log project.status_change when status changes
```

---

# 5. Role Design

Roles should describe responsibility, not vague power.

Example roles:

```text
owner
admin
manager
member
viewer
reviewer
billing_admin
support_admin
external_partner
```

Each role should define:

- purpose;
- scope;
- assigner;
- allowed permissions;
- denied permissions;
- risk level;
- audit requirement.

---

# 6. Permission Design

Permissions should be action-based.

Examples:

```text
project.create
project.read
project.update
project.delete
project.submit
project.approve
document.upload
document.download
billing.manage
workspace.invite_member
settings.update
audit.read
```

Avoid vague permissions:

```text
project.manage
data.access
admin.all
```

Use broad permissions only when carefully justified.

---

# 7. Resource and Scope Design

Every protected action should define its resource and scope.

Common scopes:

```text
global
tenant
organization
workspace
project
owner
assigned
public
```

Example:

```text
A reviewer may read a project only when assigned to that project.
A workspace admin may invite members only inside the same workspace.
A creator may update a project only while it is still in draft state and owned by them.
```

---

# 8. Enforcement Points

Authorization must be enforced where actions happen.

Common enforcement points:

```text
API middleware
application service
domain policy
database query scope
file access layer
background job
admin action handler
```

Do not rely on frontend-only permission checks.

---

# 9. Testing Requirement

Every permission model should include tests for:

```text
allowed access
denied access
cross-tenant access
unauthenticated access
wrong role access
wrong owner access
admin-only access
sensitive data exposure
```

---

# 10. Final Principle

> Permission models should be designed as product behavior, not hidden as scattered conditional code.
