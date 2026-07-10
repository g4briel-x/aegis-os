## FILE: `playbooks/engineering/write-test-plan/PLAYBOOK.md`

# Write Test Plan — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured process for creating a test plan from product or engineering requirements.

---

# 2. Trigger

A feature, release, bug fix, API, workflow or PRD needs clear validation before merge or deployment.

---

# 3. Inputs

Useful inputs include:

- PRD;
- user stories;
- acceptance criteria;
- feature scope;
- bug report;
- implementation notes;
- UX flow;
- API contract;
- permission model;
- release plan;
- known risks;
- affected components.

---

# 4. Outputs

Expected outputs include:

- test plan;
- test scope;
- test strategy;
- functional test cases;
- edge case test cases;
- regression test cases;
- permission test cases;
- test data requirements;
- environment requirements;
- release validation checklist.

---

# 5. Execution Summary

```text
1. Review requirements and acceptance criteria
2. Define test scope and non-scope
3. Identify risk areas
4. Define test strategy
5. Write functional test cases
6. Write edge and failure test cases
7. Write permission and security test cases
8. Define regression coverage
9. Define test data and environment needs
10. Produce release validation checklist
```

---

# 6. Completion Criteria

The Playbook is complete when:

- test scope is clear;
- acceptance criteria are covered;
- critical workflows are tested;
- edge cases are documented;
- permission risks are covered;
- regression tests are identified;
- test data and environment needs are known;
- validation evidence is defined.

---

# 7. Escalation or Fallback

Escalate when:

- requirements are not testable;
- acceptance criteria are vague;
- security-sensitive behavior lacks review;
- test environment is missing;
- data setup is unclear;
- release risk is high;
- test coverage cannot prove critical behavior.

---

# 8. Final Principle

> Testing should verify product value, technical correctness and release safety.
