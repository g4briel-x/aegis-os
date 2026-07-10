## FILE: `playbooks/operations/prepare-release/examples/examples.md`

# Prepare Release — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — SaaS Billing Feature Release

## Trigger

A new billing feature is ready for production release.

## Expected Execution

The Playbook should guide the team to:

- confirm release scope;
- review payment provider integration;
- review authorization and audit logs;
- verify test coverage;
- define rollback and feature flag;
- prepare support communication;
- monitor payment errors after release.

## Expected Output

```text
Release readiness summary
Security review notes
Deployment plan
Rollback plan
Monitoring plan
Go / no-go decision
```

---

# 2. Example — Database Migration Release

## Trigger

A release includes a database migration.

## Expected Execution

The Playbook should guide the team to:

- review migration safety;
- confirm backup;
- define rollback limits;
- run validation queries;
- monitor errors and data integrity after deployment.

---

# 3. Example — API Version Release

## Trigger

A new API version is being released.

## Expected Execution

The Playbook should guide the team to:

- check backward compatibility;
- review authorization;
- validate error responses;
- update documentation;
- monitor API errors and client failures.

---

# 4. Example — Hotfix Release

## Trigger

A production bug requires a fast hotfix.

## Expected Execution

The Playbook should guide the team to:

- confirm minimal scope;
- validate fix against root cause;
- skip non-essential changes;
- define rollback;
- monitor recovery signals.

---

# 5. Example — Frontend Feature Release

## Trigger

A new SaaS dashboard feature is ready for production.

## Expected Execution

The Playbook should guide the team to:

- confirm acceptance criteria;
- verify UX states;
- test responsive behavior;
- monitor frontend errors;
- collect user feedback.

---

# 6. Final Principle

> Examples show that release preparation adapts to risk while preserving the same readiness discipline.
