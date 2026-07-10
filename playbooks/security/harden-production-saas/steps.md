## FILE: `playbooks/security/harden-production-saas/steps.md`

# Harden Production SaaS — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Define Production Hardening Scope

Clarify what system and environment will be reviewed.

Capture:

- application name;
- environment;
- release version;
- critical workflows;
- sensitive data;
- public surfaces;
- third-party services;
- review owner.

Output:

```text
Production hardening scope
```

---

# 2. Step 2 — Review Identity and Access Controls

Review how users, admins and services access the system.

Check:

- authentication method;
- session management;
- password reset or recovery;
- MFA needs;
- admin roles;
- service accounts;
- least privilege;
- stale users or tokens.

Output:

```text
Identity and access control findings
```

---

# 3. Step 3 — Review Authorization and Tenant Isolation

Verify access control beyond login.

Check:

- role-permission mapping;
- object-level authorization;
- tenant or workspace boundary;
- cross-tenant access prevention;
- support access controls;
- admin override behavior;
- permission tests.

Output:

```text
Authorization and tenant isolation findings
```

---

# 4. Step 4 — Review API, Frontend and File Exposure

Review public and semi-public attack surfaces.

Check:

- public endpoints;
- authenticated endpoints;
- rate limiting;
- CORS configuration;
- file upload validation;
- download authorization;
- frontend exposed secrets;
- error messages;
- API response sensitive fields.

Output:

```text
API and exposure findings
```

---

# 5. Step 5 — Review Secrets and Environment Configuration

Verify sensitive configuration is protected.

Check:

- API keys;
- database credentials;
- OAuth secrets;
- payment secrets;
- deployment tokens;
- environment variable scope;
- secret rotation;
- secrets in logs or repository.

Output:

```text
Secrets and configuration findings
```

---

# 6. Step 6 — Review Dependencies and Supply Chain

Review external code and build risks.

Check:

- outdated dependencies;
- vulnerable packages;
- lockfiles;
- dependency source trust;
- build scripts;
- container image base;
- CI permissions;
- package publishing risk.

Output:

```text
Dependency and supply chain findings
```

---

# 7. Step 7 — Review Logging, Audit and Monitoring

Confirm the system can detect and investigate problems.

Check:

- authentication logs;
- authorization failure logs;
- admin action audit logs;
- data export logs;
- error monitoring;
- security alerts;
- log retention;
- sensitive data redaction.

Output:

```text
Logging audit and monitoring findings
```

---

# 8. Step 8 — Review Backup, Rollback and Recovery

Confirm the system can recover.

Check:

- database backup policy;
- backup restoration test;
- rollback procedure;
- disaster recovery plan;
- incident response plan;
- deployment rollback;
- recovery ownership.

Output:

```text
Backup rollback and recovery findings
```

---

# 9. Step 9 — Prioritize Remediation Actions

Convert findings into a remediation plan.

Classify each item:

```text
blocker
high
medium
low
accepted_risk
```

For each item, define:

- issue;
- impact;
- owner;
- priority;
- due date;
- verification method.

Output:

```text
Prioritized remediation plan
```

---

# 10. Step 10 — Decide Production Readiness

Make a clear readiness decision.

Possible decisions:

```text
ready
ready_with_accepted_risks
not_ready
specialist_review_required
```

Output:

```text
Production hardening readiness decision
```

---

# 11. Final Principle

> Hardening steps should reduce the chance, blast radius and recovery time of production security failures.