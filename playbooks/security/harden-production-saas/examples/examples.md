## FILE: `playbooks/security/harden-production-saas/examples/examples.md`

# Harden Production SaaS — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — SaaS MVP Production Launch

## Trigger

A SaaS MVP is ready for first production launch.

## Expected Execution

The Playbook should guide the team to:

- review auth and RBAC;
- verify tenant isolation;
- review environment secrets;
- check public APIs;
- confirm monitoring;
- confirm backups and rollback;
- create remediation plan.

## Expected Output

```text
Production hardening report
Access control findings
Tenant isolation findings
Secrets findings
Remediation plan
Readiness decision
```

---

# 2. Example — New File Upload Feature

## Trigger

A release adds file uploads for customer documents.

## Expected Execution

The Playbook should guide the team to:

- review file type and size validation;
- check storage permissions;
- verify download authorization;
- confirm malware or abuse considerations;
- add audit logs for file access.

---

# 3. Example — Enterprise Customer Readiness

## Trigger

An enterprise customer asks about security controls before adoption.

## Expected Execution

The Playbook should guide the team to:

- summarize access controls;
- document audit logging;
- review backups;
- identify hardening gaps;
- prepare remediation timeline.

---

# 4. Example — Admin Dashboard Release

## Trigger

A production release adds admin-only dashboards.

## Expected Execution

The Playbook should guide the team to:

- verify admin permissions;
- test denied access for non-admins;
- audit admin actions;
- prevent sensitive data overexposure.

---

# 5. Final Principle

> Examples show that production hardening connects security design, operational control and launch readiness.
