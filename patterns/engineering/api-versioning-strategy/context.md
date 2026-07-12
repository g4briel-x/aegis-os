## FILE: `patterns/engineering/api-versioning-strategy/context.md`

# API Versioning Strategy — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern fits SaaS products where APIs are consumed by more than one client or where clients cannot always be updated instantly.

Typical contexts:

```text
web frontend and backend deployed separately
mobile application
public API
partner integration
enterprise automation
internal service API
webhook platform
```

---

# 2. Product Context

Use this Pattern when API changes affect:

- onboarding;
- billing;
- project workflows;
- file uploads;
- permissions;
- reporting;
- webhooks;
- external customer integrations.

---

# 3. Technical Context

The Pattern applies to:

```text
REST APIs
GraphQL APIs
webhook payloads
SDKs
OpenAPI contracts
mobile backends
integration APIs
```

---

# 4. Operational Context

Operators and support teams need to know:

- which versions are supported;
- which clients use old versions;
- when a deprecated endpoint will be removed;
- how to identify version-related failures;
- how to guide customers through migration.

---

# 5. Security Context

Versioning must preserve security posture.

Avoid:

```text
old versions with weaker authorization
deprecated endpoints exposing extra data
legacy error behavior leaking sensitive details
unsupported versions remaining public forever
```

---

# 6. Warning Signs

API evolution is unsafe when:

- changes are made without contract tests;
- clients parse undocumented fields;
- old mobile apps break after backend release;
- deprecated endpoints have no sunset date;
- error codes change silently;
- API documentation does not match production;
- webhooks change without notice.

---

# 7. Final Principle

> API versioning context includes every client that depends on the contract, not only the backend team.
