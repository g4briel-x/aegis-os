## FILE: `templates/architecture/architecture-decision-record-template/TEMPLATE.md`

# Architecture Decision Record Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
ADR Title: {{adr_title}}
ADR ID: {{adr_id}}
Status: {{status}}
Decision Owner: {{decision_owner}}
Date: {{decision_date}}
Review Date: {{review_date}}
Related System: {{related_system}}
Related Release: {{related_release}}
```

---

# 2. Decision Summary

Summarize the decision in one short paragraph.

```text
{{decision_summary}}
```

Recommended format:

```text
We will use {{chosen_option}} for {{decision_scope}} because {{main_reason}}.
```

---

# 3. Context

Describe the situation that required a decision.

```text
{{context}}
```

Include:

```text
business context
technical context
product constraints
security constraints
operational constraints
current pain points
decision urgency
```

---

# 4. Problem

State the decision problem clearly.

```text
{{problem_statement}}
```

Recommended format:

```text
The team needs to decide {{decision_question}} in order to {{desired_outcome}}.
```

---

# 5. Decision Drivers

List the criteria used to evaluate options.

```text
Driver 1: {{decision_driver_1}}
Driver 2: {{decision_driver_2}}
Driver 3: {{decision_driver_3}}
Driver 4: {{decision_driver_4}}
```

Common drivers:

```text
simplicity
security
scalability
cost
delivery speed
maintainability
operational reliability
team capability
customer impact
```

---

# 6. Options Considered

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

## Option 3 — {{option_3_name}}

Description:

```text
{{option_3_description}}
```

Pros:

```text
{{option_3_pro_1}}
{{option_3_pro_2}}
```

Cons:

```text
{{option_3_con_1}}
{{option_3_con_2}}
```

---

# 7. Decision

Chosen option:

```text
{{chosen_option}}
```

Decision:

```text
{{decision}}
```

Reason:

```text
{{decision_reason}}
```

---

# 8. Consequences

## Positive Consequences

```text
{{positive_consequence_1}}
{{positive_consequence_2}}
{{positive_consequence_3}}
```

## Negative Consequences

```text
{{negative_consequence_1}}
{{negative_consequence_2}}
{{negative_consequence_3}}
```

## Neutral Consequences

```text
{{neutral_consequence_1}}
{{neutral_consequence_2}}
```

---

# 9. Risks and Mitigations

```text
Risk | Impact | Mitigation | Owner
{{risk_1}} | {{risk_impact_1}} | {{mitigation_1}} | {{risk_owner_1}}
{{risk_2}} | {{risk_impact_2}} | {{mitigation_2}} | {{risk_owner_2}}
```

---

# 10. Implementation Notes

```text
Implementation owner: {{implementation_owner}}
Implementation plan: {{implementation_plan}}
Migration required: {{migration_required}}
Feature flag required: {{feature_flag_required}}
Operational change required: {{operational_change_required}}
Documentation update required: {{documentation_update_required}}
```

---

# 11. Validation

How the decision will be validated:

```text
{{validation_method}}
```

Success signals:

```text
{{success_signal_1}}
{{success_signal_2}}
{{success_signal_3}}
```

Failure signals:

```text
{{failure_signal_1}}
{{failure_signal_2}}
{{failure_signal_3}}
```

---

# 12. Follow-Up Actions

```text
Action | Owner | Due Date | Status
{{action_1}} | {{action_owner_1}} | {{action_due_date_1}} | {{action_status_1}}
{{action_2}} | {{action_owner_2}} | {{action_due_date_2}} | {{action_status_2}}
```

---

# 13. Approval

```text
Architecture approval: {{architecture_approval}}
Engineering approval: {{engineering_approval}}
Security approval: {{security_approval}}
Operations approval: {{operations_approval}}
Product approval: {{product_approval}}
```

---

# 14. Final Principle

> An ADR should preserve the reasoning that future teams will need when the original context is gone.
