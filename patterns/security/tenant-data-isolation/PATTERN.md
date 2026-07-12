## FILE: `patterns/security/tenant-data-isolation/PATTERN.md`

# Tenant Data Isolation Pattern

Version: 0.1.0  
Status: Draft

---

# 1. Problem

A SaaS product stores data for multiple customers in the same application.

If tenant boundaries are not explicit, users may access data from another organization, workspace or account.

This can happen through:

- API endpoints;
- database queries;
- file downloads;
- background jobs;
- search results;
- reports;
- admin dashboards;
- exports;
- integrations.

---

# 2. Context

This Pattern applies to multi-tenant SaaS systems where data is scoped by:

```text
tenant
organization
workspace
account
client
project
owner
membership
```

It is especially important for B2B SaaS, collaboration platforms, client portals, document platforms and enterprise tools.

---

# 3. Forces

Key forces:

```text
security versus implementation speed
shared infrastructure versus customer isolation
query flexibility versus safe defaults
admin access versus auditability
reporting needs versus boundary control
support access versus customer privacy
```

---

# 4. Recommended Model

Define tenant isolation using this model:

```text
Tenant entity
Tenant-scoped resource
Membership
Role
Permission
Ownership rule
Tenant-aware query
Enforcement point
Audit event
Test case
```

Example:

```text
A project belongs to a workspace.
A user can read a project only when the user has active membership in the same workspace and the required permission.
```

---

# 5. Tenant Scoping Rules

Every tenant-owned table should include a clear scope.

Examples:

```text
projects.workspace_id
documents.workspace_id
comments.workspace_id
invoices.organization_id
audit_events.tenant_id
```

Avoid relying only on global resource IDs.

---

# 6. Query Safety

Queries should include tenant constraints by default.

Recommended practices:

```text
tenant-scoped repository methods
authorization-aware service methods
query helpers that require tenant id
database policies where available
tests for missing tenant filters
```

Bad:

```text
SELECT * FROM projects WHERE id = :project_id;
```

Better:

```text
SELECT * FROM projects
WHERE id = :project_id
AND workspace_id = :current_workspace_id;
```

---

# 7. File and Object Storage Isolation

Files must also follow tenant rules.

Review:

```text
file metadata ownership
storage path design
signed URL permissions
download authorization
upload validation
file deletion rules
audit events for sensitive downloads
```

Storage paths should not be treated as authorization.

---

# 8. Background Jobs

Background jobs must carry tenant context.

Examples:

```text
send notification for tenant
generate report for workspace
process uploaded file for project
sync integration for organization
```

Each job payload should include tenant or resource scope and validate it before processing.

---

# 9. Admin and Support Access

Admin access should be:

```text
least privilege
approved when needed
time-bound if possible
audited
visible in logs
separated from normal user access
```

Support access should not bypass tenant rules silently.

---

# 10. Final Principle

> Tenant isolation should be enforced where data is read, written, exported, processed and downloaded.