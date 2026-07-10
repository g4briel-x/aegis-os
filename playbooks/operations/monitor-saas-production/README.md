## FILE: `playbooks/operations/monitor-saas-production/README.md`

# Monitor SaaS Production Playbook

Version: 0.1.0  
Status: Premium Draft  
Domain: Operations  
Category: Production Monitoring

---

# 1. Purpose

The Monitor SaaS Production Playbook provides a structured procedure for monitoring a live SaaS application after deployment or during normal operations.

It helps teams detect errors, latency, degraded user flows, infrastructure pressure, security signals and business-impacting issues before they become major incidents.

---

# 2. Trigger

Use this Playbook when:

- a SaaS application is running in production;
- a release has just been deployed;
- production health needs daily or weekly review;
- user complaints increase;
- error rate, latency or resource usage changes;
- a critical workflow needs monitoring;
- an incident or regression must be detected early.

---

# 3. Scope

This Playbook covers:

- health signal definition;
- error monitoring;
- latency and performance monitoring;
- infrastructure monitoring;
- database monitoring;
- critical user flow monitoring;
- security signal monitoring;
- alert review;
- escalation;
- follow-up actions.

This Playbook does not replace incident response, but it detects when incident response should start.

---

# 4. Related Skills

```text
infrastructure.devops-engineer
infrastructure.cloud-architect
engineering.senior-debugger
security.security-engineer
management.technical-project-manager
```

---

# 5. Final Principle

> Production monitoring is useful only when signals lead to clear decisions and timely action.
