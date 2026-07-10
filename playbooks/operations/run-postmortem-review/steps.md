## FILE: `playbooks/operations/run-postmortem-review/steps.md`

# Run Postmortem Review — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Define Review Scope

Clarify what event is being reviewed.

Capture:

- incident name;
- date and time;
- severity;
- affected services;
- affected users;
- review owner;
- participants.

Output:

```text
Postmortem review scope
```

---

# 2. Step 2 — Collect Facts and Evidence

Gather factual information before interpretation.

Collect:

- alerts;
- logs;
- metrics;
- deployment history;
- support reports;
- communication records;
- mitigation actions;
- recovery evidence.

Output:

```text
Incident fact set
```

---

# 3. Step 3 — Reconstruct Timeline

Create a chronological account.

Include:

- first signal;
- first user impact;
- detection time;
- acknowledgment time;
- mitigation attempts;
- recovery time;
- communication events;
- final resolution.

Output:

```text
Incident timeline
```

---

# 4. Step 4 — Summarize Impact

Describe the real effect of the incident.

Assess:

- users affected;
- workflows affected;
- downtime or degradation duration;
- business impact;
- data impact;
- security impact;
- support impact.

Output:

```text
Impact summary
```

---

# 5. Step 5 — Identify Root Cause

Identify the primary technical or process cause.

Separate:

- symptom;
- trigger;
- root cause;
- contributing factors;
- detection gap;
- response gap.

Output:

```text
Root cause analysis
```

---

# 6. Step 6 — Identify Contributing Factors

Document conditions that made the incident possible or worse.

Examples:

- missing test coverage;
- weak monitoring;
- unclear ownership;
- risky deployment process;
- incomplete rollback plan;
- missing documentation;
- fragile dependency;
- unclear alert threshold.

Output:

```text
Contributing factor list
```

---

# 7. Step 7 — Review Response Effectiveness

Evaluate how well the team responded.

Review:

- detection speed;
- triage quality;
- communication quality;
- escalation timing;
- mitigation effectiveness;
- recovery verification;
- stakeholder updates.

Output:

```text
Response review
```

---

# 8. Step 8 — Define Prevention Actions

Turn lessons into concrete improvements.

Good actions should be:

- specific;
- owned;
- prioritized;
- time-bound;
- verifiable.

Output:

```text
Prevention action plan
```

---

# 9. Step 9 — Publish Postmortem Report

Create a clear report for the right audience.

Include:

- summary;
- timeline;
- impact;
- root cause;
- response review;
- lessons;
- follow-up actions.

Output:

```text
Postmortem report
```

---

# 10. Step 10 — Track Follow-Up to Closure

Ensure actions are not forgotten.

Track:

- action;
- owner;
- priority;
- due date;
- status;
- verification evidence.

Output:

```text
Follow-up tracker
```

---

# 11. Final Principle

> Postmortem steps should convert incident memory into operational resilience.
