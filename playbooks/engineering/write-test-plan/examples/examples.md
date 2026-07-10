## FILE: `playbooks/engineering/write-test-plan/examples/examples.md`

# Write Test Plan — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — Audiovisual Project Submission Feature

## Trigger

A PRD defines a flow where creators submit film, series or documentary projects for financing review.

## Expected Execution

The Playbook should guide the team to:

- test required form fields;
- test draft and submitted states;
- test file upload success and failure;
- test reviewer permissions;
- test creator cannot access another creator's project;
- test submission confirmation.

## Expected Output

```text
Test plan
Functional test cases
Edge case test cases
Permission test matrix
Regression coverage
Release validation checklist
```

---

# 2. Example — Login Bug Fix

## Trigger

A bug fix corrects login failure for existing users.

## Expected Execution

The Playbook should guide the team to:

- test successful login;
- test invalid password;
- test expired session;
- test account recovery if affected;
- add regression coverage for the original bug.

---

# 3. Example — Billing Feature

## Trigger

A SaaS billing feature is ready for QA.

## Expected Execution

The Playbook should guide the team to:

- test subscription creation;
- test payment failure;
- test invoice display;
- test account owner permissions;
- validate no sensitive payment data is exposed.

---

# 4. Example — API Contract Change

## Trigger

An API response schema changes for a dashboard endpoint.

## Expected Execution

The Playbook should guide the team to:

- test response schema;
- test backward compatibility;
- test error responses;
- test frontend integration;
- add regression coverage.

---

# 5. Final Principle

> Examples show how test planning turns requirements into evidence before release.
