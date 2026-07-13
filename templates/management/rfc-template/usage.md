## FILE: `templates/management/rfc-template/usage.md`

# RFC Template — Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Usage Process

Use this sequence:

```text
1. Define RFC title and owner
2. State the problem
3. Define goals and non-goals
4. Write the proposal
5. Compare realistic options
6. Analyze impact
7. Document risks and mitigations
8. Define rollout or migration plan
9. Collect feedback
10. Record decision and follow-up actions
```

---

# 2. Recommended Review Flow

Review in this order:

```text
Author self-review
Product review if user impact exists
Engineering review if implementation impact exists
Architecture review if system structure changes
Security review if security impact exists
Operations review if production impact exists
Final decision owner review
```

---

# 3. Writing Rules

An RFC should:

- be specific;
- separate goals and non-goals;
- compare options honestly;
- include risks;
- define decision owner;
- include enough context for reviewers;
- record the final decision.

---

# 4. Proposal Rule

Weak:

```text
We should improve releases.
```

Better:

```text
We should introduce feature flags for customer-facing releases so activation can be staged, monitored and rolled back without redeploying.
```

---

# 5. Final Principle

> Use the RFC Template when the cost of being unclear is higher than the cost of writing the proposal.
