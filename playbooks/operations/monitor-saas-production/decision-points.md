## FILE: `playbooks/operations/monitor-saas-production/decision-points.md`

# Monitor SaaS Production — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is User Impact Confirmed?

```yaml
decision_point:
  question: Is production behavior affecting real users or critical workflows?
  options:
    - yes
    - no
    - unknown
  criteria:
    - support reports
    - failed transactions
    - critical workflow failures
    - error spikes
    - monitoring alerts
  recommended_action:
    yes: escalate to production incident workflow.
    no: continue monitoring and document finding.
    unknown: collect more evidence from logs, metrics and support channels.
  fallback: treat critical workflow failures as user impact until ruled out.
```

---

# 2. Decision Point — Is the Signal Normal or Anomalous?

```yaml
decision_point:
  question: Is the observed signal within expected baseline?
  options:
    - normal
    - anomalous
    - unclear
  criteria:
    - historical baseline
    - deployment timing
    - traffic pattern
    - alert threshold
    - user reports
  recommended_action:
    normal: record status and continue.
    anomalous: investigate and classify severity.
    unclear: monitor longer or compare against recent baseline.
  fallback: create investigation task if signal affects critical area.
```

---

# 3. Decision Point — Is Security Review Needed?

```yaml
decision_point:
  question: Does the signal suggest abuse, unauthorized access or compromise?
  options:
    - yes
    - no
    - unclear
  criteria:
    - suspicious login attempts
    - unusual authorization failures
    - abnormal traffic
    - data access anomalies
    - credential exposure signs
  recommended_action:
    yes: escalate to security review or security incident response.
    no: continue operational monitoring.
    unclear: preserve evidence and involve Security Engineer Skill.
  fallback: treat as security-sensitive until reviewed.
```

---

# 4. Decision Point — Is Alerting Accurate?

```yaml
decision_point:
  question: Did the alert provide useful, timely and actionable information?
  options:
    - yes
    - no
    - partially
  criteria:
    - alert triggered at useful threshold
    - alert includes context
    - alert maps to owner
    - alert avoids noise
    - alert includes next action
  recommended_action:
    yes: keep alert.
    no: tune or replace alert.
    partially: improve alert message, threshold or routing.
  fallback: document monitoring improvement task.
```

---

# 5. Decision Point — Should Incident Response Start?

```yaml
decision_point:
  question: Should the team start incident response?
  options:
    - yes
    - no
    - watch
  criteria:
    - user impact
    - severity
    - duration
    - data risk
    - security risk
    - business impact
  recommended_action:
    yes: start debug production issue playbook.
    no: record normal health status.
    watch: define monitoring window and owner.
  fallback: escalate if critical signals worsen.
```

---

# 6. Final Principle

> Monitoring decisions should be conservative when user impact, data risk or security risk is unclear.