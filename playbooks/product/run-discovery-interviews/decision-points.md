## FILE: `playbooks/product/run-discovery-interviews/decision-points.md`

# Run Discovery Interviews — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the Participant Relevant?

```yaml
decision_point:
  question: Does the participant match the target customer profile?
  options:
    - yes
    - no
    - partially
  criteria:
    - role
    - workflow relevance
    - pain exposure
    - buying influence
    - segment fit
  recommended_action:
    yes: conduct full interview.
    no: use as secondary context only.
    partially: label evidence carefully and avoid over-weighting it.
  fallback: recruit more targeted participants.
```

---

# 2. Decision Point — Is the Pain Strong Enough?

```yaml
decision_point:
  question: Is the pain frequent, costly or urgent enough to justify action?
  options:
    - strong
    - moderate
    - weak
    - unknown
  criteria:
    - frequency
    - time cost
    - money cost
    - operational risk
    - emotional intensity
    - current workaround
  recommended_action:
    strong: continue toward MVP or prototype.
    moderate: refine segment or problem framing.
    weak: avoid building until stronger evidence exists.
    unknown: run more interviews.
  fallback: test a narrower segment.
```

---

# 3. Decision Point — Is There a Buying Signal?

```yaml
decision_point:
  question: Did the interview reveal willingness to pay or adopt?
  options:
    - yes
    - no
    - unclear
  criteria:
    - budget mentioned
    - paid alternative used
    - decision maker identified
    - urgency expressed
    - request for follow-up
  recommended_action:
    yes: capture buying trigger and pricing context.
    no: validate whether the problem is only a convenience.
    unclear: ask follow-up questions about cost and alternatives.
  fallback: test with a landing page, paid pilot or concierge offer.
```

---

# 4. Decision Point — Do Patterns Repeat?

```yaml
decision_point:
  question: Are similar pains, workflows or objections repeating across interviews?
  options:
    - yes
    - no
    - insufficient_data
  criteria:
    - repeated pain language
    - repeated workflow
    - repeated workaround
    - repeated objection
    - repeated segment characteristics
  recommended_action:
    yes: synthesize into product requirements.
    no: segment may be too broad or problem may be weak.
    insufficient_data: continue interviews.
  fallback: split participants into subsegments and compare.
```

---

# 5. Final Principle

> Discovery decisions should be based on repeated evidence, not isolated enthusiasm.