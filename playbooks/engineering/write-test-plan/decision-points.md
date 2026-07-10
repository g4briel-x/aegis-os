## FILE: `playbooks/engineering/write-test-plan/decision-points.md`

# Write Test Plan — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Are Requirements Testable?

```yaml
decision_point:
  question: Can the requirement be verified through a test, review or observable result?
  options:
    - yes
    - no
    - partially
  criteria:
    - observable behavior
    - clear expected result
    - measurable outcome
    - acceptance criteria available
  recommended_action:
    yes: convert requirement into test case.
    no: request requirement clarification.
    partially: add assumptions and missing acceptance criteria.
  fallback: block release validation until critical requirements are testable.
```

---

# 2. Decision Point — Is Automated Testing Required?

```yaml
decision_point:
  question: Should this behavior be covered by automated tests?
  options:
    - yes
    - no
    - optional
  criteria:
    - critical path
    - high regression risk
    - repeated workflow
    - security-sensitive behavior
    - business impact
  recommended_action:
    yes: define automated test coverage.
    no: document manual validation reason.
    optional: prioritize if time allows.
  fallback: automate critical behavior first.
```

---

# 3. Decision Point — Is Security Testing Required?

```yaml
decision_point:
  question: Does the feature require security or permission test coverage?
  options:
    - yes
    - no
    - unclear
  criteria:
    - role permissions
    - sensitive data
    - authentication
    - authorization
    - tenant boundary
    - public API
  recommended_action:
    yes: add security and permission tests.
    no: document low security impact.
    unclear: involve Security Engineer Skill.
  fallback: treat as security-sensitive until reviewed.
```

---

# 4. Decision Point — Is Test Data Available?

```yaml
decision_point:
  question: Is required test data available and safe to use?
  options:
    - yes
    - no
    - partially
  criteria:
    - test accounts
    - sample records
    - files
    - mock services
    - seeded data
    - privacy constraints
  recommended_action:
    yes: proceed.
    no: create test data setup task.
    partially: document gaps and owners.
  fallback: avoid using real sensitive production data.
```

---

# 5. Decision Point — Is Release Validation Complete?

```yaml
decision_point:
  question: Is there enough evidence to approve merge or release?
  options:
    - yes
    - no
    - conditional
  criteria:
    - critical tests passed
    - blockers resolved
    - risks accepted
    - evidence recorded
    - owners approved
  recommended_action:
    yes: approve validation.
    no: block release.
    conditional: document explicit conditions and owner approval.
  fallback: keep release blocked for critical workflow uncertainty.
```

---

# 6. Final Principle

> Test planning decisions should protect users from unverified behavior.