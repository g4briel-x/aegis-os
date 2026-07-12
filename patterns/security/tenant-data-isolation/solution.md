## FILE: `patterns/security/tenant-data-isolation/solution.md`

# Tenant Data Isolation — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Solution Overview

Design tenant isolation as a system invariant.

Core elements:

```text
tenant entity
membership model
tenant-scoped resources
authorization policy
safe query layer
file access control
tenant-aware jobs
audit logging
test matrix
```

---

# 2. Tenant Entity

Define the tenant boundary.

Possible tenant entities:

```text
organization
workspace
account
client
company
team
```

Choose one primary boundary for the MVP.

---

# 3. Resource Scoping

Map every protected entity to a tenant.

Example:

```text
workspace owns projects
workspace owns documents through projects
organization owns invoices
workspace owns audit events
user belongs to workspace through membership
```

---

# 4. Membership Model

A user should access tenant data through membership or assignment.

Example:

```text
users
workspaces
workspace_memberships
roles
permissions
```

The membership should define:

- user;
- tenant;
- role;
- status;
- created date;
- removed date if relevant.

---

# 5. Safe Query Layer

Use tenant-aware data access methods.

Example:

```text
findProjectForWorkspace(projectId, workspaceId)
listDocumentsForProject(projectId, workspaceId)
getInvoiceForOrganization(invoiceId, organizationId)
```

Avoid generic methods that fetch protected records without scope.

---

# 6. API Enforcement

Each protected endpoint should check:

```text
authentication
tenant membership
role or permission
resource ownership
resource state
```

Example endpoint rule:

```text
GET /workspaces/:workspaceId/projects/:projectId
requires authenticated user
requires active membership in workspace
requires project.read permission
requires project.workspace_id == workspaceId
```

---

# 7. File Access

File access should require metadata authorization.

Flow:

```text
request file
load file metadata with tenant scope
check user permission
generate signed URL or stream file
audit sensitive download
```

Never authorize only by storage path.

---

# 8. Background Jobs

Job payloads should include scope.

Example:

```yaml
job:
  type: generate_project_report
  workspace_id: wsp_123
  project_id: prj_456
```

Worker should validate that the project belongs to the workspace before processing.

---

# 9. Testing Strategy

Create cross-tenant tests.

Test examples:

```text
user from tenant A cannot read tenant B project
user from tenant A cannot download tenant B file
workspace admin cannot manage another workspace
search results only include current tenant
background job rejects mismatched tenant and resource
```

---

# 10. Final Principle

> Tenant isolation succeeds when unsafe access is hard to write and easy to detect.