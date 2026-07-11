## FILE: `patterns/operations/feature-flag-rollout/examples/examples.md`

# Feature Flag Rollout — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Project Submission V2

## Context

A SaaS platform introduces a new project submission flow for creators.

## Flag

```text
project_submission_v2
```

## Rollout

```text
internal staff
10 selected creators
25% of beta creators
100% of creators
cleanup
```

## Monitoring

```text
submission completion rate
form validation errors
file upload failures
support requests
API error rate
```

---

# 2. Example — New Billing Page

## Context

A new billing interface is released to workspace owners.

## Rollout

```text
internal only
5% of owners
25% of owners
all owners
```

## Rollback Trigger

```text
billing update errors
payment provider errors
support spike
```

---

# 3. Example — AI Report Generator

## Context

An AI-powered report generator has variable API cost.

## Rollout

```text
paid beta customers only
usage limit enabled
cost monitoring active
```

## Monitoring

```text
AI API cost
generation failures
latency
user satisfaction
```

---

# 4. Example — Kill Switch

## Context

A risky background job can overload the database.

## Flag

```text
background_job_processing_enabled
```

## Rollback

```text
set flag off
confirm queue stops processing
monitor database recovery
investigate root cause
```

---

# 5. Final Principle

> Examples show that rollout control is strongest when flag, audience, signal and rollback are designed together.
