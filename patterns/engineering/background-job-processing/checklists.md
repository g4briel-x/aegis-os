## FILE: `patterns/engineering/background-job-processing/checklists.md`

# Background Job Processing — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Context Fit Checklist

```text
[ ] Work is slow or blocking
[ ] Delayed execution is acceptable
[ ] Retry is useful
[ ] External dependency is involved
[ ] Queue or worker infrastructure exists
[ ] Job status can be monitored
```

---

# 2. Job Design Checklist

```text
[ ] Job type is named
[ ] Payload schema is defined
[ ] Tenant or scope id is included
[ ] Resource id is included
[ ] Idempotency key is defined
[ ] Timeout is defined
[ ] Owner is assigned
```

---

# 3. Retry Checklist

```text
[ ] Retryable errors defined
[ ] Non-retryable errors defined
[ ] Max attempts defined
[ ] Backoff strategy defined
[ ] Dead-letter behavior defined
[ ] Duplicate side effects prevented
```

---

# 4. Security Checklist

```text
[ ] Payload contains no secrets
[ ] Tenant context is validated
[ ] Resource ownership is checked
[ ] Sensitive actions are audited
[ ] Worker permissions are limited
[ ] Logs avoid sensitive data
```

---

# 5. Observability Checklist

```text
[ ] Queue depth monitored
[ ] Job failure rate monitored
[ ] Retry count monitored
[ ] Dead-letter count monitored
[ ] Worker heartbeat monitored
[ ] Oldest job age monitored
[ ] Runbook exists for stuck queue
```

---

# 6. Test Checklist

```text
[ ] Successful job tested
[ ] Retry behavior tested
[ ] Non-retryable failure tested
[ ] Idempotency tested
[ ] Dead-letter behavior tested
[ ] Tenant mismatch tested
[ ] Duplicate enqueue tested
```

---

# 7. Final Principle

> Background job checklists should prove that async work is safe under failure.
