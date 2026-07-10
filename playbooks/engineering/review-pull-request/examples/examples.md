## FILE: `playbooks/engineering/review-pull-request/examples/examples.md`

# Review Pull Request — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — Feature PR

## Trigger

A PR implements a new audiovisual project submission feature.

## Expected Execution

The Playbook should guide the reviewer to:

- compare implementation to PRD;
- inspect form validation;
- review API and database changes;
- verify file access permissions;
- check tests;
- request security review if needed.

## Expected Output

```text
PR review summary
Correctness findings
Security findings
Test review
Merge decision
Follow-up actions
```

---

# 2. Example — Bug Fix PR

## Trigger

A PR fixes a login failure affecting production users.

## Expected Execution

The Playbook should guide the reviewer to:

- confirm the fix targets the root cause;
- review regression test;
- check side effects on authentication;
- verify release urgency and rollback notes.

---

# 3. Example — Database Migration PR

## Trigger

A PR adds new fields and indexes to support a dashboard feature.

## Expected Execution

The Playbook should guide the reviewer to:

- inspect migration safety;
- check rollback limits;
- review index impact;
- validate data compatibility;
- involve Database Engineer Skill if needed.

---

# 4. Example — Security-Sensitive PR

## Trigger

A PR changes role permissions for workspace admins.

## Expected Execution

The Playbook should guide the reviewer to:

- review authorization matrix;
- check privilege escalation risk;
- require permission tests;
- require audit logging;
- involve Security Engineer Skill.

---

# 5. Final Principle

> Examples show how PR review adapts to change type while keeping the same quality discipline.
