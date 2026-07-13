## FILE: `templates/engineering/api-contract-template/checklists.md`

# API Contract Template — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Completeness Checklist

```text
[ ] API name is defined
[ ] Method is defined
[ ] Path is defined
[ ] Version is defined
[ ] Request schema is defined
[ ] Response schema is defined
[ ] Error responses are defined
[ ] Test cases are included
```

---

# 2. Security Checklist

```text
[ ] Authentication requirement is defined
[ ] Authorization rule is defined
[ ] Tenant boundary is defined if relevant
[ ] Resource ownership is checked
[ ] Sensitive fields are not exposed
[ ] Error responses are safe
[ ] Audit event is defined if needed
```

---

# 3. Client Readiness Checklist

```text
[ ] Frontend can build from contract
[ ] Backend can implement from contract
[ ] QA can test from contract
[ ] Error behavior is predictable
[ ] Pagination is documented if relevant
[ ] Versioning impact is documented
```

---

# 4. Operations Checklist

```text
[ ] Request id is included
[ ] Logs are defined
[ ] Metrics are defined
[ ] Rate limits are defined if needed
[ ] Side effects are documented
[ ] Background jobs are documented if triggered
```

---

# 5. Approval Checklist

```text
[ ] Product approved
[ ] Backend approved
[ ] Frontend approved
[ ] Security approved if required
[ ] QA approved
[ ] Operations approved if required
```

---

# 6. Final Principle

> An API contract is complete when behavior is testable before code is written.
