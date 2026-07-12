## FILE: `patterns/engineering/background-job-processing/PATTERN.md`

# Background Job Processing Pattern

Version: 0.1.0  
Status: Draft

---

# 1. Problem

A SaaS system needs to process work that should not block the user request.

Examples:

- sending email;
- processing uploaded files;
- generating reports;
- syncing integrations;
- calling AI providers;
- recalculating analytics;
- running scheduled maintenance;
- exporting data.

If this work is done inside the request path, users experience slow responses, failures become hard to recover and retries can create duplicated side effects.

---

# 2. Context

This Pattern applies when the system uses:

```text
job queues
workers
scheduled tasks
message brokers
async workflows
external providers
long-running operations
```

It is especially useful for SaaS products with document processing, notifications, analytics, billing, AI features or integrations.

---

# 3. Forces

Key forces:

```text
responsiveness versus consistency
retry safety versus duplicate side effects
queue simplicity versus workflow complexity
throughput versus provider limits
observability versus operational cost
tenant safety versus background autonomy
```

---

# 4. Recommended Model

Use a job model with:

```text
job type
payload schema
tenant or scope id
resource id
idempotency key
priority
timeout
retry policy
dead-letter behavior
status tracking
logs and metrics
```

Example:

```yaml
job:
  type: generate_project_readiness_report
  tenant_id: wsp_123
  project_id: prj_456
  idempotency_key: readiness_report:prj_456:v1
  priority: normal
  timeout_seconds: 300
  max_retries: 3
```

---

# 5. Job Payload Rules

Job payloads should include stable identifiers, not full mutable objects.

Good:

```text
tenant_id
resource_id
user_id
operation_id
idempotency_key
```

Avoid:

```text
full document contents
large payloads
secrets
stale business state
unvalidated external data
```

Workers should reload current state and validate scope before processing.

---

# 6. Idempotency

Jobs should be safe to retry.

Idempotency strategies:

```text
idempotency key
unique operation record
status transition guard
deduplication table
provider idempotency header
check-before-write
```

Example:

```text
Do not send the same billing receipt twice.
Do not generate duplicate exports for the same operation.
Do not create duplicate notifications for one event.
```

---

# 7. Retry Policy

Retries should be intentional.

Define:

```text
retryable errors
non-retryable errors
maximum attempts
backoff strategy
timeout
dead-letter behavior
alert threshold
```

Examples:

```text
network timeout: retry
provider 429: retry with backoff
validation failure: do not retry
permission failure: do not retry
missing resource: do not retry unless eventual consistency is expected
```

---

# 8. Observability

Track queue and job health.

Minimum signals:

```text
queue_depth
job_started_count
job_completed_count
job_failed_count
job_retry_count
job_duration
dead_letter_count
oldest_job_age
worker_heartbeat
```

Logs should include job id, job type, tenant id where safe and request id or correlation id when available.

---

# 9. Final Principle

> Background jobs should be designed as reliable workflows with explicit failure behavior.
