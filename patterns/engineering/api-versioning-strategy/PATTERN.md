## FILE: `patterns/engineering/api-versioning-strategy/PATTERN.md`

# API Versioning Strategy Pattern

Version: 0.1.0  
Status: Draft

---

# 1. Problem

An API must evolve without unexpectedly breaking consumers.

API changes can affect:

- frontend applications;
- mobile applications;
- partner integrations;
- automation scripts;
- enterprise customers;
- internal services;
- documentation and SDKs.

Without versioning discipline, small backend changes can become client outages.

---

# 2. Context

This Pattern applies when a SaaS system exposes APIs through:

```text
REST
GraphQL
webhooks
public endpoints
partner integrations
internal service contracts
mobile backends
SDKs
```

It is especially useful when API clients cannot all be updated at the same time.

---

# 3. Forces

Key forces:

```text
product evolution versus client stability
API simplicity versus compatibility layers
fast delivery versus migration planning
clean contracts versus legacy support
public API trust versus internal refactoring
```

---

# 4. Recommended Versioning Model

Choose one primary versioning method.

Common options:

```text
URI versioning: /api/v1/projects
header versioning: Accept: application/vnd.product.v1+json
query versioning: ?version=1
date-based versioning: API-Version: 2026-07-12
GraphQL field evolution: additive schema plus deprecation
```

For most early SaaS REST APIs, URI versioning is simple and explicit.

---

# 5. Compatibility Rules

Treat these as backward-compatible:

```text
add optional response field
add optional request field
add new endpoint
add new enum value only if clients handle unknown values
improve validation message without changing error code
```

Treat these as breaking changes:

```text
remove field
rename field
change field type
change endpoint path
change required request field
change authentication requirement
change error code contract
change pagination behavior
change response semantics
```

---

# 6. Breaking Change Policy

Breaking changes should require:

```text
new API version or compatibility layer
migration guide
deprecation notice
client impact review
contract tests
release communication
sunset timeline
approval
```

Do not silently change behavior for existing clients.

---

# 7. Deprecation Policy

A deprecation notice should include:

```text
deprecated endpoint or field
replacement endpoint or field
reason
migration steps
deadline
support contact
risk of not migrating
```

Deprecation should be visible in documentation and release notes.

---

# 8. Testing Strategy

API versioning requires contract tests.

Test:

```text
old client behavior still works
new version behavior works
deprecated endpoint returns expected response
error format remains stable
auth behavior remains stable
pagination remains stable
webhooks remain stable
```

---

# 9. Documentation

API documentation should include:

```text
current version
supported versions
deprecated versions
change log
migration guides
examples per version
sunset dates
```

---

# 10. Final Principle

> API changes should be designed as client migrations, not just backend edits.