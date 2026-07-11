## FILE: `patterns/engineering/api-error-handling/PATTERN.md`

# API Error Handling Pattern

Version: 0.1.0  
Status: Draft

---

# 1. Problem

A SaaS API must communicate failures clearly without leaking sensitive implementation details.

Without a standard error model, each endpoint may return different structures:

```text
plain text
HTML error pages
raw stack traces
inconsistent JSON
different validation formats
unclear authorization errors
```

This increases frontend complexity, weakens observability and creates security risk.

---

# 2. Context

This Pattern applies when the system has:

- API endpoints;
- frontend clients;
- mobile clients;
- external integrations;
- authentication and authorization;
- validation-heavy forms;
- production observability needs.

---

# 3. Forces

Key forces:

```text
developer clarity versus security secrecy
user-friendly messages versus technical detail
frontend simplicity versus backend flexibility
stable codes versus evolving behavior
debuggability versus sensitive data protection
```

---

# 4. Recommended Error Envelope

Use one envelope for all API errors:

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": [],
    "request_id": "string",
    "documentation_url": "string|null"
  }
}
```

Field meaning:

```text
code: stable machine-readable error identifier
message: safe human-readable message
details: optional structured error details
request_id: correlation id for logs and support
documentation_url: optional support or API docs reference
```

---

# 5. Standard Error Categories

Recommended categories:

```text
validation_failed
authentication_required
invalid_credentials
permission_denied
resource_not_found
conflict
rate_limited
payload_too_large
unsupported_media_type
dependency_failed
internal_error
service_unavailable
```

---

# 6. HTTP Status Mapping

Recommended mapping:

```text
400 validation_failed
401 authentication_required / invalid_credentials
403 permission_denied
404 resource_not_found
409 conflict
413 payload_too_large
415 unsupported_media_type
422 semantic_validation_failed
429 rate_limited
500 internal_error
502 dependency_failed
503 service_unavailable
```

---

# 7. Validation Details

Validation errors should include structured field information.

Example:

```json
{
  "error": {
    "code": "validation_failed",
    "message": "The request contains invalid fields.",
    "details": [
      {
        "field": "email",
        "code": "invalid_format",
        "message": "Email format is invalid."
      }
    ],
    "request_id": "req_123",
    "documentation_url": null
  }
}
```

---

# 8. Security Rules

Never expose:

```text
stack traces
SQL queries
secret names or values
internal file paths
dependency credentials
authorization policy internals
existence of private resources when unsafe
```

For authorization-sensitive resources, consider returning `404` instead of `403` when revealing resource existence creates risk.

---

# 9. Logging Rules

API responses should be safe and concise.

Server logs should capture more context:

```text
request_id
user_id if available
tenant_id if available
endpoint
status
error_code
internal exception type
safe diagnostic context
```

Do not log sensitive data.

---

# 10. Final Principle

> Error handling is part of the API contract, not an afterthought.
