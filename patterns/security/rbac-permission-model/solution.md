## FILE: `patterns/security/rbac-permission-model/solution.md`

# RBAC Permission Model — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Solution Overview

Design access control using this model:

```text
Subject
Role
Permission
Resource
Scope
Condition
Enforcement Point
Audit Event
```

---

# 2. Role Catalog

Create a role catalog.

Example:

```text
owner:
  scope: workspace
  purpose: full control over workspace
  assignable_by: existing owner
  risk: high

admin:
  scope: workspace
  purpose: manage members and settings
  assignable_by: owner
  risk: high

member:
  scope: workspace
  purpose: normal contributor
  assignable_by: owner_or_admin
  risk: medium

viewer:
  scope: workspace
  purpose: read-only access
  assignable_by: owner_or_admin
  risk: low
```

---

# 3. Permission Catalog

Create explicit permissions.

Example:

```text
workspace.read
workspace.update
workspace.delete
workspace.invite_member
workspace.remove_member
project.create
project.read
project.update
project.delete
document.upload
document.download
billing.manage
audit.read
```

---

# 4. Resource Scope Model

Define how each resource is scoped.

Example:

```text
users: global identity, scoped access through memberships
workspaces: tenant boundary
projects: workspace-scoped
documents: project-scoped and workspace-scoped
invoices: workspace-scoped, billing role required
audit_events: workspace-scoped, admin or owner only
```

---

# 5. Policy Matrix

Create a matrix:

```text
Role | Resource | Action | Scope | Condition | Allowed
```

Example:

```text
workspace_admin | project | update | same_workspace | project.status != archived | yes
reviewer | project | read | assigned_project | review.assignment active | yes
viewer | billing | manage | same_workspace | none | no
```

---

# 6. Enforcement Strategy

Enforce permissions in multiple layers:

```text
API route: authenticate user
application service: check permission
repository/query: enforce tenant scope
file service: check file access
audit service: record sensitive actions
```

Do not trust only frontend checks.

---

# 7. Permission Test Matrix

Every critical permission should have tests:

```text
allowed role succeeds
wrong role fails
wrong tenant fails
wrong owner fails
unauthenticated fails
archived or locked resource fails
admin action is audited
```

---

# 8. Audit Strategy

Audit high-risk events:

```text
role change
permission change
member invite
billing update
file download
data export
admin action
support access
tenant setting change
```

---

# 9. Implementation Guidance

Recommended implementation:

```text
central permission constants
central policy definitions
resource ownership resolver
tenant scope resolver
authorization helper
API middleware for authentication
service-level checks for authorization
test helpers for role scenarios
```

---

# 10. Final Principle

> RBAC implementation should centralize policy and decentralize enforcement at the correct action boundaries.
