## FILE: `patterns/security/tenant-data-isolation/examples/examples.md`

# Tenant Data Isolation — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Financing SaaS

## Context

Creators, studios and reviewers use a SaaS platform to manage project financing materials.

## Tenant Boundary

```text
workspace
```

## Scoped Resources

```text
projects.workspace_id
documents.workspace_id
reviews.workspace_id
audit_events.workspace_id
```

## Rule Examples

```text
Creator can read only projects in their workspace.
Reviewer can read assigned projects in the same workspace.
Investor can access only approved investor-room materials.
Document download checks workspace membership and document permission.
```

---

# 2. Example — Client Portal

## Tenant Boundary

```text
client_organization
```

## Rule Examples

```text
Client user can read invoices only inside their organization.
Internal support access requires audit event.
Document export requires client organization scope.
```

---

# 3. Example — Unsafe Query

Bad:

```sql
SELECT * FROM documents WHERE id = :document_id;
```

Better:

```sql
SELECT * FROM documents
WHERE id = :document_id
AND workspace_id = :workspace_id;
```

---

# 4. Example — Cross-Tenant Test

```text
Test:
User from workspace A requests project from workspace B.

Expected:
Access denied.
No project fields returned.
Event logged if policy requires it.
```

---

# 5. Final Principle

> Examples show that tenant isolation must be visible in schema, queries, APIs, files and tests.
