## FILE: `playbooks/operations/prepare-release/decision-points.md`

# Prepare Release — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is Release Scope Stable?

```yaml
decision_point:
  question: Is the release scope stable and clearly documented?
  options:
    - yes
    - no
    - partially
  criteria:
    - included changes
    - excluded changes
    - affected services
    - stakeholder agreement
  recommended_action:
    yes: continue readiness review.
    no: freeze or redefine scope before release.
    partially: document uncertainties and require owner approval.
  fallback: reduce release scope to the safest coherent set.
```

---

# 2. Decision Point — Are Tests and Reviews Complete?

```yaml
decision_point:
  question: Are required tests and reviews complete?
  options:
    - yes
    - no
    - with_known_risk
  criteria:
    - code review
    - test results
    - QA status
    - unresolved defects
  recommended_action:
    yes: continue release preparation.
    no: block release until required checks pass.
    with_known_risk: require explicit approval and mitigation.
  fallback: delay release or reduce scope.
```

---

# 3. Decision Point — Is Rollback Possible?

```yaml
decision_point:
  question: Can this release be rolled back safely?
  options:
    - yes
    - no
    - limited
  criteria:
    - database migration
    - feature flags
    - deployment method
    - compatibility
    - data transformation
  recommended_action:
    yes: document rollback path.
    no: require stronger validation and staged rollout.
    limited: define containment and mitigation plan.
  fallback: release behind feature flag or delay.
```

---

# 4. Decision Point — Is Security Review Required?

```yaml
decision_point:
  question: Does the release affect security-sensitive behavior?
  options:
    - yes
    - no
    - unclear
  criteria:
    - authentication
    - authorization
    - sensitive data
    - public API
    - secrets
    - payments
  recommended_action:
    yes: require security review before release.
    no: document no security-sensitive impact.
    unclear: involve security reviewer.
  fallback: treat as security-sensitive until ruled out.
```

---

# 5. Decision Point — Go or No-Go?

```yaml
decision_point:
  question: Should the release proceed?
  options:
    - go
    - no_go
    - conditional_go
  criteria:
    - scope readiness
    - quality readiness
    - rollback readiness
    - monitoring readiness
    - stakeholder approval
  recommended_action:
    go: proceed with deployment.
    no_go: block release and document reasons.
    conditional_go: proceed only with explicit conditions and owner approval.
  fallback: delay release until blockers are resolved.
```

---

# 6. Final Principle

> Release decisions should be evidence-based, not momentum-based.