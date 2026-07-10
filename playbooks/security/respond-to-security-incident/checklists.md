## FILE: `playbooks/security/respond-to-security-incident/checklists.md`

# Respond to Security Incident — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. Incident Intake Checklist

```text
[ ] Incident signal captured
[ ] Reporter or alert source identified
[ ] Time of first signal recorded
[ ] Affected system identified
[ ] Incident classification assigned
[ ] Initial severity estimated
[ ] Incident owner assigned
```

---

# 2. Evidence Checklist

```text
[ ] Logs preserved
[ ] Audit events preserved
[ ] Alert details preserved
[ ] Timestamps recorded
[ ] Affected accounts listed
[ ] Suspicious IPs or clients captured
[ ] Configuration snapshot captured if relevant
[ ] Evidence access restricted
```

---

# 3. Containment Checklist

```text
[ ] Active exposure assessed
[ ] Compromised accounts disabled if needed
[ ] Tokens revoked if needed
[ ] Secrets rotated if needed
[ ] Suspicious access blocked if needed
[ ] Vulnerable feature disabled if needed
[ ] Data write paths paused if needed
```

---

# 4. Investigation Checklist

```text
[ ] Entry point investigated
[ ] Affected assets identified
[ ] Affected users identified if possible
[ ] Root cause hypothesis documented
[ ] Supporting evidence linked
[ ] Unknowns documented
[ ] Specialist review requested if needed
```

---

# 5. Recovery Checklist

```text
[ ] Patch or configuration fix applied
[ ] Secrets rotation verified
[ ] Access permissions reviewed
[ ] Critical workflows tested
[ ] Monitoring checked
[ ] Suspicious activity stopped
[ ] Recovery status communicated
```

---

# 6. Prevention Checklist

```text
[ ] Root cause addressed
[ ] Monitoring improved
[ ] Logging improved if needed
[ ] Access controls strengthened
[ ] Secret scanning added or reviewed
[ ] Security tests added if possible
[ ] Post-incident review scheduled
[ ] Owners assigned for follow-up actions
```

---

# 7. Final Principle

> Security incident checklists keep the team disciplined when urgency and uncertainty are high.
