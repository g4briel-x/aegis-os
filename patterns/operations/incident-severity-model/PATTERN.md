## FILE: `patterns/operations/incident-severity-model/PATTERN.md`

# Incident Severity Model Pattern

Version: 0.1.0  
Status: Draft

---

# 1. Problem

A SaaS team needs a consistent way to classify production incidents.

Without a severity model:

- engineers disagree about urgency;
- support cannot set expectations;
- executives are notified too late or too often;
- security issues may be minimized;
- customers receive inconsistent communication;
- postmortems lack comparable data.

---

# 2. Context

This Pattern applies to SaaS products with:

```text
production users
critical workflows
customer support
monitoring alerts
deployment risk
security events
billing workflows
background jobs
external dependencies
```

---

# 3. Forces

Key forces:

```text
speed versus accuracy
high urgency versus alert fatigue
customer transparency versus premature communication
technical symptoms versus business impact
security caution versus operational continuity
response cost versus incident risk
```

---

# 4. Recommended Severity Levels

Use four severity levels:

```text
SEV1 — Critical
SEV2 — High
SEV3 — Medium
SEV4 — Low
```

Optional:

```text
SEV0 — Crisis
```

Use SEV0 only for rare existential, legal, security or full-business outage events.

---

# 5. Severity Definitions

## SEV1 — Critical

```text
Major customer impact.
Core product unavailable or critical workflow broken.
No acceptable workaround.
Immediate response required.
```

Examples:

```text
production API down
login unavailable for most users
data loss risk
billing failure affecting all customers
active security breach
cross-tenant data exposure
```

## SEV2 — High

```text
Significant customer impact.
Important workflow degraded or unavailable for a subset of users.
Workaround may exist.
Fast response required.
```

Examples:

```text
document upload failing for many users
background job backlog blocking submissions
payment failures for a subset
major latency degradation
third-party dependency outage
```

## SEV3 — Medium

```text
Limited customer impact.
Non-critical workflow affected or degraded.
Workaround exists.
Normal urgent response.
```

Examples:

```text
dashboard chart incorrect
notification delays
admin-only issue
minor integration sync problem
single tenant issue without data loss
```

## SEV4 — Low

```text
Minimal customer impact.
Cosmetic issue, minor defect or low-risk operational issue.
Handled through normal backlog.
```

Examples:

```text
minor UI bug
documentation mismatch
non-critical analytics delay
low-priority alert requiring tuning
```

---

# 6. Classification Criteria

Classify by:

```text
customer impact
number of affected users or tenants
critical workflow impact
data integrity risk
security or privacy exposure
revenue impact
availability impact
workaround availability
duration
regulatory or contractual risk
```

When uncertain, classify higher until impact is understood.

---

# 7. Response Expectations

Each severity should define:

```text
acknowledgement time
incident owner
communication channel
update frequency
escalation rule
postmortem requirement
```

Example:

```text
SEV1:
  acknowledge immediately
  assign incident commander
  update every 15-30 minutes
  customer communication required if visible
  postmortem required
```

---

# 8. Severity Changes

Severity can change during investigation.

Rules:

```text
upgrade if impact is broader than expected
upgrade if security or data risk appears
downgrade if impact is contained
downgrade if workaround is confirmed
record reason for severity change
```

---

# 9. Final Principle

> Severity is a decision tool for coordinated response, not a label for blame.
