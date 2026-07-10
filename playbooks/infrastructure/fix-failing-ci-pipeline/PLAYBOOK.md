## FILE: `playbooks/infrastructure/fix-failing-ci-pipeline/PLAYBOOK.md`

# Fix Failing CI Pipeline — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured troubleshooting process for CI pipeline failures.

---

# 2. Trigger

A CI check, build, test, lint, typecheck, packaging or deployment workflow fails.

---

# 3. Inputs

Useful inputs include:

- CI provider;
- repository;
- branch;
- pull request;
- failed workflow name;
- failed job;
- failed step;
- error logs;
- recent commits;
- CI configuration;
- package manager files;
- environment variable requirements;
- local reproduction result.

---

# 4. Outputs

Expected outputs include:

- CI failure diagnosis;
- root cause summary;
- fix recommendation;
- corrected configuration or code;
- verification steps;
- prevention actions;
- PR or release notes.

---

# 5. Execution Summary

```text
1. Identify failed workflow, job and step
2. Read the first meaningful error
3. Classify the failure type
4. Compare CI environment with local environment
5. Review recent changes
6. Build hypotheses
7. Apply minimal safe fix
8. Re-run CI or reproduce locally
9. Verify pipeline recovery
10. Document prevention action
```

---

# 6. Completion Criteria

The Playbook is complete when:

- failed step is identified;
- root cause is documented;
- fix is applied or recommended;
- CI passes or verification path is clear;
- recurrence prevention is documented;
- merge or release status is updated.

---

# 7. Escalation or Fallback

Escalate when:

- credentials or secrets are involved;
- deployment permissions fail;
- failure affects release branch;
- multiple unrelated checks fail;
- pipeline is flaky and not deterministic;
- logs are insufficient;
- security-sensitive environment variables are exposed.

---

# 8. Final Principle

> A CI failure is resolved only when the pipeline passes and the reason it failed is understood.
