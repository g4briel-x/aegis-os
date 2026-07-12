## FILE: `patterns/operations/production-observability-baseline/README.md`

# Production Observability Baseline Pattern

Version: 0.1.0  
Status: Draft  
Domain: Operations  
Category: Observability

---

# 1. Purpose

The Production Observability Baseline Pattern defines the minimum observability foundation required for operating a SaaS application safely in production.

It helps teams define logs, metrics, traces, dashboards, alerts, health checks, error tracking, request correlation and operational review practices before production incidents happen.

---

# 2. Problem

SaaS teams often launch without enough visibility into production behavior.

Common failures:

```text
no request correlation
no useful dashboards
alerts are missing or noisy
logs lack tenant and user context
errors are visible only after customer reports
latency issues are hard to diagnose
background jobs fail silently
business-critical workflows are not monitored
```

---

# 3. Recommended Solution

Create a baseline observability model covering:

```text
structured logs
key metrics
distributed traces when needed
request ids
health checks
error tracking
dashboards
alerts
SLO indicators
business workflow monitoring
incident evidence
```

---

# 4. Recommended When

Use this Pattern when:

- a SaaS product is moving toward production;
- production support needs visibility;
- incidents are difficult to diagnose;
- background jobs exist;
- API latency matters;
- customer workflows need monitoring;
- reliability and trust are business priorities.

---

# 5. Avoid When

Avoid overbuilding this Pattern when:

- the product is a local prototype;
- no real users exist yet;
- observability tooling cost exceeds immediate risk;
- the system is fully managed and already observable.

Even then, basic logs and error tracking should exist before external users use the system.

---

# 6. Related Assets

```text
Related skills:
infrastructure.devops-engineer
engineering.senior-debugger
engineering.software-architect
security.security-engineer
management.technical-project-manager

Related playbooks:
operations.monitor-saas-production
operations.create-runbook
operations.prepare-release
operations.run-postmortem-review
infrastructure.deploy-saas-application
engineering.debug-production-issue

Related patterns:
engineering.api-error-handling
security.audit-logging-traceability
operations.feature-flag-rollout
```

---

# 7. Final Principle

> Production observability should make system behavior visible before customers become the monitoring system.
