## FILE: `patterns/engineering/api-versioning-strategy/examples/examples.md`

# API Versioning Strategy — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Financing SaaS API

## Context

A SaaS platform exposes project submission APIs to web frontend and partner tools.

## Current API

```text
GET /api/v1/projects/:id
POST /api/v1/projects/:id/submit
```

## Breaking Change

The project readiness response changes from:

```json
{
  "score": 82
}
```

to:

```json
{
  "readiness": {
    "score": 82,
    "level": "investor_ready"
  }
}
```

## Safe Strategy

```text
keep v1 response unchanged
create v2 response shape
document field mapping
migrate frontend to v2
notify partner clients
monitor v1 usage
sunset v1 after migration window
```

---

# 2. Example — Add Optional Field

## Change

Add `project.category` to response.

## Decision

```text
Backward-compatible if clients ignore unknown fields.
No new version required.
Documentation update required.
Contract test updated.
```

---

# 3. Example — Error Code Change

## Change

Replace `not_allowed` with `permission_denied`.

## Decision

```text
Breaking change if clients depend on error.code.
Keep old code in v1.
Use new code in v2.
Document migration.
```

---

# 4. Example — Webhook Versioning

## Context

External systems receive project approval events.

## Strategy

```text
webhook event type includes version
payload schema documented
new payload version introduced for breaking change
old webhook version supported during migration window
delivery failures monitored
```

Example:

```text
project.approved.v1
project.approved.v2
```

---

# 5. Final Principle

> Examples show that API versioning protects clients by making change explicit and migratable.
