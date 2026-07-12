# FILE: `patterns/security/audit-logging-traceability/trade-offs.md`

# Audit Logging Traceability — Trade-Offs

Version: 0.1.0  
Status: Draft

---

# 1. Benefits

This Pattern improves:

```text
incident investigation
admin accountability
customer trust
security monitoring
compliance readiness
support clarity
postmortem evidence
```

---

# 2. Costs

This Pattern adds:

```text
storage volume
event design work
retention management
access policy complexity
test coverage requirements
privacy review effort
```

---

# 3. Security Trade-Offs

Audit logs improve security evidence but may become sensitive assets.

Mitigation:

```text
restrict access
avoid secrets
encrypt when required
apply retention policy
audit access to audit logs when needed
```

---

# 4. Product Trade-Offs

Customer-visible audit logs improve trust but may expose internal implementation details.

Mitigation:

```text
separate internal and customer-facing event views
use safe action labels
hide internal metadata
document event meaning
```

---

# 5. Operational Trade-Offs

Detailed events improve investigation but can create noise.

Mitigation:

```text
audit high-value actions
avoid low-value event spam
group by action type
define alert-worthy events separately
```

---

# 6. Main Risks

Key risks:

```text
missing critical events
logging sensitive data
no tenant scope
mutable logs
unrestricted audit access
no retention policy
unsearchable event format
```

---

# 7. Mitigations

Mitigate with:

- action catalog;
- safe metadata rules;
- append-only storage;
- access policy;
- retention policy;
- audit tests;
- periodic security review.

---

# 8. Final Principle

> Audit logging is valuable only when the evidence is trustworthy, safe and findable.