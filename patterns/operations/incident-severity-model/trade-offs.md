## FILE: `patterns/operations/incident-severity-model/trade-offs.md`

# Incident Severity Model — Trade-Offs

Version: 0.1.0  
Status: Draft

---

# 1. Benefits

This Pattern improves:

```text
response consistency
customer communication
engineering prioritization
support alignment
security escalation
postmortem quality
reliability governance
```

---

# 2. Costs

This Pattern adds:

```text
process overhead
classification debate
communication expectations
postmortem work
on-call or ownership pressure
review cadence
```

---

# 3. Under-Classification Risk

If severity is too low:

```text
response is delayed
customers lose trust
security issues expand
data risk increases
communication comes too late
```

Mitigation:

```text
classify higher when uncertain
downgrade later with evidence
include security and data criteria
```

---

# 4. Over-Classification Risk

If severity is too high:

```text
alert fatigue grows
teams burn out
stakeholders stop trusting alerts
normal bugs interrupt critical work
```

Mitigation:

```text
define objective impact criteria
review severity after incident
track false-positive severity patterns
```

---

# 5. Communication Trade-Off

Early communication can be incomplete, but delayed communication can damage trust.

Mitigation:

```text
communicate known impact
avoid speculation
state next update time
correct information transparently
```

---

# 6. Main Risks

Key risks:

```text
severity levels ignored
security criteria missing
no incident owner
no communication owner
postmortems become blame sessions
repeated incidents not escalated
```

---

# 7. Mitigations

Mitigate with:

- severity decision table;
- role assignments;
- escalation rules;
- communication templates;
- postmortem template;
- incident metrics review.

---

# 8. Final Principle

> Severity modeling trades process discipline for faster, calmer and safer incident response.
