## FILE: `templates/security/security-review-template/checklists.md`

# Security Review Template — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Completeness Checklist

```text
[ ] Review scope is defined
[ ] Security owner is assigned
[ ] Risk level is assigned
[ ] Roles are listed
[ ] Resources are listed
[ ] Data types are listed
[ ] APIs are listed if relevant
[ ] Release decision is recorded
```

---

# 2. Authentication and Authorization Checklist

```text
[ ] Authentication is required where needed
[ ] Unauthenticated access is denied
[ ] Required roles are defined
[ ] Required permissions are defined
[ ] Permission checks are server-side
[ ] Resource ownership is checked
[ ] Admin actions are protected
```

---

# 3. Tenant Isolation Checklist

```text
[ ] Tenant boundary is defined
[ ] Tenant identifier is validated
[ ] Cross-tenant reads are denied
[ ] Cross-tenant writes are denied
[ ] Background jobs preserve tenant scope
[ ] File access preserves tenant scope
[ ] Tests cover wrong-tenant access
```

---

# 4. Data Protection Checklist

```text
[ ] Sensitive fields are identified
[ ] Data storage is reviewed
[ ] Encryption needs are reviewed
[ ] Retention rules are reviewed
[ ] Export controls are reviewed
[ ] Error responses do not leak sensitive data
```

---

# 5. Audit and Observability Checklist

```text
[ ] Sensitive actions are audited
[ ] Permission changes are audited
[ ] Admin actions are audited
[ ] Audit events include actor and resource
[ ] Security-relevant failures are observable
[ ] Request id or trace id is available
```

---

# 6. Release Decision Checklist

```text
[ ] Findings are listed
[ ] Required pre-release fixes are assigned
[ ] Accepted risks are documented
[ ] Security decision is explicit
[ ] Approval is recorded
[ ] Follow-up actions are tracked
```

---

# 7. Final Principle

> Security checklists should prove that protected resources fail closed.
