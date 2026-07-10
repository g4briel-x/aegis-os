## FILE: `playbooks/engineering/debug-production-issue/checklists.md`

# Debug Production Issue — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. Incident Intake Checklist

```text
[ ] Issue summary captured
[ ] Reporter identified
[ ] Time of first signal recorded
[ ] Affected service identified
[ ] Expected behavior documented
[ ] Actual behavior documented
[ ] User impact estimated
[ ] Severity estimated
```

---

# 2. Evidence Checklist

```text
[ ] Application logs reviewed
[ ] Error rate reviewed
[ ] Latency reviewed
[ ] Recent deployments reviewed
[ ] Configuration changes reviewed
[ ] Database indicators reviewed if relevant
[ ] Third-party dependency status reviewed
[ ] Feature flags reviewed if relevant
```

---

# 3. Mitigation Checklist

```text
[ ] Immediate user impact considered
[ ] Rollback option identified
[ ] Feature disablement considered
[ ] Data integrity risk reviewed
[ ] Security risk reviewed
[ ] Mitigation owner assigned
[ ] Communication needed identified
```

---

# 4. Root Cause Checklist

```text
[ ] Hypotheses documented
[ ] Evidence linked to hypothesis
[ ] Contradicting evidence considered
[ ] Recent changes analyzed
[ ] Root cause separated from symptom
[ ] Confidence level stated
```

---

# 5. Recovery Checklist

```text
[ ] Fix or mitigation applied
[ ] Error rate normalized
[ ] Latency normalized
[ ] Critical user flow tested
[ ] Logs checked after fix
[ ] Monitoring checked after fix
[ ] Stakeholders updated if needed
```

---

# 6. Prevention Checklist

```text
[ ] Regression test identified
[ ] Monitoring improvement identified
[ ] Logging improvement identified
[ ] Deployment safeguard identified
[ ] Documentation or runbook update identified
[ ] Owner assigned for follow-up actions
```

---

# 7. Final Principle

> Checklists keep production debugging disciplined when pressure is high.