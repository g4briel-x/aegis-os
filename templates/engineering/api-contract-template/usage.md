## FILE: `templates/engineering/api-contract-template/usage.md`

# API Contract Template — Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Usage Process

Use this sequence:

```text
1. Define endpoint purpose
2. Define method and path
3. Define authentication and authorization
4. Define request parameters and body
5. Define successful response
6. Define error responses
7. Define pagination, rate limits and idempotency if needed
8. Define side effects
9. Define observability
10. Define test cases and approvals
```

---

# 2. Recommended Review Flow

Review in this order:

```text
Product review
Backend engineering review
Frontend engineering review
Security review
QA review
Operations review if endpoint is high-risk
```

---

# 3. Writing Rules

The API Contract should:

- use stable field names;
- define required and optional fields;
- avoid exposing database internals;
- include authorization rules;
- include safe error behavior;
- include test cases;
- include versioning impact.

---

# 4. Error Rule

Use the standard error envelope:

```text
error.code
error.message
error.details
error.request_id
```

Do not return raw stack traces or internal exception names.

---

# 5. Authorization Rule

Every protected endpoint should define:

```text
authenticated actor
tenant scope
required permission
resource ownership rule
denied behavior
```

---

# 6. Final Principle

> Use the API Contract Template before implementation, not after clients already depend on behavior.
