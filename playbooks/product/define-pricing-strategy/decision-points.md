## FILE: `playbooks/product/define-pricing-strategy/decision-points.md`

# Define Pricing Strategy — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the Buyer Clearly Identified?

```yaml
decision_point:
  question: Is the person or organization that pays clearly identified?
  options:
    - yes
    - no
    - partially
  criteria:
    - budget owner
    - decision maker
    - user versus buyer distinction
    - buying trigger
    - approval process
  recommended_action:
    yes: continue pricing design.
    no: run customer discovery before final pricing.
    partially: document assumptions and validate quickly.
  fallback: do not finalize pricing without buyer clarity.
```

---

# 2. Decision Point — Is the Pricing Metric Value-Aligned?

```yaml
decision_point:
  question: Does the pricing metric scale with customer value?
  options:
    - yes
    - no
    - partially
  criteria:
    - easy to understand
    - grows with usage or value
    - does not punish adoption
    - aligns with cost
    - simple to bill
  recommended_action:
    yes: use as primary metric.
    no: select another metric.
    partially: combine with tier or usage guardrails.
  fallback: choose the simplest value-aligned metric for MVP.
```

---

# 3. Decision Point — Should Freemium Be Used?

```yaml
decision_point:
  question: Should the product include a free plan?
  options:
    - yes
    - no
    - trial_instead
  criteria:
    - self-serve acquisition
    - low cost to serve
    - viral or network effect
    - clear upgrade trigger
    - support burden
  recommended_action:
    yes: design strict limits and upgrade path.
    no: use paid plan or demo-led model.
    trial_instead: offer temporary access with conversion path.
  fallback: avoid freemium if cost to serve or support burden is high.
```

---

# 4. Decision Point — Is Enterprise Pricing Needed?

```yaml
decision_point:
  question: Does the product need enterprise or custom pricing?
  options:
    - yes
    - no
    - later
  criteria:
    - large customer complexity
    - custom onboarding
    - security review
    - SLA requirement
    - volume discounting
    - procurement process
  recommended_action:
    yes: define enterprise package and sales process.
    no: keep transparent pricing.
    later: document enterprise triggers.
  fallback: add contact-sales option only if enterprise motion is credible.
```

---

# 5. Decision Point — Is Pricing Ready to Launch?

```yaml
decision_point:
  question: Is pricing clear enough to test with real customers?
  options:
    - yes
    - no
    - test_only
  criteria:
    - segments defined
    - tiers understandable
    - value proposition clear
    - assumptions documented
    - validation plan ready
  recommended_action:
    yes: launch pricing test.
    no: refine segmentation and packaging.
    test_only: present as pilot or beta pricing.
  fallback: test pricing conversations before publishing final pricing page.
```

---

# 6. Final Principle

> Pricing decisions should be validated against customer value, adoption friction and business viability.
