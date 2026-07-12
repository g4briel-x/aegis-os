## FILE: `patterns/operations/production-observability-baseline/examples/examples.md`

# Production Observability Baseline — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Financing SaaS

## Context

A platform allows creators to submit financing-ready project packages.

## Critical Workflows

```text
creator signup
project creation
document upload
project submission
review assignment
review feedback
notification delivery
```

## Metrics

```text
project_submitted_count
document_upload_failure_rate
review_assignment_latency
notification_failed_count
api_error_rate
api_latency_p95
```

## Alerts

```text
document upload failures above threshold
project submission endpoint error rate high
review assignment job stuck
notification provider outage
```

---

# 2. Example — Background Job Monitoring

## Workflow

Project readiness reports are generated asynchronously.

## Metrics

```text
readiness_report_queue_depth
readiness_report_job_failure_rate
readiness_report_generation_duration
```

## Alert

```text
Queue depth above 100 for 15 minutes.
```

## Action

```text
Open runbook for background worker recovery.
Check recent release marker.
Inspect error logs by request_id or job_id.
```

---

# 3. Example — API Error Correlation

## User Report

A customer says project submission failed.

## Investigation Path

```text
Collect request_id from frontend error.
Search logs by request_id.
Find error_code.
Check release marker.
Check affected tenant.
Review related metric spike.
Verify fix by tracking submission success metric.
```

---

# 4. Example — Release Impact Dashboard

## Dashboard Sections

```text
deployment marker
error rate before and after release
latency before and after release
critical workflow completion
new exception types
feature flag changes
```

---

# 5. Final Principle

> Examples show that observability should connect customer symptoms to system evidence.
