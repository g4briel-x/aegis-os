## FILE: `patterns/operations/incident-severity-model/README.md`

# Incident Severity Model Pattern

Version: 0.1.0  
Status: Draft  
Domain: Operations  
Category: Incident Management

---

# 1. Purpose

The Incident Severity Model Pattern defines a reusable model for classifying production incidents by customer impact, urgency, business risk, security exposure and operational response requirements.

It helps teams decide how fast to respond, who to involve, how to communicate, when to escalate and how to review incidents after resolution.

---

# 2. Problem

SaaS teams often react to incidents inconsistently.

Common failures:

```text
severity is decided emotionally
customer impact is unclear
security incidents are under-classified
minor alerts trigger major response
major failures are treated too slowly
communication is delayed
ownership is unclear
postmortems are inconsistent
```

---

# 3. Recommended Solution

Define a severity model with clear levels, impact criteria and response expectations.

A good severity model should define:

```text
severity levels
impact criteria
response time
escalation path
communication rules
incident roles
resolution expectations
postmortem requirement
customer notification policy
```

---

# 4. Recommended When

Use this Pattern when:

- a SaaS product has production users;
- incidents require coordinated response;
- alerts need prioritization;
- support and engineering need shared language;
- customer impact must drive urgency;
- security and reliability events need classification;
- postmortems must be standardized.

---

# 5. Avoid When

Avoid overcomplicating this Pattern when:

- the product has no users;
- the system is a local prototype;
- every alert is handled manually by the same person;
- severity levels are unused by the team.

Even then, critical failures should still have an escalation rule.

---

# 6. Related Assets

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
operations.production-observability-baseline
security.audit-logging-traceability
operations.feature-flag-rollout
```

---

# 7. Final Principle

> Incident severity should be based on customer and business impact, not internal stress level.