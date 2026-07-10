## FILE: `playbooks/operations/run-postmortem-review/PLAYBOOK.md`

# Run Postmortem Review — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured post-incident review after an operational, security, release or delivery failure.

---

# 2. Trigger

An incident, outage, failed deployment, degraded workflow, security event or major delivery failure has been resolved or contained.

---

# 3. Inputs

Useful inputs include:

- incident summary;
- severity;
- affected services;
- affected users;
- timeline;
- logs;
- alerts;
- deployment history;
- mitigation actions;
- recovery notes;
- communication records;
- support reports;
- root cause notes.

---

# 4. Outputs

Expected outputs include:

- postmortem report;
- incident timeline;
- impact summary;
- root cause analysis;
- contributing factor list;
- response review;
- detection gap list;
- prevention action plan;
- follow-up tracker.

---

# 5. Execution Summary

```text
1. Define review scope
2. Collect incident facts and evidence
3. Reconstruct timeline
4. Summarize user and business impact
5. Identify root cause and contributing factors
6. Review detection and response effectiveness
7. Identify prevention actions
8. Assign owners and deadlines
9. Publish postmortem report
10. Track follow-up actions to closure
```

---

# 6. Completion Criteria

The Playbook is complete when:

- incident facts are documented;
- timeline is reconstructed;
- impact is understood;
- root cause and contributing factors are recorded;
- response gaps are identified;
- prevention actions have owners;
- follow-up tracking exists;
- final report is shareable.

---

# 7. Escalation or Fallback

Escalate when:

- customer data was affected;
- legal or compliance review may be needed;
- root cause is still unknown;
- teams disagree on ownership;
- prevention actions require leadership approval;
- recurring incidents show systemic failure.

---

# 8. Final Principle

> The postmortem is complete only when learning becomes operational change.