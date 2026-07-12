## FILE: `patterns/engineering/background-job-processing/README.md`

# Background Job Processing Pattern

Version: 0.1.0  
Status: Draft  
Domain: Engineering  
Category: Asynchronous Processing

---

# 1. Purpose

The Background Job Processing Pattern defines a reusable model for running asynchronous work safely in SaaS applications.

It helps teams process slow, expensive, scheduled, retryable or external-service-dependent operations outside the main request path while preserving reliability, observability, idempotency and tenant safety.

---

# 2. Problem

SaaS applications often perform long-running work directly inside API requests.

Common failures:

```text
slow user requests
timeouts
duplicate processing
lost jobs
unsafe retries
silent failures
missing tenant context
no dead-letter handling
no visibility into queue health
```

---

# 3. Recommended Solution

Move long-running or retryable work into background jobs with explicit processing rules.

A good job should define:

```text
job name
payload schema
tenant context
idempotency key
retry policy
timeout
failure handling
observability signals
dead-letter behavior
ownership
```

---

# 4. Recommended When

Use this Pattern when:

- work is slow or blocking;
- external APIs are involved;
- emails or notifications must be sent;
- files must be processed;
- reports must be generated;
- AI tasks are expensive or long-running;
- scheduled jobs are needed;
- retries are necessary.

---

# 5. Avoid When

Avoid background jobs when:

- the action must be completed synchronously;
- the work is extremely fast and safe;
- delayed execution would confuse users;
- there is no retry or failure plan;
- job execution has no observability;
- the system cannot handle eventual consistency.

---

# 6. Related Assets

```text
Related skills:
engineering.senior-developer
engineering.software-architect
engineering.senior-debugger
infrastructure.devops-engineer
security.security-engineer

Related playbooks:
engineering.debug-production-issue
operations.monitor-saas-production
operations.create-runbook
infrastructure.deploy-saas-application
engineering.write-test-plan

Related patterns:
operations.production-observability-baseline
security.tenant-data-isolation
security.audit-logging-traceability
operations.feature-flag-rollout
```

---

# 7. Final Principle

> A background job is production code with delayed execution, not a place to hide unreliable work.
