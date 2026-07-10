## FILE: `playbooks/infrastructure/fix-failing-ci-pipeline/README.md`

# Fix Failing CI Pipeline Playbook

Version: 0.1.0  
Status: Premium Draft  
Domain: Infrastructure  
Category: CI/CD Troubleshooting

---

# 1. Purpose

The Fix Failing CI Pipeline Playbook provides a structured procedure for diagnosing, fixing and preventing continuous integration failures.

It helps teams move from a failed check to a clear root cause, safe correction, verified pipeline recovery and prevention action.

---

# 2. Trigger

Use this Playbook when:

- a pull request check fails;
- a build fails in CI but works locally;
- tests fail only in the pipeline;
- dependency installation fails;
- lint, typecheck or formatting checks fail;
- deployment preview build fails;
- CI configuration changes break the workflow;
- pipeline failures block merge or release.

---

# 3. Scope

This Playbook covers:

- failed check identification;
- log review;
- local versus CI comparison;
- environment variable review;
- dependency and cache review;
- test failure diagnosis;
- build and deployment failure diagnosis;
- fix validation;
- prevention actions.

This Playbook does not replace production incident response, but it supports release and pull request quality gates.

---

# 4. Related Skills

```text
infrastructure.devops-engineer
engineering.senior-debugger
engineering.senior-developer
engineering.software-architect
security.security-engineer
```

---

# 5. Final Principle

> CI failures should be treated as evidence, not noise. A failing pipeline is a quality signal until proven otherwise.