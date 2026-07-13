## FILE: `templates/operations/runbook-template/examples/examples.md`

# Runbook Template — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Background Job Queue Delay

## Runbook Name

```text
Resolve Project Review Queue Delay
```

## Trigger Condition

```text
Project review jobs remain pending for more than 15 minutes or queue depth exceeds 500 jobs.
```

## Required Access

```text
Production monitoring dashboard
Worker logs
Queue management console
Read-only database access
```

## Procedure

```text
1. Check queue depth and job age.
2. Check worker health dashboard.
3. Review recent worker error logs.
4. Confirm whether external dependency failures are occurring.
5. Restart worker only if worker is unhealthy and restart policy allows it.
6. Validate queue depth decreases.
7. Notify support if customer-facing delay exceeds threshold.
```

## Validation

```text
Queue depth decreases for 10 consecutive minutes.
New jobs are processed successfully.
No increase in failed jobs.
```

---

# 2. Example — Failed Deployment Rollback

## Trigger Condition

```text
Error rate increases above rollback threshold within 10 minutes after deployment.
```

## Procedure

```text
1. Confirm error rate and affected endpoints.
2. Check release version.
3. Disable feature flag if applicable.
4. Roll back deployment to last known good version.
5. Validate health checks and core workflows.
6. Update incident channel.
```

---

# 3. Example — Security Escalation

## Trigger Condition

```text
Operator observes possible cross-tenant data access.
```

## Action

```text
Stop normal runbook execution.
Escalate to security lead immediately.
Preserve logs.
Do not delete or modify evidence.
```

---

# 4. Final Principle

> Examples show that runbooks must guide action, validation and escalation together.