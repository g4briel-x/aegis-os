## FILE: `playbooks/engineering/implement-feature-from-prd/decision-points.md`

# Implement Feature From PRD — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the PRD Implementation-Ready?

```yaml
decision_point:
  question: Is the PRD clear enough for engineering implementation?
  options:
    - yes
    - no
    - partially
  criteria:
    - requirements clear
    - acceptance criteria testable
    - scope defined
    - open questions manageable
  recommended_action:
    yes: proceed to technical planning.
    no: return to product clarification.
    partially: implement stable scope and document blockers.
  fallback: create engineering questions for Product Manager.
```

---

# 2. Decision Point — Is Architecture Review Needed?

```yaml
decision_point:
  question: Does the feature affect architecture, data model, permissions or integrations?
  options:
    - yes
    - no
    - unclear
  criteria:
    - new component
    - database change
    - API contract change
    - new integration
    - authorization change
  recommended_action:
    yes: request architecture review.
    no: proceed with standard implementation.
    unclear: perform lightweight architecture review.
  fallback: involve Software Architect Skill.
```

---

# 3. Decision Point — Is a Database Migration Required?

```yaml
decision_point:
  question: Does the feature require schema, data or migration changes?
  options:
    - yes
    - no
    - unknown
  criteria:
    - new table
    - new field
    - changed constraint
    - data backfill
    - index need
  recommended_action:
    yes: create migration plan and rollback notes.
    no: continue without data migration.
    unknown: review data model before coding.
  fallback: involve Database Engineer Skill.
```

---

# 4. Decision Point — Is Security Review Required?

```yaml
decision_point:
  question: Does the feature affect identity, authorization, sensitive data, files, payments or public APIs?
  options:
    - yes
    - no
    - unclear
  criteria:
    - user roles
    - sensitive fields
    - object ownership
    - public endpoint
    - file access
    - billing logic
  recommended_action:
    yes: require security review before merge.
    no: document no security-sensitive impact.
    unclear: treat as security-sensitive until reviewed.
  fallback: involve Security Engineer Skill.
```

---

# 5. Decision Point — Is the Feature Ready for Pull Request?

```yaml
decision_point:
  question: Is the implementation ready for review?
  options:
    - yes
    - no
    - partially
  criteria:
    - requirements implemented
    - tests pass
    - acceptance criteria covered
    - risks documented
    - documentation updated where needed
  recommended_action:
    yes: prepare PR.
    no: complete missing implementation or validation.
    partially: open draft PR with clear remaining work.
  fallback: request senior developer review.
```

---

# 6. Final Principle

> Implementation decision points prevent unclear product requirements from becoming hidden engineering risk.