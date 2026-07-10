## FILE: `patterns/security/rbac-permission-model/README.md`

# RBAC Permission Model Pattern

Version: 0.1.0  
Status: Draft  
Domain: Security  
Category: Access Control

---

# 1. Purpose

The RBAC Permission Model Pattern defines a reusable access-control structure for SaaS applications.

It helps teams define roles, permissions, resources, tenant boundaries, ownership checks, enforcement points and permission tests in a way that is understandable, auditable and safe to implement.

---

# 2. Problem

SaaS teams often start with vague roles such as `admin`, `member` and `viewer`, but fail to define what those roles can actually do.

This creates risks:

```text
over-permissioned users
unclear authorization logic
cross-tenant data exposure
inconsistent API checks
weak tests
uncontrolled admin power
```

---

# 3. Recommended Solution

Use an explicit RBAC model:

```text
Subject = user or service account
Role = assigned access profile
Resource = protected object
Permission = allowed action
Scope = tenant, workspace, organization or ownership boundary
Policy = rule that combines role, resource, permission and scope
Enforcement point = API, service, UI or background job where the policy is checked
```

---

# 4. Recommended When

Use this Pattern when:

- the product has multiple user roles;
- customer data must be protected;
- organizations or workspaces exist;
- API endpoints need consistent authorization;
- admin actions need auditability;
- permissions must be tested;
- SaaS tenant isolation matters.

---

# 5. Avoid When

Avoid overbuilding this Pattern when:

- the product is a simple single-user tool;
- there is no shared or sensitive data;
- permissions are temporary prototype logic;
- a managed platform already fully controls authorization.

Even in those cases, keep access rules explicit.

---

# 6. Related Assets

```text
Related skills:
security.security-engineer
engineering.software-architect
engineering.senior-developer
engineering.database-engineer

Related playbooks:
security.design-auth-rbac
security.review-api-security
security.harden-production-saas
engineering.create-api-contract
engineering.design-saas-data-model
```

---

# 7. Final Principle

> RBAC is safe when every allowed action is explicit and every denied action is testable.
