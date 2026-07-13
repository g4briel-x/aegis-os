## FILE: `templates/engineering/test-plan-template/examples/examples.md`

# Test Plan Template — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Project Submission Workflow

## Change Name

```text
Project Submission Workflow
```

## Summary

```text
This test plan validates that creators can submit complete audiovisual project packages for readiness review and that incomplete or unauthorized submissions are safely blocked.
```

## Functional Test Case

```text
TC-FUNC-001:
Given a creator has completed all required project fields and uploaded required documents
When the creator submits the project
Then the project status changes to submitted and a project.submitted audit event is created.
```

## Negative Test Case

```text
TC-NEG-001:
Given a project is missing a pitch deck
When the creator attempts to submit it
Then the system blocks submission and returns validation_failed.
```

## Security Test Case

```text
TC-SEC-001:
Given a user belongs to workspace A
When the user attempts to submit a project from workspace B
Then access is denied and no project data from workspace B is returned.
```

---

# 2. Example — API Contract Test

```text
Endpoint: POST /api/v1/projects/{{project_id}}/submit
Expected success status: 200
Expected validation error: 400 validation_failed
Expected unauthorized error: 401 authentication_required
Expected forbidden error: 403 permission_denied
```

---

# 3. Example — Background Job Test

```text
Given a project is submitted
When reviewer assignment is queued
Then the background job includes workspace_id and project_id
And the worker validates project workspace ownership before processing.
```

---

# 4. Final Principle

> Examples show that good test plans cover success, failure, authorization and operational behavior.