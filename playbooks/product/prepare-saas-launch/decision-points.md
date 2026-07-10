## FILE: `playbooks/product/prepare-saas-launch/decision-points.md`

# Prepare SaaS Launch — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the Product Ready for the Launch Type?

```yaml
decision_point:
  question: Is product quality sufficient for the chosen launch type?
  options:
    - yes
    - no
    - limited_launch_only
  criteria:
    - critical workflows work
    - blockers resolved
    - tests passed
    - known issues acceptable
    - production readiness verified
  recommended_action:
    yes: continue launch preparation.
    no: delay launch.
    limited_launch_only: reduce audience or launch as beta/pilot.
  fallback: choose a smaller launch if readiness is uncertain.
```

---

# 2. Decision Point — Is the Offer Clear?

```yaml
decision_point:
  question: Can the target customer understand what is offered and why it matters?
  options:
    - yes
    - no
    - partially
  criteria:
    - value proposition clear
    - audience defined
    - pricing understandable
    - activation promise clear
    - objections addressed
  recommended_action:
    yes: proceed.
    no: refine positioning and pricing.
    partially: test messaging with target users before launch.
  fallback: do not launch publicly with vague positioning.
```

---

# 3. Decision Point — Is Onboarding Ready?

```yaml
decision_point:
  question: Can a new user reach the first value milestone without team assistance?
  options:
    - yes
    - no
    - assisted_only
  criteria:
    - signup works
    - first action clear
    - empty states helpful
    - support available
    - activation milestone measurable
  recommended_action:
    yes: launch normally.
    no: improve onboarding before launch.
    assisted_only: launch as concierge or pilot.
  fallback: use assisted onboarding for early beta users.
```

---

# 4. Decision Point — Are Launch Metrics Ready?

```yaml
decision_point:
  question: Can the team measure whether the launch is working?
  options:
    - yes
    - no
    - partially
  criteria:
    - analytics installed
    - success metrics defined
    - funnel events tracked
    - error monitoring available
    - feedback channel active
  recommended_action:
    yes: proceed.
    no: add basic analytics before launch.
    partially: define manual tracking fallback.
  fallback: delay large launch until core metrics are visible.
```

---

# 5. Decision Point — Should the Launch Proceed?

```yaml
decision_point:
  question: Should the launch proceed now?
  options:
    - launch
    - delay
    - limited_launch
    - pilot_only
  criteria:
    - product readiness
    - support readiness
    - analytics readiness
    - security readiness
    - business urgency
    - risk tolerance
  recommended_action:
    launch: proceed and monitor.
    delay: resolve blockers first.
    limited_launch: restrict audience and observe.
    pilot_only: launch with selected customers and high support.
  fallback: choose the smallest launch that can produce useful learning.
```

---

# 6. Final Principle

> Launch decisions should balance learning speed with user trust and operational readiness.
