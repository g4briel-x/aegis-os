## FILE: `playbooks/engineering/debug-production-issue/PLAYBOOK.md`

# Debug Production Issue — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured response to a production issue from initial signal to verified recovery and prevention.

---

# 2. Trigger

A production system is failing, degraded or producing unexpected behavior.

---

# 3. Inputs

Useful inputs include:

- incident summary;
- affected service;
- user reports;
- logs;
- metrics;
- traces;
- recent deployments;
- configuration changes;
- error messages;
- affected environment;
- rollback options.

---

# 4. Outputs

Expected outputs include:

- impact summary;
- diagnosis;
- likely root cause;
- mitigation plan;
- fix recommendation;
- verification steps;
- prevention actions;
- post-incident notes.

---

# 5. Execution Summary

```text
1. Assess impact
2. Stabilize the situation
3. Collect evidence
4. Identify recent changes
5. Build hypotheses
6. Isolate likely root cause
7. Mitigate or rollback if needed
8. Apply fix
9. Verify recovery
10. Document prevention actions
```

---

# 6. Completion Criteria

The Playbook is complete when:

- user impact is resolved or contained;
- the likely root cause is documented;
- recovery is verified;
- follow-up actions are assigned;
- prevention improvements are recorded.

---

# 7. Escalation or Fallback

Escalate when:

- customer impact is high;
- data integrity is at risk;
- security compromise is suspected;
- the issue cannot be isolated quickly;
- rollback is risky;
- required owner is unavailable.

---

# 8. Final Principle

> A production issue is not closed when the alert stops. It is closed when recovery is verified and recurrence risk is reduced.