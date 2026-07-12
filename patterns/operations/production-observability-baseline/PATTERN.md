## FILE: `patterns/operations/production-observability-baseline/PATTERN.md`

# Production Observability Baseline Pattern

Version: 0.1.0  
Status: Draft

---

# 1. Problem

A SaaS system needs to run reliably in production, but the team cannot manage what it cannot see.

Without observability, teams struggle to answer:

- is the system healthy;
- which customers are affected;
- which endpoint is failing;
- which background job is stuck;
- whether latency is increasing;
- whether a release introduced regressions;
- whether a business-critical workflow is broken.

---

# 2. Context

This Pattern applies to SaaS systems with:

```text
production users
HTTP APIs
frontend application
background workers
database dependencies
third-party services
authentication
file processing
billing or critical workflows
```

---

# 3. Forces

Key forces:

```text
visibility versus cost
signal versus noise
debuggability versus privacy
technical metrics versus business workflows
alert speed versus alert fatigue
baseline simplicity versus deep tracing
```

---

# 4. Recommended Baseline

A production-ready baseline should include:

```text
structured application logs
request id propagation
error tracking
API metrics
database metrics
background job metrics
health checks
release markers
dashboards
alerts for critical failures
business workflow indicators
```

---

# 5. Structured Logs

Logs should be structured and searchable.

Recommended fields:

```text
timestamp
level
service
environment
request_id
user_id when safe
tenant_id when safe
endpoint
method
status_code
duration_ms
error_code
event_name
```

Avoid logging secrets, tokens, passwords or full sensitive payloads.

---

# 6. Metrics

Metrics should cover system and product-critical behavior.

Core technical metrics:

```text
request_count
error_rate
latency_p95
latency_p99
database_query_time
job_failure_count
queue_depth
memory_usage
cpu_usage
dependency_error_rate
```

Workflow metrics:

```text
signup_completed
project_submitted
document_uploaded
payment_succeeded
review_completed
notification_sent
```

---

# 7. Dashboards

Create dashboards for:

```text
system health
API health
database health
background jobs
critical workflows
release impact
customer-impact view
security-sensitive events if needed
```

Dashboards should help answer what is broken, where and how severe it is.

---

# 8. Alerts

Alerts should be actionable.

Alert on:

```text
high error rate
critical endpoint failure
latency threshold breach
job queue stuck
payment failures
authentication failures spike
dependency outage
database saturation
workflow completion drop
```

Do not alert on noisy symptoms without a required action.

---

# 9. Incident Evidence

Observability should support incident response.

Capture:

```text
request ids
release version
deployment timestamp
error traces
affected tenants
affected endpoints
metric timeline
alert history
operator actions
```

---

# 10. Final Principle

> Observability is complete enough when operators can detect, diagnose and verify recovery of critical production failures.
