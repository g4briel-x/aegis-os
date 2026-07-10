## FILE: `playbooks/infrastructure/deploy-saas-application/README.md`

# Deploy SaaS Application Playbook

Version: 0.1.0  
Status: Premium Draft  
Domain: Infrastructure  
Category: SaaS Deployment

---

# 1. Purpose

The Deploy SaaS Application Playbook provides a structured procedure for deploying a SaaS application safely from a validated build to a production or staging environment.

It helps coordinate deployment readiness, environment configuration, secrets, database migrations, smoke tests, monitoring, rollback and post-deployment verification.

---

# 2. Trigger

Use this Playbook when:

- a SaaS application is ready to deploy;
- a staging or production release must be executed;
- a release candidate has passed CI;
- infrastructure or environment configuration has changed;
- database migrations are part of deployment;
- deployment risk needs operational control;
- rollback and verification must be prepared before launch.

---

# 3. Scope

This Playbook covers:

- deployment readiness;
- environment review;
- secret and configuration checks;
- build artifact validation;
- database migration checks;
- deployment execution;
- smoke testing;
- monitoring;
- rollback readiness;
- post-deployment confirmation.

This Playbook does not replace release planning. It focuses on the execution and verification of deployment.

---

# 4. Related Skills

```text
infrastructure.devops-engineer
infrastructure.cloud-architect
engineering.senior-debugger
engineering.senior-developer
security.security-engineer
management.technical-project-manager
```

---

# 5. Final Principle

> Deployment is safe when the team knows what will change, how to verify it and how to recover if it fails.