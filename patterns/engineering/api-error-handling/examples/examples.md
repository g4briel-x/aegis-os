## FILE: `patterns/engineering/api-error-handling/examples/examples.md`

# API Error Handling — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Validation Error

```json
{
  "error": {
    "code": "validation_failed",
    "message": "The request contains invalid fields.",
    "details": [
      {
        "field": "title",
        "code": "required",
        "message": "Title is required."
      }
    ],
    "request_id": "req_1001",
    "documentation_url": null
  }
}
```

---

# 2. Example — Permission Denied

```json
{
  "error": {
    "code": "permission_denied",
    "message": "You do not have permission to perform this action.",
    "details": [],
    "request_id": "req_1002",
    "documentation_url": null
  }
}
```

---

# 3. Example — Conflict

```json
{
  "error": {
    "code": "conflict",
    "message": "A project with this name already exists.",
    "details": [
      {
        "field": "name",
        "code": "already_exists",
        "message": "Project name must be unique."
      }
    ],
    "request_id": "req_1003",
    "documentation_url": null
  }
}
```

---

# 4. Example — Internal Error

```json
{
  "error": {
    "code": "internal_error",
    "message": "An unexpected error occurred.",
    "details": [],
    "request_id": "req_1004",
    "documentation_url": null
  }
}
```

The server logs should contain the internal exception mapped to `req_1004`.

---

# 5. Final Principle

> Examples show that good API errors are consistent, safe and usable by both humans and machines.
