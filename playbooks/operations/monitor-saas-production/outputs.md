## FILE: `playbooks/operations/monitor-saas-production/outputs.md`

# Monitor SaaS Production — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. Production Health Summary

Purpose:

Summarize current production state.

Required sections:

```text
Environment:
Monitoring window:
Overall status:
Critical workflows:
Major signals:
Decision:
```

---

# 2. Signal Review

Purpose:

Document reviewed operational signals.

Required sections:

```text
Signal:
Baseline:
Observed value:
Status:
Notes:
```

---

# 3. Alert Review

Purpose:

Evaluate alerts and their usefulness.

Required sections:

```text
Alert:
Trigger:
Severity:
Owner:
Action taken:
Alert quality:
```

---

# 4. Anomaly Finding

Purpose:

Record abnormal production behavior.

Required sections:

```text
Anomaly:
Affected area:
Evidence:
Severity:
Recommended action:
Owner:
```

---

# 5. Escalation Decision

Purpose:

Record whether issue response is needed.

Required sections:

```text
Decision:
Reason:
Playbook to run:
Owner:
Timing:
```

---

# 6. Monitoring Improvement Recommendation

Purpose:

Improve future detection.

Required sections:

```text
Gap:
Impact:
Improvement:
Owner:
Priority:
```

---

# 7. Final Principle

> Monitoring outputs should help the team understand production health and decide what to do next.