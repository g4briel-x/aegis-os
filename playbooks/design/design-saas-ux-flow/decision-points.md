## FILE: `playbooks/design/design-saas-ux-flow/decision-points.md`

# Design SaaS UX Flow — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the User Goal Clear?

```yaml
decision_point:
  question: Is the primary user goal clear and specific?
  options:
    - yes
    - no
    - partially
  criteria:
    - user identified
    - task defined
    - outcome defined
    - success condition clear
  recommended_action:
    yes: continue to flow mapping.
    no: clarify product requirement first.
    partially: document assumption and continue with review flag.
  fallback: return to PRD or discovery notes.
```

---

# 2. Decision Point — Does the Flow Need Multiple Roles?

```yaml
decision_point:
  question: Does the flow behave differently for different roles?
  options:
    - yes
    - no
    - unknown
  criteria:
    - admin actions
    - viewer restrictions
    - tenant permissions
    - approval workflow
    - ownership rules
  recommended_action:
    yes: map role-specific behavior.
    no: document single-role flow.
    unknown: request permission model clarification.
  fallback: design the safest restricted behavior first.
```

---

# 3. Decision Point — Is a Screen Required?

```yaml
decision_point:
  question: Is this screen required to complete the user goal?
  options:
    - required
    - optional
    - remove
  criteria:
    - supports core task
    - reduces user confusion
    - required for validation
    - required for review or confirmation
  recommended_action:
    required: keep in flow.
    optional: move to secondary path.
    remove: eliminate from core flow.
  fallback: prototype both options and test friction.
```

---

# 4. Decision Point — Is the Flow Too Complex?

```yaml
decision_point:
  question: Does the flow contain too many steps or decisions for the user?
  options:
    - acceptable
    - too_complex
    - unknown
  criteria:
    - number of steps
    - user expertise
    - decision load
    - form length
    - error frequency
  recommended_action:
    acceptable: continue.
    too_complex: simplify, split or automate.
    unknown: test with representative users.
  fallback: create a lighter version for MVP.
```

---

# 5. Decision Point — Is Engineering Handoff Ready?

```yaml
decision_point:
  question: Can engineering understand what to build from this flow?
  options:
    - yes
    - no
    - partially
  criteria:
    - screens listed
    - states defined
    - permissions described
    - errors documented
    - data behavior clear
  recommended_action:
    yes: proceed to wireframe or implementation handoff.
    no: fill missing flow details.
    partially: document open questions and owners.
  fallback: run product-design-engineering review.
```

---

# 6. Final Principle

> UX decision points prevent unclear flows from becoming expensive interface rework.
