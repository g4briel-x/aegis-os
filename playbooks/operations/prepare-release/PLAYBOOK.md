## FILE: `playbooks/operations/prepare-release/PLAYBOOK.md`

# Prepare Release — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured release readiness process from scope confirmation to post-release monitoring.

---

# 2. Trigger

A software change, feature, fix, migration or package is ready to be released.

---

# 3. Inputs

Useful inputs include:

- release name;
- release scope;
- change list;
- affected services;
- pull requests or commits;
- test results;
- acceptance criteria;
- deployment target;
- database migration plan;
- rollback plan;
- security review notes;
- stakeholder communication needs.

---

# 4. Outputs

Expected outputs include:

- release readiness summary;
- release checklist;
- risk register;
- deployment plan;
- rollback plan;
- communication plan;
- post-release monitoring plan;
- go / no-go decision.

---

# 5. Execution Summary

```text
1. Confirm release scope
2. Confirm acceptance criteria
3. Review code and tests
4. Review data, migration and compatibility impact
5. Review security and access impact
6. Confirm deployment plan
7. Confirm rollback plan
8. Confirm communication plan
9. Define post-release monitoring
10. Make go / no-go decision
```

---

# 6. Completion Criteria

The Playbook is complete when:

- release scope is clear;
- quality checks are complete;
- risks are documented;
- deployment steps are ready;
- rollback path is defined;
- communication is prepared;
- monitoring is defined;
- go / no-go decision is recorded.

---

# 7. Escalation or Fallback

Escalate when:

- tests are failing;
- migration risk is unclear;
- rollback is not possible;
- security review is incomplete;
- release scope is unstable;
- affected owners are unavailable;
- production impact is high.

---

# 8. Final Principle

> A release should not rely on hope. It should rely on readiness evidence.