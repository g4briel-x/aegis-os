## FILE: `playbooks/operations/create-runbook/PLAYBOOK.md`

# Create Runbook — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured process for writing operational runbooks.

---

# 2. Trigger

A production, support, deployment, incident or maintenance process needs a repeatable operational procedure.

---

# 3. Inputs

Useful inputs include:

- operational process name;
- trigger scenario;
- affected systems;
- prerequisites;
- required permissions;
- commands;
- dashboards;
- logs;
- known failure modes;
- rollback steps;
- escalation contacts;
- verification criteria.

---

# 4. Outputs

Expected outputs include:

- operational runbook;
- trigger definition;
- prerequisite checklist;
- procedure steps;
- command reference;
- decision points;
- rollback section;
- escalation path;
- verification checklist;
- maintenance owner.

---

# 5. Execution Summary

```text
1. Define runbook purpose and scope
2. Define triggers and non-triggers
3. Identify systems, owners and access requirements
4. Document prerequisites and safety checks
5. Write step-by-step procedure
6. Add commands, dashboards and evidence references
7. Define decision points and failure handling
8. Define rollback and recovery actions
9. Define escalation and communication path
10. Add verification and maintenance rules
```

---

# 6. Completion Criteria

The Playbook is complete when:

- the runbook has a clear trigger;
- prerequisites are known;
- execution steps are ordered;
- commands are documented safely;
- verification checks are defined;
- rollback or recovery is included;
- escalation path is clear;
- maintenance owner is assigned.

---

# 7. Escalation or Fallback

Escalate when:

- production access is unclear;
- commands can cause data loss;
- rollback is unknown;
- security-sensitive credentials are involved;
- customer impact is possible;
- the operator cannot verify success;
- the process depends on undocumented manual judgment.

---

# 8. Final Principle

> Runbooks should reduce operational risk by turning critical procedures into precise, reviewable and repeatable actions.
