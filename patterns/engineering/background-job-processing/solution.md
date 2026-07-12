## FILE: `patterns/engineering/background-job-processing/solution.md`

# Background Job Processing — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Solution Overview

Use background jobs for work that can execute asynchronously.

Core components:

```text
job producer
queue
worker
job payload schema
status tracking
retry policy
dead-letter handling
observability
runbook
```

---

# 2. Job Producer

The producer creates a job after validating the user action.

Producer responsibilities:

```text
authenticate user
authorize action
validate input
create operation record if needed
enqueue job with tenant and resource scope
return accepted or pending response
```

---

# 3. Job Payload Schema

Recommended payload:

```yaml
payload:
  job_id: job_123
  job_type: document_processing
  tenant_id: wsp_456
  resource_id: doc_789
  actor_id: usr_001
  operation_id: op_002
  idempotency_key: document_processing:doc_789:v1
  requested_at: 2026-07-12T10:00:00Z
```

---

# 4. Worker Execution Flow

Recommended worker flow:

```text
1. Receive job
2. Validate payload schema
3. Load tenant-scoped resource
4. Check resource state
5. Check idempotency
6. Execute operation
7. Persist result
8. Emit audit or domain event if needed
9. Mark job completed
10. Emit metrics and logs
```

---

# 5. Status Tracking

Track operation status when users or operators need visibility.

Example statuses:

```text
queued
processing
completed
failed
retrying
cancelled
expired
```

---

# 6. Retry and Dead-Letter Handling

Retry temporary failures.

Dead-letter after maximum attempts.

Dead-letter record should include:

```text
job id
job type
tenant id where safe
resource id
error category
attempt count
last failure time
next action
```

---

# 7. Scheduling

Scheduled jobs should define:

```text
schedule
owner
scope
expected duration
failure alert
overlap behavior
timezone
```

Avoid overlapping scheduled jobs unless explicitly safe.

---

# 8. Observability

Required signals:

```text
queue_depth
job_duration
job_failure_rate
retry_count
dead_letter_count
worker_heartbeat
oldest_job_age
```

Each alert should link to a runbook.

---

# 9. Final Principle

> The background job solution should make delayed work safe, visible and recoverable.
