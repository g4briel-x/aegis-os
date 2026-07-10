## FILE: `playbooks/engineering/review-pull-request/PLAYBOOK.md`

# Review Pull Request — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured review of a pull request before merge.

---

# 2. Trigger

A code change is submitted for review, approval or merge readiness assessment.

---

# 3. Inputs

Useful inputs include:

- pull request description;
- linked issue or PRD;
- changed files;
- code diff;
- test results;
- screenshots if UI changed;
- migration notes;
- deployment notes;
- security notes;
- reviewer comments;
- CI status.

---

# 4. Outputs

Expected outputs include:

- PR review summary;
- approval or change request;
- risk notes;
- test review;
- security findings;
- architecture findings;
- merge readiness decision;
- follow-up actions.

---

# 5. Execution Summary

```text
1. Understand the PR purpose
2. Confirm requirement alignment
3. Review changed files and scope
4. Review correctness and edge cases
5. Review architecture and maintainability
6. Review security and data impact
7. Review tests and CI results
8. Review documentation and release notes
9. Decide approve, request changes or block
10. Record review findings and follow-up actions
```

---

# 6. Completion Criteria

The Playbook is complete when:

- PR purpose is understood;
- changed scope is reviewed;
- correctness risks are assessed;
- tests are reviewed;
- security and data impact are considered;
- required changes are documented;
- merge readiness decision is recorded.

---

# 7. Escalation or Fallback

Escalate when:

- the PR is too large to review safely;
- architecture impact is unclear;
- test coverage is insufficient;
- security-sensitive behavior is changed;
- database migration risk exists;
- CI is failing;
- reviewers disagree on merge readiness.

---

# 8. Final Principle

> Code review should protect product behavior, engineering quality and production safety.
