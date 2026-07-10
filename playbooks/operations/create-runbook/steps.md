## FILE: `playbooks/operations/create-runbook/steps.md`

# Create Runbook — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Define Runbook Purpose and Scope

Clarify what operational process the runbook covers.

Capture:

- runbook name;
- process objective;
- affected services;
- intended operator;
- scope;
- non-scope;
- expected result.

Output:

```text
Runbook purpose and scope
```

---

# 2. Step 2 — Define Triggers and Non-Triggers

Specify when the runbook should and should not be used.

Capture:

- event trigger;
- alert trigger;
- manual trigger;
- scheduled trigger;
- emergency trigger;
- non-trigger scenarios;
- required approval if any.

Output:

```text
Trigger definition
```

---

# 3. Step 3 — Identify Systems, Owners and Access Requirements

List the operational context.

Capture:

- services;
- environments;
- dashboards;
- repositories;
- databases;
- cloud projects;
- required roles;
- escalation owner.

Output:

```text
System and access map
```

---

# 4. Step 4 — Document Prerequisites and Safety Checks

Define what must be true before execution.

Check:

- operator access;
- approval status;
- current incident status;
- backup availability;
- deployment state;
- maintenance window;
- customer impact risk;
- communication readiness.

Output:

```text
Prerequisite and safety checklist
```

---

# 5. Step 5 — Write Step-by-Step Procedure

Document the procedure in executable order.

Each step should include:

- action;
- command or UI path;
- expected result;
- evidence to capture;
- failure behavior;
- next step.

Output:

```text
Procedure steps
```

---

# 6. Step 6 — Add Commands, Dashboards and Evidence References

Provide exact references operators need.

Include:

- commands;
- script names;
- dashboard links or names;
- log query patterns;
- metric names;
- configuration locations;
- evidence screenshots or notes.

Output:

```text
Command and evidence reference
```

---

# 7. Step 7 — Define Decision Points and Failure Handling

Clarify choices during execution.

Examples:

- continue or stop;
- rollback or monitor;
- escalate or retry;
- mark as resolved or keep open;
- switch to incident response.

Output:

```text
Operational decision points
```

---

# 8. Step 8 — Define Rollback and Recovery Actions

Document how to undo or recover.

Capture:

- rollback trigger;
- rollback owner;
- rollback steps;
- data constraints;
- recovery validation;
- customer communication if needed.

Output:

```text
Rollback and recovery section
```

---

# 9. Step 9 — Define Escalation and Communication Path

Clarify who to contact and when.

Capture:

- technical owner;
- incident commander if relevant;
- security owner if relevant;
- product owner;
- support owner;
- communication channel;
- escalation threshold.

Output:

```text
Escalation and communication path
```

---

# 10. Step 10 — Add Verification and Maintenance Rules

Define how success is confirmed and how the runbook stays current.

Capture:

- verification checks;
- success criteria;
- post-execution notes;
- last reviewed date;
- owner;
- review cadence;
- update trigger.

Output:

```text
Verification and maintenance section
```

---

# 11. Final Principle

> Runbook steps should be written for execution during stress, not for explanation during calm.

---