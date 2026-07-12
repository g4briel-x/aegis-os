## FILE: `patterns/security/audit-logging-traceability/README.md`

# Audit Logging Traceability Pattern

Version: 0.1.0  
Status: Draft  
Domain: Security  
Category: Audit and Traceability

---

# 1. Purpose

The Audit Logging Traceability Pattern defines a reusable model for recording sensitive actions, security-relevant events and operational changes in SaaS applications.

It helps teams create audit logs that are useful for security reviews, compliance, incident response, customer support, admin accountability and production investigation.

---

# 2. Problem

SaaS systems often log technical errors but fail to record meaningful business and security actions.

Common failures:

```text
no record of who changed what
admin actions are invisible
permission changes are not traceable
file downloads are not audited
support access is not recorded
logs contain sensitive data
events cannot be correlated to requests
customers cannot prove what happened
```

---

# 3. Recommended Solution

Define audit events for high-risk actions.

Each audit event should capture:

```text
actor
action
resource
tenant
timestamp
request_id
source_ip if appropriate
result
before and after values when safe
reason or context
```

Audit logs should be tamper-resistant, searchable and safe from sensitive-data leakage.

---

# 4. Recommended When

Use this Pattern when:

- the product stores customer data;
- admin or support actions exist;
- permissions can change;
- files or documents can be accessed;
- billing or security settings can change;
- enterprise customers require traceability;
- incident response needs evidence.

---

# 5. Avoid When

Avoid excessive audit logging when:

- events are low-value noise;
- logs would expose sensitive data;
- audit storage has no retention policy;
- no one owns review or access;
- normal observability logs already satisfy the need.

Even then, sensitive actions should remain traceable.

---

# 6. Related Assets

```text
Related skills:
security.security-engineer
engineering.senior-debugger
engineering.senior-developer
engineering.database-engineer
infrastructure.devops-engineer

Related playbooks:
security.harden-production-saas
security.respond-to-security-incident
security.review-api-security
operations.monitor-saas-production
operations.create-runbook

Related patterns:
security.tenant-data-isolation
security.rbac-permission-model
engineering.api-error-handling
```

---

# 7. Final Principle

> Audit logs should answer who did what, to which resource, under which tenant, when and with what result.
