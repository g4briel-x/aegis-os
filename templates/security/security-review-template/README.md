## FILE: `templates/security/security-review-template/README.md`

# Security Review Template

Version: 0.1.0  
Status: Draft  
Domain: Security  
Category: Security Review

---

# 1. Purpose

The Security Review Template provides a reusable structure for reviewing SaaS features, APIs, workflows, data models, infrastructure changes and releases from a security perspective.

It helps product, engineering, architecture, DevOps and security teams identify authentication, authorization, tenant isolation, sensitive data, audit logging, abuse, dependency, operational and compliance risks before production release.

---

# 2. When to Use

Use this Template when:

```text
a feature handles sensitive data
authorization or roles change
tenant-scoped data is accessed
a new API endpoint is introduced
file upload or export is added
billing, identity or audit data changes
external integrations are added
production infrastructure changes
a release has security impact
```

---

# 3. Output

This Template produces:

```text
Security Review Document
```

---

# 4. Related Assets

```text
Related skills:
security.security-engineer
engineering.software-architect
engineering.senior-developer
engineering.database-engineer
infrastructure.devops-engineer

Related playbooks:
security.review-api-security
security.design-auth-rbac
security.harden-production-saas
security.respond-to-security-incident
engineering.write-test-plan
operations.prepare-release

Related patterns:
security.rbac-permission-model
security.tenant-data-isolation
security.audit-logging-traceability
engineering.api-error-handling
operations.incident-severity-model
```

---

# 5. Final Principle

> A security review is useful when it makes security risks explicit before users, data or production systems are exposed.
