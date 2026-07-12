## FILE: `patterns/security/tenant-data-isolation/README.md`

# Tenant Data Isolation Pattern

Version: 0.1.0  
Status: Draft  
Domain: Security  
Category: Multi-Tenant SaaS Security

---

# 1. Purpose

The Tenant Data Isolation Pattern defines a reusable model for protecting customer data boundaries in multi-tenant SaaS applications.

It helps teams design tenant scoping, ownership rules, query constraints, authorization checks, file access, auditability and tests that prevent cross-tenant data exposure.

---

# 2. Problem

Multi-tenant SaaS products must ensure that one customer cannot access another customer's data.

Common failure modes:

```text
missing tenant_id filters
unsafe joins
shared file paths
admin overrides without audit
background jobs processing wrong tenant data
API endpoints using only resource id
frontend hiding data instead of backend enforcing access
weak tests for cross-tenant denial
```

---

# 3. Recommended Solution

Make tenant isolation explicit at every layer:

```text
tenant model
tenant-scoped entities
tenant-aware queries
object-level authorization
file access checks
background job scoping
audit logs
cross-tenant test cases
```

---

# 4. Recommended When

Use this Pattern when:

- the SaaS product serves multiple customers;
- organizations, workspaces or accounts own data;
- private files or documents are stored;
- users can belong to multiple tenants;
- APIs expose customer-owned resources;
- background jobs process tenant data;
- enterprise or security readiness matters.

---

# 5. Avoid When

Avoid overbuilding this Pattern when:

- the product is strictly single-tenant;
- every customer has physically separate infrastructure;
- data is entirely public;
- a managed platform fully enforces isolation.

Even then, access boundaries should remain documented.

---

# 6. Related Assets

```text
Related skills:
security.security-engineer
engineering.software-architect
engineering.database-engineer
engineering.senior-developer

Related playbooks:
security.design-auth-rbac
security.harden-production-saas
security.review-api-security
engineering.design-saas-data-model
engineering.create-api-contract
```

---

# 7. Final Principle

> Tenant isolation is not a UI behavior. It is a system-wide security invariant.