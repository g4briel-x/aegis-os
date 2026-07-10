## FILE: `playbooks/management/plan-saas-mvp-delivery/decision-points.md`

# Plan SaaS MVP Delivery — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is MVP Scope Stable Enough?

```yaml
decision_point:
  question: Is the MVP scope stable enough to plan delivery?
  options:
    - yes
    - no
    - partially
  criteria:
    - target user defined
    - core workflow defined
    - must-have features listed
    - excluded features documented
    - success metrics known
  recommended_action:
    yes: proceed to workstream planning.
    no: return to MVP definition.
    partially: document assumptions and plan only stable scope.
  fallback: create a discovery or PRD task before delivery planning.
```

---

# 2. Decision Point — Are Architecture Inputs Ready?

```yaml
decision_point:
  question: Is the technical architecture clear enough for implementation planning?
  options:
    - yes
    - no
    - partially
  criteria:
    - components defined
    - data model outlined
    - API model outlined
    - auth model defined
    - infrastructure direction known
  recommended_action:
    yes: proceed to milestone planning.
    no: run architecture playbook first.
    partially: plan known work and create architecture spike for gaps.
  fallback: block high-risk implementation until architecture is reviewed.
```

---

# 3. Decision Point — Is the Timeline Realistic?

```yaml
decision_point:
  question: Is the target launch timeline realistic for the scope and team capacity?
  options:
    - yes
    - no
    - risky
  criteria:
    - number of features
    - team capacity
    - unknowns
    - dependencies
    - testing and release needs
  recommended_action:
    yes: proceed.
    no: reduce scope or adjust date.
    risky: identify scope cuts and risk buffers.
  fallback: define an internal alpha before public launch.
```

---

# 4. Decision Point — Are Owners Clear?

```yaml
decision_point:
  question: Does every critical workstream and risk have an owner?
  options:
    - yes
    - no
    - partially
  criteria:
    - product owner
    - design owner
    - engineering owner
    - infrastructure owner
    - security owner
    - release owner
  recommended_action:
    yes: proceed.
    no: assign owners before execution starts.
    partially: document missing owners as blockers.
  fallback: technical project manager owns escalation until final owners are assigned.
```

---

# 5. Decision Point — Is Release Readiness Planned?

```yaml
decision_point:
  question: Is release readiness part of the delivery plan?
  options:
    - yes
    - no
    - partially
  criteria:
    - QA plan
    - security review
    - deployment plan
    - rollback plan
    - monitoring plan
    - launch communication
  recommended_action:
    yes: keep release milestone.
    no: add release readiness workstream.
    partially: create missing readiness tasks.
  fallback: block launch until release readiness is reviewed.
```

---

# 6. Final Principle

> Delivery decision points prevent teams from starting fast and failing late.