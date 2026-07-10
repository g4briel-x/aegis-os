## FILE: `playbooks/infrastructure/deploy-saas-application/examples/examples.md`

# Deploy SaaS Application — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — SaaS MVP Production Deployment

## Trigger

A SaaS MVP has passed CI and is ready for first production deployment.

## Expected Execution

The Playbook should guide the team to:

- confirm target environment;
- verify build and CI;
- check environment variables;
- confirm secrets;
- deploy the application;
- run smoke tests;
- monitor logs and errors;
- confirm launch status.

## Expected Output

```text
Deployment readiness summary
Execution log
Smoke test result
Monitoring result
Post-deployment confirmation
```

---

# 2. Example — Staging Deployment With Database Migration

## Trigger

A staging deployment includes a schema migration.

## Expected Execution

The Playbook should guide the team to:

- review migration;
- confirm rollback limits;
- deploy to staging;
- validate database state;
- run smoke tests;
- document migration findings.

---

# 3. Example — Production Hotfix Deployment

## Trigger

A hotfix must be deployed to repair a production issue.

## Expected Execution

The Playbook should guide the team to:

- confirm minimal scope;
- check CI;
- deploy quickly but safely;
- monitor the affected workflow;
- confirm incident recovery.

---

# 4. Example — Deployment With Feature Flag

## Trigger

A new feature is deployed behind a feature flag.

## Expected Execution

The Playbook should guide the team to:

- confirm flag default state;
- deploy code;
- verify disabled behavior;
- enable for limited users;
- monitor errors and feedback.

---

# 5. Final Principle

> Examples show that deployment execution must combine speed, evidence and recovery readiness.
