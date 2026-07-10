## FILE: `playbooks/operations/run-postmortem-review/decision-points.md`

# Run Postmortem Review — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is a Full Postmortem Required?

```yaml
decision_point:
  question: Does this event require a full postmortem review?
  options:
    - yes
    - no
    - lightweight_review
  criteria:
    - user impact
    - severity
    - recurrence
    - security or data risk
    - release failure
    - business impact
  recommended_action:
    yes: run full postmortem.
    no: record short operational note.
    lightweight_review: capture timeline, cause and prevention action.
  fallback: run lightweight review if severity is unclear.
```

---

# 2. Decision Point — Is Root Cause Known?

```yaml
decision_point:
  question: Is the root cause supported by evidence?
  options:
    - yes
    - no
    - partially
  criteria:
    - logs support cause
    - metrics support cause
    - reproduction supports cause
    - fix addressed cause
    - alternative causes considered
  recommended_action:
    yes: document root cause and prevention actions.
    no: continue investigation before final report.
    partially: document confidence and unknowns.
  fallback: keep root cause as hypothesis until evidence improves.
```

---

# 3. Decision Point — Were Detection and Alerts Adequate?

```yaml
decision_point:
  question: Did monitoring detect the issue quickly and clearly?
  options:
    - yes
    - no
    - partially
  criteria:
    - alert timing
    - alert quality
    - owner routing
    - signal clarity
    - false positive or false negative behavior
  recommended_action:
    yes: keep alerting model.
    no: create monitoring improvement action.
    partially: tune threshold, message or routing.
  fallback: add explicit detection gap to prevention plan.
```

---

# 4. Decision Point — Is Leadership or Compliance Review Needed?

```yaml
decision_point:
  question: Does the incident require leadership, legal, compliance or customer-facing review?
  options:
    - yes
    - no
    - unclear
  criteria:
    - customer data impact
    - contractual obligation
    - security incident
    - extended downtime
    - major business impact
  recommended_action:
    yes: escalate to accountable owner.
    no: continue standard postmortem.
    unclear: document uncertainty and request owner decision.
  fallback: escalate when data, security or contractual risk is possible.
```

---

# 5. Decision Point — Are Follow-Up Actions Strong Enough?

```yaml
decision_point:
  question: Do the follow-up actions reduce recurrence risk in a verifiable way?
  options:
    - yes
    - no
    - partially
  criteria:
    - specific action
    - owner assigned
    - due date assigned
    - measurable verification
    - root cause addressed
  recommended_action:
    yes: publish and track.
    no: rewrite actions.
    partially: strengthen weak actions before closure.
  fallback: keep postmortem open until prevention plan is actionable.
```

---

# 6. Final Principle

> Postmortem decisions should favor evidence, learning and prevention over blame or premature closure.