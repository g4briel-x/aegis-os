## FILE: `playbooks/engineering/debug-production-issue/decision-points.md`

# Debug Production Issue — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is Production Impact Confirmed?

```yaml
decision_point:
  question: Is the issue affecting production users or business-critical workflows?
  options:
    - yes
    - no
    - unknown
  criteria:
    - user reports
    - monitoring alerts
    - failed transactions
    - service health
  recommended_action:
    yes: Treat as production incident and continue.
    no: Continue as standard debugging task.
    unknown: Collect more evidence from logs, metrics and support channels.
  fallback: Escalate if evidence cannot be collected quickly.
```

---

# 2. Decision Point — Is Immediate Rollback Safer?

```yaml
decision_point:
  question: Is rollback safer than investigating live?
  options:
    - rollback
    - investigate_first
    - escalate
  criteria:
    - severity
    - rollback availability
    - data migration risk
    - user impact
    - confidence in recent deployment as cause
  recommended_action:
    rollback: Use when recent deployment is likely cause and rollback is safe.
    investigate_first: Use when rollback may create more risk.
    escalate: Use when data, security or business impact is high.
  fallback: Contain impact with feature flag or traffic control if rollback is unsafe.
```

---

# 3. Decision Point — Is Data Integrity at Risk?

```yaml
decision_point:
  question: Could the issue corrupt, delete or expose data?
  options:
    - yes
    - no
    - unknown
  criteria:
    - database errors
    - migration activity
    - failed writes
    - inconsistent records
    - security indicators
  recommended_action:
    yes: Stop risky writes, preserve evidence and escalate.
    no: Continue normal mitigation.
    unknown: Investigate database and audit logs before applying destructive fixes.
  fallback: Pause affected write paths until integrity is understood.
```

---

# 4. Decision Point — Is Security Compromise Suspected?

```yaml
decision_point:
  question: Is there evidence of unauthorized access, abuse or compromise?
  options:
    - yes
    - no
    - unknown
  criteria:
    - suspicious logs
    - unexpected privilege changes
    - credential exposure
    - abnormal traffic
    - data access anomalies
  recommended_action:
    yes: Switch to security incident response.
    no: Continue production debugging.
    unknown: Involve security reviewer and preserve evidence.
  fallback: Treat as security-sensitive until ruled out.
```

---

# 5. Final Principle

> Decision points prevent the team from applying the same response to different risk situations.