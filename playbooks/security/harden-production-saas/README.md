## FILE: `playbooks/security/harden-production-saas/README.md`

# Harden Production SaaS Playbook

Version: 0.1.0  
Status: Premium Draft  
Domain: Security  
Category: Production Hardening

---

# 1. Purpose

The Harden Production SaaS Playbook provides a structured procedure for strengthening the security posture of a SaaS application before or after production launch.

It helps teams review authentication, authorization, tenant isolation, secrets, environment configuration, API exposure, logging, monitoring, backups, dependency risks and operational recovery readiness.

---

# 2. Trigger

Use this Playbook when:

- a SaaS product is preparing for production;
- a production system needs security review;
- a major release changes security-sensitive behavior;
- customer data is being stored or processed;
- multi-tenant access must be verified;
- public APIs or file uploads are enabled;
- compliance, audit or enterprise readiness is required.

---

# 3. Scope

This Playbook covers:

- production security baseline;
- identity and access control;
- tenant isolation;
- API and frontend hardening;
- secrets and configuration;
- dependency and supply chain review;
- logging and auditability;
- monitoring and alerting;
- backup and recovery;
- hardening evidence and follow-up actions.

This Playbook does not replace a full penetration test, but it prepares the system for safer production operation and specialist review.

---

# 4. Related Skills

```text
security.security-engineer
infrastructure.devops-engineer
infrastructure.cloud-architect
engineering.software-architect
engineering.senior-developer
```

---

# 5. Final Principle

> Production hardening is successful when critical risks are reduced, controls are verified and recovery is possible under pressure.
