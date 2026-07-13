## FILE: `templates/management/rfc-template/TEMPLATE.md`

# RFC Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
RFC Title: {{rfc_title}}
RFC ID: {{rfc_id}}
Author: {{author}}
Owner: {{owner}}
Status: {{status}}
Created Date: {{created_date}}
Last Updated: {{last_updated}}
Target Decision Date: {{target_decision_date}}
Reviewers: {{reviewers}}
```

---

# 2. Summary

```text
{{summary}}
```

Recommended format:

```text
This RFC proposes {{proposal}} in order to {{desired_outcome}} for {{affected_area}}.
```

---

# 3. Problem Statement

```text
{{problem_statement}}
```

Include:

```text
current situation
pain points
affected users or teams
business or technical cost
why action is needed now
```

---

# 4. Goals

```text
Goal 1: {{goal_1}}
Goal 2: {{goal_2}}
Goal 3: {{goal_3}}
```

---

# 5. Non-Goals

```text
Non-goal 1: {{non_goal_1}}
Non-goal 2: {{non_goal_2}}
Non-goal 3: {{non_goal_3}}
```

---

# 6. Proposal

```text
{{proposal_detail}}
```

The proposal should include:

```text
what changes
who is affected
how it will work
what will be created
what will be removed or replaced
what will remain unchanged
```

---

# 7. Scope

## 7.1 In Scope

```text
{{in_scope_item_1}}
{{in_scope_item_2}}
{{in_scope_item_3}}
```

## 7.2 Out of Scope

```text
{{out_of_scope_item_1}}
{{out_of_scope_item_2}}
{{out_of_scope_item_3}}
```

---

# 8. Options Considered

## Option 1 — {{option_1_name}}

Description:

```text
{{option_1_description}}
```

Pros:

```text
{{option_1_pro_1}}
{{option_1_pro_2}}
```

Cons:

```text
{{option_1_con_1}}
{{option_1_con_2}}
```

---

## Option 2 — {{option_2_name}}

Description:

```text
{{option_2_description}}
```

Pros:

```text
{{option_2_pro_1}}
{{option_2_pro_2}}
```

Cons:

```text
{{option_2_con_1}}
{{option_2_con_2}}
```

---

# 9. Recommended Option

```text
Recommended option: {{recommended_option}}
Reason: {{recommendation_reason}}
```

---

# 10. Impact Analysis

```text
Product impact:
{{product_impact}}

Engineering impact:
{{engineering_impact}}

Security impact:
{{security_impact}}

Operations impact:
{{operations_impact}}

Customer impact:
{{customer_impact}}

Business impact:
{{business_impact}}
```

---

# 11. Risks and Mitigations

```text
Risk | Impact | Likelihood | Mitigation | Owner
{{risk_1}} | {{risk_impact_1}} | {{risk_likelihood_1}} | {{mitigation_1}} | {{risk_owner_1}}
{{risk_2}} | {{risk_impact_2}} | {{risk_likelihood_2}} | {{mitigation_2}} | {{risk_owner_2}}
```

---

# 12. Dependencies

```text
Product dependencies:
{{product_dependencies}}

Engineering dependencies:
{{engineering_dependencies}}

Security dependencies:
{{security_dependencies}}

Operations dependencies:
{{operations_dependencies}}

External dependencies:
{{external_dependencies}}
```

---

# 13. Implementation Plan

```text
Phase 1:
{{implementation_phase_1}}

Phase 2:
{{implementation_phase_2}}

Phase 3:
{{implementation_phase_3}}
```

---

# 14. Migration or Rollout Plan

```text
Migration required: {{migration_required}}
Rollout strategy: {{rollout_strategy}}
Feature flag required: {{feature_flag_required}}
Backward compatibility: {{backward_compatibility}}
Rollback or recovery: {{rollback_or_recovery}}
```

---

# 15. Success Metrics

```text
Metric 1: {{success_metric_1}}
Metric 2: {{success_metric_2}}
Metric 3: {{success_metric_3}}
```

---

# 16. Open Questions

```text
Question 1: {{open_question_1}}
Question 2: {{open_question_2}}
Question 3: {{open_question_3}}
```

---

# 17. Decision

```text
Decision: {{decision}}
Decision date: {{decision_date}}
Decision owner: {{decision_owner}}
Decision reason: {{decision_reason}}
```

Recommended decision values:

```text
approved
approved_with_changes
rejected
deferred
needs_more_review
```

---

# 18. Follow-Up Actions

```text
Action | Owner | Due Date | Status
{{action_1}} | {{action_owner_1}} | {{action_due_date_1}} | {{action_status_1}}
{{action_2}} | {{action_owner_2}} | {{action_due_date_2}} | {{action_status_2}}
```

---

# 19. Approval

```text
Product approval: {{product_approval}}
Engineering approval: {{engineering_approval}}
Architecture approval: {{architecture_approval}}
Security approval: {{security_approval}}
Operations approval: {{operations_approval}}
Leadership approval: {{leadership_approval}}
```

---

# 20. Final Principle

> An RFC should make the proposal clear enough to approve, reject, defer or revise deliberately.
