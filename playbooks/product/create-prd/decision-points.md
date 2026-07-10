## FILE: `playbooks/product/create-prd/decision-points.md`

# Create PRD — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the Problem Clear?

```yaml
decision_point:
  question: Is the user problem clearly defined?
  options:
    - yes
    - no
    - partially
  criteria:
    - affected user
    - pain described
    - consequence described
    - evidence available
  recommended_action:
    yes: continue to goals and scope.
    no: run discovery or stakeholder clarification first.
    partially: document assumptions and open questions.
  fallback: create a provisional problem statement and validate it before build.
```

---

# 2. Decision Point — Is This Feature In Scope?

```yaml
decision_point:
  question: Should this behavior be included in the current PRD scope?
  options:
    - include
    - exclude
    - defer
  criteria:
    - supports goal
    - required for core workflow
    - feasible within release
    - dependency impact
    - risk level
  recommended_action:
    include: add requirement and acceptance criteria.
    exclude: add to non-goals.
    defer: add to future considerations.
  fallback: require product owner decision.
```

---

# 3. Decision Point — Are Requirements Testable?

```yaml
decision_point:
  question: Can the requirement be verified through testing or review?
  options:
    - yes
    - no
    - unclear
  criteria:
    - observable behavior
    - measurable outcome
    - clear input and output
    - defined acceptance criteria
  recommended_action:
    yes: keep requirement.
    no: rewrite requirement.
    unclear: add examples and acceptance criteria.
  fallback: involve business analyst or QA reviewer.
```

---

# 4. Decision Point — Is Technical Feasibility Clear?

```yaml
decision_point:
  question: Is the requirement technically feasible with current constraints?
  options:
    - yes
    - no
    - unknown
  criteria:
    - architecture fit
    - data availability
    - integration complexity
    - security constraints
    - team capability
  recommended_action:
    yes: continue.
    no: revise scope or roadmap.
    unknown: request architecture or engineering review.
  fallback: create technical spike before implementation.
```

---

# 5. Decision Point — Is Security or Compliance Review Needed?

```yaml
decision_point:
  question: Does the requirement affect sensitive data, identity, authorization, payments or compliance?
  options:
    - yes
    - no
    - unclear
  criteria:
    - personal data
    - payment data
    - auth flow
    - role permissions
    - audit needs
    - regulated workflow
  recommended_action:
    yes: require security review.
    no: document no sensitive impact.
    unclear: treat as review-needed until resolved.
  fallback: add security review as dependency.
```

---

# 6. Final Principle

> PRD decision points prevent unclear requirements from becoming expensive implementation ambiguity.
