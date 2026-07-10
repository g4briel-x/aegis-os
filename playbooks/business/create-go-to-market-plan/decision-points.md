## FILE: `playbooks/business/create-go-to-market-plan/decision-points.md`

# Create Go-To-Market Plan — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the Target Segment Specific Enough?

```yaml
decision_point:
  question: Is the target segment narrow enough to reach and learn from quickly?
  options:
    - yes
    - no
    - partially
  criteria:
    - clear buyer
    - clear pain
    - reachable channel
    - similar use case
    - measurable response
  recommended_action:
    yes: proceed with channel planning.
    no: narrow the segment.
    partially: run a small validation sprint.
  fallback: select one beachhead segment for the first campaign.
```

---

# 2. Decision Point — Is the Message Clear?

```yaml
decision_point:
  question: Can the target customer understand the value in one clear statement?
  options:
    - yes
    - no
    - partially
  criteria:
    - pain is explicit
    - outcome is concrete
    - category is clear
    - differentiator is visible
    - jargon is controlled
  recommended_action:
    yes: use message in campaign assets.
    no: refine positioning.
    partially: test message in interviews or outreach.
  fallback: use customer language from discovery interviews.
```

---

# 3. Decision Point — Is the Channel Credible?

```yaml
decision_point:
  question: Is the selected channel likely to reach the target buyer?
  options:
    - yes
    - no
    - unknown
  criteria:
    - buyer presence
    - cost to test
    - speed of feedback
    - team capability
    - channel fit with offer
  recommended_action:
    yes: run campaign.
    no: choose another channel.
    unknown: run small experiment.
  fallback: start with founder-led direct outreach.
```

---

# 4. Decision Point — Is the Sales Motion Appropriate?

```yaml
decision_point:
  question: Does the conversion motion match price, complexity and buyer expectations?
  options:
    - yes
    - no
    - partially
  criteria:
    - price point
    - onboarding complexity
    - buyer risk
    - demo need
    - procurement complexity
  recommended_action:
    yes: execute.
    no: adjust sales motion.
    partially: test with early prospects.
  fallback: use founder-led sales for early B2B SaaS validation.
```

---

# 5. Decision Point — Is GTM Ready to Execute?

```yaml
decision_point:
  question: Is the plan ready for a real market test?
  options:
    - yes
    - no
    - limited_test
  criteria:
    - segment selected
    - offer defined
    - channel selected
    - assets ready
    - metrics defined
    - owner assigned
  recommended_action:
    yes: launch GTM sprint.
    no: complete missing elements.
    limited_test: run controlled experiment with small audience.
  fallback: run a 7-day validation sprint before broad launch.
```

---

# 6. Final Principle

> GTM decisions should prioritize market learning over polished assumptions.
