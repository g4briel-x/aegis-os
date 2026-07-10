## FILE: `playbooks/operations/create-runbook/examples/examples.md`

# Create Runbook — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — Restart Background Worker

## Trigger

A background worker stops processing jobs.

## Expected Execution

The Playbook should guide the team to:

- define alert trigger;
- check queue backlog;
- restart worker safely;
- verify job processing resumes;
- escalate if backlog does not decrease.

## Expected Output

```text
Operational runbook
Trigger definition
Procedure steps
Command reference
Verification checklist
Escalation path
```

---

# 2. Example — Roll Back Deployment

## Trigger

A production deployment causes critical workflow failure.

## Expected Execution

The Playbook should guide the team to:

- confirm rollback trigger;
- identify previous version;
- execute rollback;
- verify production health;
- communicate status.

---

# 3. Example — Rotate API Key

## Trigger

A third-party API key must be rotated.

## Expected Execution

The Playbook should guide the team to:

- identify affected services;
- update secret store;
- redeploy if needed;
- verify integration;
- revoke old key safely.

---

# 4. Example — Restore Database Backup

## Trigger

A database restore procedure must be documented for disaster recovery.

## Expected Execution

The Playbook should guide the team to:

- define restore prerequisites;
- identify backup source;
- document restore commands;
- define validation queries;
- add escalation and approval gates.

---

# 5. Final Principle

> Examples show that runbooks convert operational knowledge into safe execution.

