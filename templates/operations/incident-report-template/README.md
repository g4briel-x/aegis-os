## FILE: `templates/operations/incident-report-template/README.md`

# Incident Report Template

Version: 0.1.0  
Status: Draft  
Domain: Operations  
Category: Incident Management

---

# 1. Purpose

The Incident Report Template provides a reusable structure for documenting an active or recently resolved production incident.

It helps engineering, operations, support, security and management teams capture the incident summary, severity, impact, current status, timeline, actions taken, communication, ownership and next steps.

---

# 2. When to Use

Use this Template when:

```text
a production incident is declared
a customer-visible outage occurs
a security or privacy concern is detected
a critical workflow is degraded
support needs a factual incident summary
management needs current incident status
a resolved incident needs a concise operational record
```

---

# 3. Output

This Template produces:

```text
Incident Report Document
```

---

# 4. Difference from Postmortem

```text
Incident Report = operational record during or shortly after the incident
Postmortem = deeper learning review after the incident is resolved
```

---

# 5. Related Assets

```text
Related skills:
infrastructure.devops-engineer
engineering.senior-debugger
security.security-engineer
management.technical-project-manager
engineering.software-architect

Related playbooks:
operations.monitor-saas-production
operations.create-runbook
operations.run-postmortem-review
security.respond-to-security-incident
engineering.debug-production-issue

Related patterns:
operations.incident-severity-model
operations.production-observability-baseline
security.audit-logging-traceability
```

---

# 6. Final Principle

> An incident report should make the current truth clear without speculation.
