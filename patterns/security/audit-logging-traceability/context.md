## FILE: `patterns/security/audit-logging-traceability/context.md`

# Audit Logging Traceability — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern fits SaaS products that need evidence of sensitive activity.

Typical contexts:

```text
B2B SaaS
client portals
document platforms
financing platforms
enterprise tools
admin dashboards
support consoles
multi-tenant platforms
```

---

# 2. Product Context

Use this Pattern when users can:

- invite members;
- change roles;
- update settings;
- upload or download files;
- submit approvals;
- change billing;
- connect integrations;
- delete data.

---

# 3. Security Context

Audit logging is important when the system has:

```text
tenant boundaries
sensitive records
private files
admin overrides
support access
API keys
security settings
compliance obligations
```

---

# 4. Operational Context

Audit logs support:

- incident investigation;
- customer support;
- internal accountability;
- regulatory review;
- access review;
- postmortem evidence;
- security monitoring.

---

# 5. Warning Signs

Audit logging is weak when:

- no one can trace permission changes;
- support access is invisible;
- file downloads are not recorded;
- audit logs contain secrets;
- events cannot be filtered by tenant;
- request ids are missing;
- audit logs can be modified by normal admins;
- no retention policy exists.

---

# 6. Final Principle

> Audit context begins where customer trust, security accountability and operational evidence overlap.
