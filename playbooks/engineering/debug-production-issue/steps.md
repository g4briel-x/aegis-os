## FILE: `playbooks/engineering/debug-production-issue/steps.md`

# Debug Production Issue — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Confirm the Signal

Confirm that the issue is real and production-impacting.

Check:

- monitoring alerts;
- user reports;
- support tickets;
- logs;
- health checks;
- error rate;
- latency;
- failed transactions.

Output:

```text
Confirmed signal summary
```

---

# 2. Step 2 — Assess Impact

Determine the severity and scope.

Assess:

- affected users;
- affected services;
- affected regions;
- affected workflows;
- business impact;
- data integrity risk.

Output:

```text
Impact summary and severity estimate
```

---

# 3. Step 3 — Stabilize First

If user impact is active, prioritize safe stabilization.

Possible stabilization actions:

- rollback recent deployment;
- disable faulty feature flag;
- scale resources temporarily;
- restart unhealthy service;
- pause risky background jobs;
- route traffic away from failing component.

Output:

```text
Immediate mitigation decision
```

---

# 4. Step 4 — Collect Evidence

Collect evidence before changing too much.

Evidence sources:

- application logs;
- infrastructure logs;
- metrics;
- traces;
- deployment history;
- configuration changes;
- dependency status;
- database indicators.

Output:

```text
Evidence summary
```

---

# 5. Step 5 — Identify Recent Changes

Review what changed before the issue appeared.

Check:

- deployments;
- migrations;
- configuration;
- secrets;
- third-party integrations;
- infrastructure;
- dependency versions;
- feature flags.

Output:

```text
Recent change list
```

---

# 6. Step 6 — Build Hypotheses

Create ranked hypotheses based on evidence.

For each hypothesis, record:

- suspected cause;
- supporting evidence;
- contradicting evidence;
- test or validation method;
- risk if wrong.

Output:

```text
Ranked hypothesis list
```

---

# 7. Step 7 — Isolate Root Cause

Use evidence to eliminate weak hypotheses and isolate the likely root cause.

Actions may include:

- reproducing issue;
- comparing healthy and failing environments;
- inspecting logs around failure time;
- checking dependency responses;
- testing rollback or configuration change in safe environment.

Output:

```text
Likely root cause
```

---

# 8. Step 8 — Choose Mitigation or Fix

Decide whether to apply:

- rollback;
- hotfix;
- configuration correction;
- resource scaling;
- dependency workaround;
- data repair;
- feature disablement.

Output:

```text
Selected mitigation or fix plan
```

---

# 9. Step 9 — Verify Recovery

Verify that the issue is resolved.

Check:

- error rate;
- latency;
- user workflow success;
- logs;
- metrics;
- support reports;
- data correctness where relevant.

Output:

```text
Recovery verification notes
```

---

# 10. Step 10 — Document Prevention

Define follow-up actions to reduce recurrence.

Examples:

- regression test;
- alert improvement;
- safer rollout;
- better logging;
- runbook update;
- deployment guard;
- monitoring dashboard;
- postmortem.

Output:

```text
Prevention action list
```

---

# 11. Final Principle

> Debugging steps should reduce uncertainty while protecting production stability.
