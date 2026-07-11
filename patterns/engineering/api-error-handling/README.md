## FILE: `patterns/engineering/api-error-handling/README.md`

# API Error Handling Pattern

Version: 0.1.0  
Status: Draft  
Domain: Engineering  
Category: API Design

---

# 1. Purpose

The API Error Handling Pattern defines a reusable model for returning predictable, safe and actionable API errors in SaaS applications.

It helps teams standardize error responses across validation, authentication, authorization, not found, conflict, rate limit, dependency and internal server failures.

---

# 2. Problem

APIs often fail inconsistently.

Common issues:

```text
different error formats per endpoint
unclear error messages
sensitive internal details exposed
frontend cannot handle errors reliably
validation errors are hard to display
authorization errors leak resource existence
logs lack correlation with user-facing errors
```

---

# 3. Recommended Solution

Use a standard API error envelope:

```json
{
  "error": {
    "code": "validation_failed",
    "message": "The request contains invalid fields.",
    "details": [],
    "request_id": "req_123",
    "documentation_url": null
  }
}
```

Each error should include:

```text
stable machine-readable code
safe human-readable message
optional structured details
request or trace id
appropriate HTTP status
no sensitive internals
consistent logging
```

---

# 4. Recommended When

Use this Pattern when:

- the product exposes REST or HTTP APIs;
- frontend and backend need predictable error behavior;
- API clients require stable error codes;
- validation errors must be shown to users;
- security-sensitive errors need safe responses;
- production debugging requires correlation IDs.

---

# 5. Related Assets

```text
Related skills:
engineering.senior-developer
engineering.software-architect
security.security-engineer
engineering.senior-debugger

Related playbooks:
engineering.create-api-contract
security.review-api-security
engineering.write-test-plan
engineering.review-pull-request
```

---

# 6. Final Principle

> API errors should be clear enough for clients to act and safe enough for attackers to learn nothing useful.
