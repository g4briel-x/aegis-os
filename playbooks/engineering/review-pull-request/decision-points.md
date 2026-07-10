## FILE: `playbooks/engineering/review-pull-request/decision-points.md`

# Review Pull Request — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the PR Small Enough to Review Safely?

```yaml
decision_point:
  question: Is the pull request focused enough for reliable review?
  options:
    - yes
    - no
    - partially
  criteria:
    - number of changed files
    - unrelated changes
    - diff size
    - conceptual scope
    - reviewer confidence
  recommended_action:
    yes: continue review.
    no: request split PR or clearer review scope.
    partially: review high-risk parts first and flag scope concern.
  fallback: block merge until the PR is reviewable.
```

---

# 2. Decision Point — Does the PR Match the Requirement?

```yaml
decision_point:
  question: Does the implementation satisfy the linked requirement or acceptance criteria?
  options:
    - yes
    - no
    - unclear
  criteria:
    - PRD alignment
    - user story alignment
    - bug fix expectation
    - acceptance criteria coverage
  recommended_action:
    yes: continue technical review.
    no: request changes.
    unclear: ask for clarification or examples.
  fallback: block merge until expected behavior is clear.
```

---

# 3. Decision Point — Is Security Review Required?

```yaml
decision_point:
  question: Does the PR affect identity, permissions, sensitive data, files, payments or public APIs?
  options:
    - yes
    - no
    - unclear
  criteria:
    - auth change
    - role or permission change
    - sensitive data
    - public endpoint
    - file handling
    - billing or financial logic
  recommended_action:
    yes: require security review.
    no: document no security-sensitive impact.
    unclear: treat as security-sensitive until reviewed.
  fallback: involve Security Engineer Skill.
```

---

# 4. Decision Point — Are Tests Sufficient?

```yaml
decision_point:
  question: Does the PR include enough validation for the changed behavior?
  options:
    - yes
    - no
    - partially
  criteria:
    - critical path covered
    - edge cases covered
    - regression covered
    - CI passing
    - manual validation documented
  recommended_action:
    yes: continue.
    no: request tests or documented validation.
    partially: request targeted tests for high-risk gaps.
  fallback: block merge for untested critical behavior.
```

---

# 5. Decision Point — Is the PR Merge-Ready?

```yaml
decision_point:
  question: Should the PR be merged now?
  options:
    - approve
    - request_changes
    - block
    - needs_specialist_review
  criteria:
    - correctness
    - tests
    - security
    - maintainability
    - release risk
  recommended_action:
    approve: merge after required checks pass.
    request_changes: list required corrections.
    block: explain blocking risk.
    needs_specialist_review: route to relevant expert.
  fallback: keep PR open until risk is resolved.
```

---

# 6. Final Principle

> PR decisions should be based on evidence, not trust in momentum.