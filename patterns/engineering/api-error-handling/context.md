## FILE: `patterns/engineering/api-error-handling/context.md`

# API Error Handling — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern fits SaaS systems with multiple API consumers.

Examples:

```text
web frontend
mobile app
external partner integration
admin dashboard
public API
internal service API
```

---

# 2. Product Context

Use this Pattern when:

- users submit forms;
- workflows have validation rules;
- permissions can deny access;
- API failures must be shown in UI;
- support needs request IDs;
- integrations need stable error codes.

---

# 3. Security Context

This Pattern is especially important when:

- private resources exist;
- tenant isolation matters;
- APIs expose customer data;
- file access is controlled;
- authentication or authorization can fail.

---

# 4. Operational Context

Useful when production support needs:

```text
request correlation
safe logs
consistent status codes
error dashboards
alert grouping by error code
debugging without exposing internals to clients
```

---

# 5. Warning Signs

Error handling is weak when:

- frontend checks message strings;
- validation errors vary by endpoint;
- stack traces reach clients;
- 500 errors are used for business validation;
- 200 responses contain failure states;
- support cannot correlate user reports to logs.

---

# 6. Final Principle

> API error context includes the user, the client, the attacker and the operator.
