## FILE: `skills/engineering/senior-debugger/checklists.md`

# Senior Debugger — Checklists

Version: 0.2.0  
Status: Premium Draft

---

# 1. Debugging Intake Checklist

```text
[ ] Symptom captured
[ ] Expected behavior captured
[ ] Actual behavior captured
[ ] Error message captured
[ ] Environment identified
[ ] Recent changes identified
[ ] Reproduction path identified if available
[ ] Impact understood
```

---

# 2. Root Cause Checklist

```text
[ ] Evidence reviewed
[ ] Hypotheses listed
[ ] Most likely cause identified
[ ] Alternative causes considered
[ ] Symptom separated from root cause
[ ] Contributing factors documented
[ ] Unknowns stated
```

---

# 3. Fix Checklist

```text
[ ] Fix targets root cause
[ ] Fix is minimal where possible
[ ] Side effects considered
[ ] Security impact considered
[ ] Data impact considered
[ ] Regression risk considered
[ ] Rollback considered where relevant
```

---

# 4. Verification Checklist

```text
[ ] Verification steps defined
[ ] Expected result defined
[ ] Regression test suggested
[ ] Logs or monitoring considered
[ ] User-facing behavior confirmed
[ ] Edge cases considered
```

---

# 5. Production Incident Checklist

```text
[ ] Impact assessed
[ ] Affected services identified
[ ] Recent deploys reviewed
[ ] Logs reviewed
[ ] Metrics reviewed
[ ] Mitigation considered
[ ] Escalation path considered
[ ] Prevention action defined
```

---

# 6. 4-Pass Validation Checklist

```text
[ ] Pass 1 completed — symptom, error and context
[ ] Pass 2 completed — hypothesis and root cause
[ ] Pass 3 completed — fix safety and regression
[ ] Pass 4 completed — verification and prevention
[ ] Weaknesses corrected or documented
```

---

# 7. Final Principle

> Debugging checklists protect the process from premature conclusions.