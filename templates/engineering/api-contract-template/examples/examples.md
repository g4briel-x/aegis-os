## FILE: `templates/engineering/api-contract-template/examples/examples.md`

# API Contract Template — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Submit Project API

## Endpoint

```text
Method: POST
Path: /api/v1/projects/{{project_id}}/submit
Version: v1
Authentication Required: Yes
Authorization Required: Yes
```

## Authorization

```text
Required permission: project.submit
Tenant boundary: project.workspace_id must match current workspace
Ownership rule: user must be creator or workspace admin
```

## Request Body

```json
{
  "submission_note": "Ready for readiness review."
}
```

## Successful Response

```json
{
  "project_id": "prj_123",
  "status": "submitted",
  "submitted_at": "2026-07-13T12:00:00Z"
}
```

## Error Response

```json
{
  "error": {
    "code": "validation_failed",
    "message": "The project cannot be submitted because required documents are missing.",
    "details": [
      {
        "field": "documents.pitch_deck",
        "code": "required",
        "message": "Pitch deck is required before submission."
      }
    ],
    "request_id": "req_123",
    "documentation_url": null
  }
}
```

## Side Effects

```text
Project status changes to submitted.
Audit event project.submitted is created.
Reviewer assignment job may be queued.
Notification may be sent.
```

---

# 2. Example — List Projects API

## Endpoint

```text
Method: GET
Path: /api/v1/workspaces/{{workspace_id}}/projects
```

## Query Parameters

```text
status: optional
cursor: optional
limit: optional, max 100
```

## Response

```json
{
  "data": [
    {
      "id": "prj_123",
      "title": "Documentary Project",
      "status": "draft"
    }
  ],
  "pagination": {
    "next_cursor": null,
    "has_more": false
  }
}
```

---

# 3. Example — Permission Denied

```json
{
  "error": {
    "code": "permission_denied",
    "message": "You do not have permission to perform this action.",
    "details": [],
    "request_id": "req_456",
    "documentation_url": null
  }
}
```

---

# 4. Final Principle

> Examples show that API contracts must cover happy paths, failure paths and side effects.