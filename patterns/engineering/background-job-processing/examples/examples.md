## FILE: `patterns/engineering/background-job-processing/examples/examples.md`

# Background Job Processing — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Project Readiness Report

## Context

A SaaS platform generates a readiness report after a creator submits a project for financing review.

## Job

```text
generate_project_readiness_report
```

## Payload

```yaml
job_type: generate_project_readiness_report
tenant_id: wsp_123
project_id: prj_456
operation_id: op_789
idempotency_key: readiness_report:prj_456:v1
```

## Processing

```text
load project with workspace scope
verify project is submitted
generate report
save report
notify creator
audit report generation
```

---

# 2. Example — Document Processing

## Context

A user uploads a pitch deck.

## Job

```text
process_uploaded_document
```

## Processing

```text
scan file
extract metadata
generate preview
update document status
notify user if processing fails
```

---

# 3. Example — Notification Delivery

## Context

A reviewer is assigned to a project.

## Job

```text
send_reviewer_assignment_notification
```

## Idempotency Rule

```text
Do not send more than one assignment notification for the same reviewer and project assignment event.
```

---

# 4. Example — Dead-Letter Handling

## Failure

A third-party provider fails after maximum retries.

## Dead-Letter Record

```yaml
job_type: sync_external_provider
tenant_id: wsp_123
resource_id: integration_456
attempts: 5
last_error_category: provider_unavailable
next_action: operator_review
```

---

# 5. Final Principle

> Examples show that background jobs must carry enough context to execute safely and recover when they fail.
