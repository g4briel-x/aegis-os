## FILE: `patterns/security/rbac-permission-model/examples/examples.md`

# RBAC Permission Model — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Financing SaaS

## Context

A platform allows creators to submit projects, reviewers to evaluate them and investors to access selected opportunities.

## Roles

```text
creator
reviewer
investor
workspace_admin
platform_admin
```

## Permissions

```text
project.create
project.update
project.submit
project.review
project.approve
document.upload
document.download
investor_room.read
admin.user_manage
```

## Rule Examples

```text
creator can update own draft project.
creator cannot update project after submission.
reviewer can read assigned projects only.
investor can read approved investor-room projects only.
platform_admin actions are audited.
```

---

# 2. Example — Workspace SaaS

## Roles

```text
owner
admin
member
viewer
billing_admin
```

## Rule Examples

```text
owner can manage billing and delete workspace.
admin can invite members but cannot delete workspace.
member can create projects.
viewer can read projects but cannot edit.
billing_admin can manage invoices but not project content.
```

---

# 3. Example — Client Portal

## Roles

```text
client_admin
client_user
internal_support
account_manager
```

## Rule Examples

```text
client_user can read documents in their organization.
client_admin can invite users to their organization.
internal_support requires audited temporary access.
account_manager can view account summary but not private files.
```

---

# 4. Example — Permission Test Case

```text
Test:
A user from workspace A attempts to read a project from workspace B.

Expected:
Access denied.

Evidence:
API returns 403 or 404 according to system policy.
No sensitive project fields are returned.
Access denial is logged if required.
```

---

# 5. Final Principle

> Examples show that RBAC must connect real product roles to concrete protected actions.
