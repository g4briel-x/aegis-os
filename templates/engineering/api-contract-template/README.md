## FILE: `templates/engineering/api-contract-template/README.md`

# API Contract Template

Version: 0.1.0  
Status: Draft  
Domain: Engineering  
Category: API Design

---

# 1. Purpose

The API Contract Template provides a reusable structure for documenting REST or HTTP API endpoints before implementation.

It helps product, engineering, security, frontend, backend and QA teams align on endpoint behavior, authentication, authorization, request schema, response schema, errors, pagination, versioning, observability and test cases.

---

# 2. When to Use

Use this Template when:

```text
a new API endpoint is being designed
an existing API is being changed
frontend and backend teams need a stable contract
external integrations depend on API behavior
API security must be reviewed
API tests need clear expected behavior
API documentation must be generated or maintained
```

---

# 3. Output

This Template produces:

```text
API Contract Document
```

---

# 4. Related Assets

```text
Related skills:
engineering.software-architect
engineering.senior-developer
security.security-engineer
engineering.senior-debugger
product.business-analyst

Related playbooks:
engineering.create-api-contract
security.review-api-security
engineering.write-test-plan
engineering.review-pull-request
operations.prepare-release

Related patterns:
engineering.api-error-handling
engineering.api-versioning-strategy
security.rbac-permission-model
security.tenant-data-isolation
```

---

# 5. Final Principle

> An API contract is ready when client and server can be built and tested from the same document.
