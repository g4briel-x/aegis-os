## FILE: `patterns/operations/production-observability-baseline/solution.md`

# Production Observability Baseline — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Solution Overview

Create a baseline before production launch.

Baseline components:

```text
logging
metrics
tracing where useful
error tracking
health checks
dashboards
alerts
workflow monitoring
release markers
runbook links
```

---

# 2. Structured Log Schema

Recommended log schema:

```yaml
log_event:
  timestamp: 2026-07-12T10:00:00Z
  level: info
  service: api
  environment: production
  request_id: req_123
  tenant_id: wsp_456
  user_id: usr_789
  event: project.submitted
  endpoint: POST /projects/:id/submit
  status_code: 200
  duration_ms: 142
```

Sensitive data must be excluded or redacted.

---

# 3. Request Correlation

Every request should receive or generate a request id.

Propagate it through:

```text
API response
logs
error tracking
background jobs
third-party calls where possible
support tickets
audit events where appropriate
```

---

# 4. Metric Catalog

Define a metric catalog.

System metrics:

```text
api_request_count
api_error_rate
api_latency_p95
api_latency_p99
database_latency
database_connection_count
queue_depth
job_failure_rate
dependency_failure_rate
```

Workflow metrics:

```text
signup_completed_count
project_created_count
document_uploaded_count
project_submitted_count
review_completed_count
payment_succeeded_count
notification_failed_count
```

---

# 5. Dashboard Map

Minimum dashboards:

```text
Production Overview
API Health
Database Health
Background Jobs
Critical Workflows
Release Impact
Customer Impact
Security and Audit Events if needed
```

Each dashboard should define owner and review cadence.

---

# 6. Alert Rules

Alert rules should include:

```text
condition
threshold
duration
severity
owner
runbook
notification channel
expected action
```

Example:

```yaml
alert:
  name: api_error_rate_high
  condition: api_error_rate > 5%
  duration: 5m
  severity: high
  owner: operations
  runbook: operations/create-runbook
```

---

# 7. Health Checks

Health checks should include:

```text
application process health
database connectivity
critical dependency readiness
background worker heartbeat
storage access if critical
```

Avoid health checks that only prove the process is alive while the product is unusable.

---

# 8. Release Markers

Every deployment should mark observability timelines.

Capture:

```text
version
commit
deployment time
environment
release owner
feature flags changed
migration status
```

---

# 9. Privacy and Security

Observability must avoid leaking sensitive data.

Rules:

```text
redact secrets
avoid full request bodies
avoid private document contents
limit access to logs
define retention policy
audit access if needed
```

---

# 10. Final Principle

> The observability solution should connect symptoms, causes, affected users and recovery evidence.
