## FILE: `playbooks/security/review-api-security/checklists.md`

# Review API Security — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. API Scope Checklist

```text
[ ] Endpoint path documented
[ ] HTTP method documented
[ ] Purpose documented
[ ] Consumer identified
[ ] Exposure level identified
[ ] Protected resources identified
[ ] Owner identified
```

---

# 2. Authentication Checklist

```text
[ ] Authentication requirement defined
[ ] Token or session handling reviewed
[ ] Expiry behavior reviewed
[ ] Anonymous access justified if allowed
[ ] Service-to-service identity considered
[ ] Credentials not exposed
```

---

# 3. Authorization Checklist

```text
[ ] Roles identified
[ ] Resource ownership checked
[ ] Tenant isolation checked
[ ] Object-level authorization checked
[ ] Admin-only actions protected
[ ] Privilege escalation risk reviewed
```

---

# 4. Input Validation Checklist

```text
[ ] Required fields validated
[ ] Types validated
[ ] Length limits defined
[ ] Allowed values constrained
[ ] File upload rules defined if relevant
[ ] Injection risks reviewed
[ ] Malformed input handled safely
```

---

# 5. Data Exposure Checklist

```text
[ ] Sensitive fields removed
[ ] Tokens and secrets not returned
[ ] Internal debug data not returned
[ ] Cross-tenant leakage checked
[ ] Response fields minimized
[ ] Error responses reviewed
```

---

# 6. Abuse and Observability Checklist

```text
[ ] Rate limits considered
[ ] Request size limits considered
[ ] Pagination limits considered
[ ] Expensive operations reviewed
[ ] Security logs defined
[ ] Audit events defined
[ ] Suspicious behavior alerts considered
```

---

# 7. Final Principle

> API security checklists make hidden permission and data exposure risks visible before release.
