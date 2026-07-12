## FILE: `patterns/operations/production-observability-baseline/trade-offs.md`

# Production Observability Baseline — Trade-Offs

Version: 0.1.0  
Status: Draft

---

# 1. Benefits

This Pattern improves:

```text
incident detection
debugging speed
customer support
release confidence
reliability governance
postmortem quality
operational maturity
```

---

# 2. Costs

This Pattern adds:

```text
tooling cost
setup time
dashboard maintenance
alert tuning
log storage volume
privacy review
operational ownership
```

---

# 3. Signal Versus Noise

More telemetry is not always better.

Good observability prioritizes:

```text
critical workflows
actionable alerts
correlated evidence
clear ownership
stable dashboards
```

Avoid:

```text
vanity metrics
unowned dashboards
duplicate alerts
logs without context
alerts without runbooks
```

---

# 4. Privacy Trade-Off

Logs help debugging but may expose sensitive information.

Mitigation:

```text
redaction
field allowlists
access controls
retention policy
privacy review
no secret logging
```

---

# 5. Cost Trade-Off

High-cardinality metrics and verbose logs can become expensive.

Mitigation:

```text
sample where appropriate
control log levels
use retention tiers
avoid unnecessary labels
measure dashboard usage
```

---

# 6. Main Risks

Key risks:

```text
alert fatigue
missing request correlation
sensitive data in logs
dashboards no one uses
workflow failures not monitored
background jobs invisible
no runbook attached to alert
```

---

# 7. Mitigations

Mitigate with:

- observability review before release;
- alert ownership;
- dashboard ownership;
- log schema standard;
- request id propagation;
- workflow metrics;
- runbook links.

---

# 8. Final Principle

> Observability should create confidence through useful signals, not noise through excessive instrumentation.
