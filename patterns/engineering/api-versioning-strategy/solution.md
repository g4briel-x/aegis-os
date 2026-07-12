## FILE: `patterns/engineering/api-versioning-strategy/solution.md`

# API Versioning Strategy — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Solution Overview

Create a controlled API evolution model.

Core components:

```text
versioning method
compatibility rules
breaking change process
deprecation policy
migration guide
contract tests
documentation
monitoring
sunset plan
```

---

# 2. Versioning Method

Select one primary approach.

Recommended for early REST SaaS:

```text
/api/v1
/api/v2
```

Example:

```text
GET /api/v1/projects
GET /api/v2/projects
```

Use header or date-based versioning only when the team can support the added operational discipline.

---

# 3. Compatibility Rules

Write rules that define what can change inside an existing version.

Safe changes:

```text
add optional fields
add new endpoints
add optional filters
improve performance
fix incorrect behavior when no client depends on it
```

Unsafe changes:

```text
remove fields
change field type
rename fields
change error codes
change pagination format
change authorization model
change webhook payload shape
```

---

# 4. Breaking Change Workflow

For breaking changes:

```text
1. Identify affected clients
2. Create new version or compatibility path
3. Write migration guide
4. Add contract tests
5. Update documentation
6. Announce deprecation
7. Monitor usage
8. Sunset old version after migration window
```

---

# 5. Deprecation Notice Template

Use this format:

```text
Deprecated API:
Replacement:
Reason:
Migration steps:
First notice date:
Sunset date:
Affected clients:
Support contact:
```

---

# 6. Migration Guide

A migration guide should include:

```text
old request
new request
old response
new response
field mapping
error changes
authentication changes
pagination changes
test examples
timeline
```

---

# 7. Contract Testing

Use contract tests to protect versions.

Test categories:

```text
request schema
response schema
error schema
authentication behavior
authorization behavior
pagination behavior
webhook payloads
deprecated compatibility
```

---

# 8. Monitoring

Track API version usage.

Useful metrics:

```text
requests_by_api_version
errors_by_api_version
deprecated_endpoint_usage
client_id_by_version
webhook_delivery_failures
migration_progress
```

---

# 9. Sunset

Before removing an old version:

```text
confirm usage is below threshold
notify remaining customers
verify migration support
prepare rollback or restore plan
remove docs only after removal
monitor errors after sunset
```

---

# 10. Final Principle

> API versioning succeeds when clients can migrate deliberately instead of discovering breakage accidentally.
