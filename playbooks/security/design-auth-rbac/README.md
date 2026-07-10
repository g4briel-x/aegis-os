## FILE: `playbooks/security/design-auth-rbac/README.md`

# Design Auth RBAC Playbook

Version: 0.1.0  
Status: Premium Draft  
Domain: Security  
Category: Authentication and Authorization

---

# 1. Purpose

The Design Auth RBAC Playbook provides a structured procedure for designing authentication, roles, permissions and access-control rules for SaaS applications.

It helps teams define who can access the system, what actions each role can perform, which resources are protected, how tenant isolation works and how permissions are validated before implementation.

---

# 2. Trigger

Use this Playbook when:

- a SaaS product needs login and access control;
- a new feature introduces roles or permissions;
- multi-tenant access boundaries must be defined;
- admin, member, reviewer or client roles are needed;
- object-level authorization is required;
- API endpoints need permission rules;
- sensitive data or private files must be protected.

---

# 3. Scope

This Playbook covers:

- authentication model;
- role model;
- permission matrix;
- object ownership;
- tenant isolation;
- API authorization rules;
- admin access controls;
- audit requirements;
- test coverage;
- security review handoff.

This Playbook does not replace implementation of an identity provider. It defines the access-control design that implementation must satisfy.

---

# 4. Related Skills

```text
security.security-engineer
engineering.software-architect
engineering.senior-developer
engineering.database-engineer
product.business-analyst
```

---

# 5. Final Principle

> Access control is safe when every protected action has an explicit subject, resource, permission and enforcement point.
