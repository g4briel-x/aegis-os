## FILE: `patterns/operations/incident-severity-model/solution.md`

# Incident Severity Model — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Solution Overview

Define incident severity as an operational contract.

Core components:

```text
severity levels
impact criteria
response times
roles
escalation rules
communication policy
postmortem rules
review cadence
```

---

# 2. Severity Table

Recommended severity table:

```text
SEV1 Critical:
  Core system or critical workflow down.
  Broad customer impact, data risk or active security issue.
  Immediate response and postmortem required.

SEV2 High:
  Significant degradation or subset impact.
  Fast response and incident review required.

SEV3 Medium:
  Limited impact with workaround.
  Track and resolve through priority process.

SEV4 Low:
  Minimal impact.
  Handle through normal backlog.
```

---

# 3. Response Times

Example response expectations:

```text
SEV1:
  acknowledge: immediate
  owner: incident commander
  updates: every 15-30 minutes
  postmortem: required

SEV2:
  acknowledge: within 30 minutes
  owner: technical lead
  updates: every 60 minutes
  postmortem: required if customer-visible

SEV3:
  acknowledge: same business day
  owner: team owner
  updates: as needed
  postmortem: optional

SEV4:
  acknowledge: normal backlog
  owner: backlog owner
  updates: normal process
  postmortem: not required
```

---

# 4. Incident Roles

Define roles:

```text
incident commander
technical lead
communications owner
support liaison
security lead if relevant
executive sponsor if needed
```

For small teams, one person may hold multiple roles, but the responsibilities should still be explicit.

---

# 5. Escalation Rules

Escalate when:

```text
impact expands
customer data may be exposed
incident exceeds expected duration
workaround fails
critical customer is affected
legal or compliance risk appears
team lacks required expertise
```

---

# 6. Communication Policy

Define communication by severity.

Recommended:

```text
SEV1:
  internal incident channel
  support notification
  customer status update if visible
  executive notification if broad impact

SEV2:
  internal incident channel
  support notification
  customer communication if affected

SEV3:
  team channel
  support note if customers report it

SEV4:
  backlog or normal issue tracking
```

---

# 7. Postmortem Rules

Postmortem required for:

```text
SEV1
security incidents
data integrity incidents
repeated SEV2
customer-visible SEV2 above threshold duration
incidents causing SLA breach
```

Postmortem should include:

```text
timeline
impact
root cause
detection gap
response gap
corrective actions
owners
due dates
```

---

# 8. Review Cadence

Review incident data monthly or quarterly.

Review:

```text
incident count by severity
mean time to detect
mean time to acknowledge
mean time to resolve
repeat incidents
alert quality
postmortem action completion
```

---

# 9. Final Principle

> The solution should turn incident chaos into a predictable response system.