## FILE: `patterns/engineering/api-error-handling/checklists.md`

# API Error Handling — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Context Fit Checklist

```text
[ ] API clients exist
[ ] Frontend needs predictable errors
[ ] Validation errors must be displayed
[ ] Authorization failures occur
[ ] Production support needs request ids
[ ] Security-sensitive resources exist
```

---

# 2. Error Envelope Checklist

```text
[ ] Standard error envelope defined
[ ] Stable error code included
[ ] Safe message included
[ ] Details field included if needed
[ ] Request id included
[ ] Documentation URL included or intentionally omitted
```

---

# 3. Error Code Checklist

```text
[ ] Error code catalog exists
[ ] Codes are stable
[ ] Codes are machine-readable
[ ] HTTP status mapping exists
[ ] Business validation is not returned as 500
[ ] Internal errors are generic
```

---

# 4. Security Checklist

```text
[ ] Stack traces are not exposed
[ ] SQL details are not exposed
[ ] Secrets are not exposed
[ ] Sensitive resource existence is protected
[ ] Auth errors are safe
[ ] Logs avoid sensitive data
```

---

# 5. Test Checklist

```text
[ ] Validation error tested
[ ] Authentication error tested
[ ] Authorization error tested
[ ] Not found error tested
[ ] Conflict error tested
[ ] Internal error safety tested
[ ] Request id presence tested
```

---

# 6. Final Principle

> API error checklists make failure behavior part of quality assurance.
