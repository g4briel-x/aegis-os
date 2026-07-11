## FILE: `patterns/engineering/api-error-handling/solution.md`

# API Error Handling — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Error Envelope

Use one error response shape.

```json
{
  "error": {
    "code": "permission_denied",
    "message": "You do not have permission to perform this action.",
    "details": [],
    "request_id": "req_abc123",
    "documentation_url": null
  }
}
```

---

# 2. Error Code Catalog

Define stable error codes.

Example:

```text
validation_failed
authentication_required
invalid_credentials
permission_denied
resource_not_found
conflict
rate_limited
dependency_failed
internal_error
```

Codes should be:

- lowercase;
- snake_case;
- stable;
- documented;
- safe for clients to branch on.

---

# 3. Validation Error Format

Use structured field-level details.

```json
{
  "field": "project_title",
  "code": "required",
  "message": "Project title is required."
}
```

For nested fields:

```json
{
  "field": "documents[0].type",
  "code": "unsupported_value",
  "message": "Document type is not supported."
}
```

---

# 4. Error Message Rules

Messages should be:

```text
short
safe
clear
user-actionable when possible
not dependent on internal implementation
```

Bad:

```text
SQLSTATE 23505: duplicate key value violates unique constraint projects_slug_key
```

Good:

```text
A project with this slug already exists.
```

---

# 5. Request ID

Every error should include a request id.

Use it to connect:

```text
client error
server logs
trace
support ticket
incident investigation
```

---

# 6. Internal Exception Mapping

Map internal exceptions to public errors.

Example:

```text
ValidationException -> 400 validation_failed
AuthRequiredException -> 401 authentication_required
PermissionException -> 403 permission_denied
NotFoundException -> 404 resource_not_found
UniqueConstraintException -> 409 conflict
RateLimitException -> 429 rate_limited
UnhandledException -> 500 internal_error
```

---

# 7. Logging Model

Log safe diagnostic context.

Recommended fields:

```text
request_id
error_code
status_code
endpoint
method
user_id
tenant_id
exception_type
duration_ms
safe_context
```

Avoid logging:

```text
passwords
tokens
private file contents
payment data
full request bodies containing sensitive data
```

---

# 8. Client Handling

Clients should rely on:

```text
HTTP status
error.code
error.details
```

Clients should not rely on:

```text
exact message text
stack traces
undocumented fields
```

---

# 9. Test Cases

Test:

```text
validation error shape
authentication error shape
authorization error shape
not found behavior
conflict behavior
rate limit behavior
internal error does not leak details
request_id is present
```

---

# 10. Final Principle

> The API error model should be stable for clients and safe for production.
