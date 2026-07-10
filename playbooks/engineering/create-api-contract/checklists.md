## FILE: `playbooks/engineering/create-api-contract/checklists.md`

# Create API Contract — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. API Purpose Checklist

```text
[ ] Product workflow identified
[ ] API consumer identified
[ ] Resource purpose defined
[ ] Success outcome defined
[ ] Non-goals documented
[ ] Existing standards reviewed
[ ] Open questions listed
```

---

# 2. Endpoint Checklist

```text
[ ] Endpoint path defined
[ ] HTTP method selected
[ ] Path parameters defined
[ ] Query parameters defined
[ ] Request body defined if needed
[ ] Response body defined
[ ] Status codes defined
```

---

# 3. Schema Checklist

```text
[ ] Required fields marked
[ ] Optional fields marked
[ ] Data types defined
[ ] Validation rules defined
[ ] Defaults defined
[ ] Sensitive fields excluded
[ ] Example payload included
```

---

# 4. Error Checklist

```text
[ ] Validation error defined
[ ] Authentication error defined
[ ] Authorization error defined
[ ] Not found error defined
[ ] Conflict error defined
[ ] Rate limit error defined if needed
[ ] Server error format defined
```

---

# 5. Security Checklist

```text
[ ] Authentication requirement defined
[ ] Role requirement defined
[ ] Object ownership rule defined
[ ] Tenant boundary rule defined
[ ] Sensitive data exposure reviewed
[ ] Audit event considered
[ ] Abuse or rate limit need reviewed
```

---

# 6. Compatibility Checklist

```text
[ ] Existing clients considered
[ ] Breaking changes identified
[ ] Versioning need reviewed
[ ] Deprecated fields documented if needed
[ ] Migration plan defined if needed
[ ] Backward-compatible path preferred
```

---

# 7. Final Principle

> API contract checklists prevent frontend, backend and security from implementing different assumptions.
