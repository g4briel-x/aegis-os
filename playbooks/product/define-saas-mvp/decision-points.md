## FILE: `playbooks/product/define-saas-mvp/decision-points.md`

# Define SaaS MVP — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the Target User Clear?

```yaml
decision_point:
  question: Is there one clear primary user segment?
  options:
    - yes
    - no
    - partially
  criteria:
    - user type
    - pain context
    - ability to access users
    - business relevance
  recommended_action:
    yes: Continue to problem definition.
    no: run customer segmentation before MVP definition.
    partially: choose the most urgent and reachable segment for MVP.
  fallback: Define a temporary assumption and validate it during discovery.
```

---

# 2. Decision Point — Is the Problem Painful Enough?

```yaml
decision_point:
  question: Is the problem painful, frequent or valuable enough to justify a SaaS?
  options:
    - yes
    - no
    - unknown
  criteria:
    - frequency
    - cost of problem
    - current workaround
    - willingness to pay
    - urgency
  recommended_action:
    yes: Continue to MVP scope.
    no: reconsider positioning or customer segment.
    unknown: run discovery interviews before building.
  fallback: Create a validation experiment before committing engineering effort.
```

---

# 3. Decision Point — Is a Feature Must-Have?

```yaml
decision_point:
  question: Is this feature required to prove the core MVP value?
  options:
    - must_have
    - should_have_later
    - exclude
  criteria:
    - supports core workflow
    - validates demand
    - required for trust or safety
    - required for payment or activation
  recommended_action:
    must_have: include in MVP.
    should_have_later: move to post-MVP roadmap.
    exclude: remove from scope.
  fallback: If uncertain, create manual workaround for MVP.
```

---

# 4. Decision Point — Is the MVP Buildable With Available Resources?

```yaml
decision_point:
  question: Can this MVP be built with available time, budget and technical capacity?
  options:
    - yes
    - no
    - risky
  criteria:
    - engineering complexity
    - design complexity
    - data requirements
    - integration needs
    - timeline
  recommended_action:
    yes: move to delivery planning.
    no: reduce scope.
    risky: identify the highest-risk part and validate it first.
  fallback: create prototype or concierge MVP.
```

---

# 5. Final Principle

> Decision points force the MVP to stay focused on proof, not ambition.