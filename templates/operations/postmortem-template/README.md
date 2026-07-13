## FILE: `templates/operations/postmortem-template/README.md`

# Postmortem Template

Version: 0.1.0  
Status: Draft  
Domain: Operations  
Category: Incident Review

---

# 1. Purpose

The Postmortem Template provides a reusable structure for analyzing production incidents, reliability failures, security events, deployment failures or major operational disruptions.

It helps teams document what happened, who was affected, why it happened, how it was detected, how it was resolved and what corrective actions will prevent recurrence.

---

# 2. When to Use

Use this Template when:

```text
a SEV1 incident occurred
a customer-visible SEV2 incident occurred
a security incident occurred
a data integrity issue occurred
a deployment caused production impact
a repeated incident indicates systemic weakness
a reliability review is required
```

---

# 3. Output

This Template produces:

```text
Incident Postmortem Document
```

---

# 4. Related Assets

```text
Related skills:
infrastructure.devops-engineer
engineering.senior-debugger
security.security-engineer
management.technical-project-manager
engineering.software-architect

Related playbooks:
operations.run-postmortem-review
operations.monitor-saas-production
operations.create-runbook
security.respond-to-security-incident
engineering.debug-production-issue

Related patterns:
operations.incident-severity-model
operations.production-observability-baseline
security.audit-logging-traceability
engineering.database-migration-safety
```

---

# 5. Final Principle

> A postmortem should improve the system, not assign blame.
