## FILE: `playbooks/operations/run-postmortem-review/examples/examples.md`

# Run Postmortem Review — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — Production Outage Postmortem

## Trigger

A SaaS API was unavailable for 45 minutes after deployment.

## Expected Execution

The Playbook should guide the team to:

- reconstruct deployment and failure timeline;
- identify user impact;
- separate failed migration symptom from root cause;
- review rollback timing;
- define prevention actions such as migration testing and deployment gates.

## Expected Output

```text
Postmortem report
Timeline
Impact summary
Root cause analysis
Response review
Prevention action plan
```

---

# 2. Example — Security Incident Postmortem

## Trigger

An API token was leaked in logs and rotated.

## Expected Execution

The Playbook should guide the team to:

- record exposure window;
- review containment speed;
- identify why logging exposed the token;
- define redaction, secret scanning and logging improvements.

---

# 3. Example — Failed Release Review

## Trigger

A release required rollback after smoke tests failed.

## Expected Execution

The Playbook should guide the team to:

- review release readiness;
- identify missing test coverage;
- evaluate rollback effectiveness;
- define stronger release criteria.

---

# 4. Example — CI Failure Pattern Review

## Trigger

CI failures delayed multiple pull requests over two weeks.

## Expected Execution

The Playbook should guide the team to:

- group repeated failures;
- identify flaky tests or environment drift;
- define ownership and prevention improvements.

---

# 5. Final Principle

> Examples show that postmortems turn operational pain into repeatable improvement.
