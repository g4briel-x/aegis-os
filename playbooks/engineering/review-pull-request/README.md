## FILE: `playbooks/engineering/review-pull-request/README.md`

# Review Pull Request Playbook

Version: 0.1.0  
Status: Premium Draft  
Domain: Engineering  
Category: Code Review

---

# 1. Purpose

The Review Pull Request Playbook provides a structured procedure for reviewing code changes before merge.

It helps reviewers validate correctness, maintainability, security, tests, architecture alignment, performance impact, documentation and release risk.

---

# 2. Trigger

Use this Playbook when:

- a pull request is ready for review;
- a feature implementation needs approval;
- a bug fix needs validation;
- a security-sensitive change needs inspection;
- a database or API change needs review;
- a release branch requires final technical review;
- a code change has unclear risks or side effects.

---

# 3. Scope

This Playbook covers:

- PR context review;
- requirement alignment;
- code correctness;
- architecture impact;
- security impact;
- test coverage;
- database and API changes;
- performance and reliability;
- documentation;
- merge readiness.

This Playbook does not replace automated tests or static analysis, but it ensures human review is disciplined and evidence-based.

---

# 4. Related Skills

```text
engineering.senior-developer
engineering.software-architect
engineering.senior-debugger
engineering.database-engineer
security.security-engineer
infrastructure.devops-engineer
```

---

# 5. Final Principle

> A pull request is ready to merge only when its behavior, risks, tests and operational impact are understood.