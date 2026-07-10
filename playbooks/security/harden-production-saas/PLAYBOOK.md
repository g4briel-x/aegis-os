## FILE: `playbooks/security/harden-production-saas/PLAYBOOK.md`

# Harden Production SaaS — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured hardening process for SaaS applications running in staging or production.

---

# 2. Trigger

A SaaS system is approaching production, already running in production, or undergoing a security-sensitive release.

---

# 3. Inputs

Useful inputs include:

- production architecture;
- deployment environment;
- auth and RBAC model;
- API contract;
- tenant model;
- data model;
- environment variables;
- secrets inventory;
- dependency list;
- logging and monitoring setup;
- backup policy;
- incident response plan.

---

# 4. Outputs

Expected outputs include:

- production hardening report;
- security baseline checklist;
- access control findings;
- tenant isolation findings;
- secrets and configuration findings;
- API exposure findings;
- monitoring and audit findings;
- backup and recovery findings;
- prioritized remediation plan;
- launch readiness decision.

---

# 5. Execution Summary

```text
1. Define production hardening scope
2. Review identity and access controls
3. Review tenant isolation and data boundaries
4. Review API, frontend and file exposure
5. Review secrets and environment configuration
6. Review dependency and supply chain risks
7. Review logging, audit and monitoring
8. Review backup, rollback and recovery
9. Prioritize remediation actions
10. Decide launch or production readiness
```

---

# 6. Completion Criteria

The Playbook is complete when:

- production security scope is defined;
- critical access paths are reviewed;
- tenant boundaries are verified;
- secrets and configuration risks are assessed;
- exposed APIs and file flows are reviewed;
- monitoring and audit gaps are documented;
- recovery readiness is reviewed;
- remediation actions have owners and priorities.

---

# 7. Escalation or Fallback

Escalate when:

- customer data may be exposed;
- tenant isolation is unverified;
- admin access is too broad;
- secrets are stored insecurely;
- backups or rollback are missing;
- public APIs lack rate limits or authorization;
- security-critical issues block launch.

---

# 8. Final Principle

> A SaaS system should not be considered production-ready until its most likely security failures have been reviewed and reduced.
