## FILE: `playbooks/operations/prepare-release/README.md`

# Prepare Release Playbook

Version: 0.1.0  
Status: Premium Draft  
Domain: Operations  
Category: Release Readiness

---

# 1. Purpose

The Prepare Release Playbook provides a structured procedure for preparing a software release before deployment.

It helps ensure that scope, code, tests, documentation, security, operations, rollback and communication are ready before a release goes live.

---

# 2. Trigger

Use this Playbook when:

- a new version is ready for release;
- a SaaS feature is moving to production;
- a technical change needs deployment approval;
- a release requires coordination across product, engineering and operations;
- a risky change needs rollback planning;
- a production deployment must be reviewed before execution.

---

# 3. Scope

This Playbook covers:

- release scope confirmation;
- readiness review;
- test and validation review;
- risk and dependency review;
- security and data-impact review;
- deployment planning;
- rollback planning;
- communication planning;
- post-release monitoring.

This Playbook does not replace full incident response, but it prepares the team to reduce release failure risk.

---

# 4. Related Skills

```text
management.technical-project-manager
infrastructure.devops-engineer
engineering.senior-developer
engineering.senior-debugger
security.security-engineer
product.product-manager-saas
```

---

# 5. Final Principle

> A release is ready only when it can be deployed, verified, communicated and rolled back safely.
