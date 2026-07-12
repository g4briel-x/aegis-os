## FILE: `patterns/engineering/background-job-processing/context.md`

# Background Job Processing — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern fits SaaS systems that need work to happen outside the main request path.

Typical contexts:

```text
file upload processing
document parsing
email delivery
notification delivery
report generation
AI generation
payment webhooks
integration sync
scheduled cleanup
analytics aggregation
```

---

# 2. Product Context

Use this Pattern when users expect:

- fast request response;
- progress tracking;
- notification after completion;
- retry after temporary failure;
- reliable processing of submitted work.

---

# 3. Technical Context

The Pattern applies when the system has:

```text
API server
worker process
queue or broker
database
object storage
external providers
scheduler
monitoring system
```

---

# 4. Operational Context

Operators need to know:

- whether workers are alive;
- whether queues are stuck;
- whether jobs are failing;
- whether retries are increasing;
- whether tenants are affected;
- whether external providers are causing failures.

---

# 5. Security Context

Background jobs must preserve:

```text
tenant isolation
permission boundaries
safe payload handling
secret management
audit logging for sensitive actions
```

Workers should not become privileged bypass paths.

---

# 6. Warning Signs

Background processing is weak when:

- jobs have no idempotency key;
- failed jobs disappear silently;
- retries create duplicate side effects;
- payloads include secrets;
- tenant context is missing;
- workers have no dashboards;
- dead-letter queues are ignored;
- users cannot understand job status.

---

# 7. Final Principle

> Background job context must include user expectations, system reliability and operational recovery.
