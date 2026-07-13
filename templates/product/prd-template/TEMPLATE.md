## FILE: `templates/product/prd-template/TEMPLATE.md`

# Product Requirements Document Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
Product / Feature Name: {{feature_name}}
Product Area: {{product_area}}
Owner: {{owner}}
Contributors: {{contributors}}
Status: {{status}}
Version: {{version}}
Last Updated: {{last_updated}}
Target Release: {{target_release}}
```

---

# 2. Summary

Write a short summary of the feature or product initiative.

```text
{{summary}}
```

Recommended format:

```text
This feature helps {{target_user}} solve {{problem_statement}} by enabling {{core_capability}}.
```

---

# 3. Problem Statement

Describe the customer or business problem.

```text
{{problem_statement}}
```

Include:

```text
who has the problem
why it matters
how it is currently handled
what pain or cost exists today
```

---

# 4. Goals

List the goals of the feature.

```text
Goal 1: {{goal_1}}
Goal 2: {{goal_2}}
Goal 3: {{goal_3}}
```

Goals should be measurable when possible.

---

# 5. Non-Goals

List what is intentionally out of scope.

```text
Non-goal 1: {{non_goal_1}}
Non-goal 2: {{non_goal_2}}
Non-goal 3: {{non_goal_3}}
```

Non-goals prevent scope creep.

---

# 6. Target Users

Define the primary and secondary users.

```text
Primary user: {{primary_user}}
Secondary users: {{secondary_users}}
Buyer or decision-maker: {{buyer}}
Admin or operator: {{admin_user}}
```

---

# 7. Use Cases

Describe the main use cases.

```text
Use Case 1:
As a {{user_role}}, I want to {{user_action}} so that {{user_outcome}}.

Use Case 2:
As a {{user_role}}, I want to {{user_action}} so that {{user_outcome}}.
```

---

# 8. User Journey

Describe the expected user flow.

```text
1. {{journey_step_1}}
2. {{journey_step_2}}
3. {{journey_step_3}}
4. {{journey_step_4}}
5. {{journey_step_5}}
```

---

# 9. Functional Requirements

Define what the system must do.

```text
FR-001: {{functional_requirement_1}}
FR-002: {{functional_requirement_2}}
FR-003: {{functional_requirement_3}}
FR-004: {{functional_requirement_4}}
FR-005: {{functional_requirement_5}}
```

Each requirement should be testable.

---

# 10. Acceptance Criteria

Define acceptance criteria for the feature.

```text
AC-001:
Given {{condition}}
When {{action}}
Then {{expected_result}}

AC-002:
Given {{condition}}
When {{action}}
Then {{expected_result}}
```

---

# 11. UX and UI Requirements

Define product experience requirements.

```text
Screens required:
- {{screen_1}}
- {{screen_2}}

Empty states:
- {{empty_state}}

Loading states:
- {{loading_state}}

Error states:
- {{error_state}}

Accessibility notes:
- {{accessibility_notes}}
```

---

# 12. Data Requirements

Define data that must be created, read, updated or deleted.

```text
Entities:
- {{entity_1}}
- {{entity_2}}

Fields:
- {{field_1}}
- {{field_2}}

Data ownership:
{{data_ownership}}

Retention or deletion:
{{data_retention}}
```

---

# 13. API Requirements

Define APIs if relevant.

```text
Endpoint: {{api_endpoint}}
Method: {{api_method}}
Request: {{api_request}}
Response: {{api_response}}
Errors: {{api_errors}}
```

---

# 14. Permissions and Security

Define authorization and security expectations.

```text
Roles:
- {{role_1}}
- {{role_2}}

Permissions:
- {{permission_1}}
- {{permission_2}}

Security notes:
{{security_notes}}

Audit events:
{{audit_events}}
```

---

# 15. Analytics and Success Metrics

Define success metrics and product analytics.

```text
Success metric: {{success_metric}}
Activation event: {{activation_event}}
Adoption metric: {{adoption_metric}}
Retention signal: {{retention_signal}}
Business metric: {{business_metric}}
```

Events to track:

```text
{{event_1}}
{{event_2}}
{{event_3}}
```

---

# 16. Dependencies

List dependencies.

```text
Design dependency: {{design_dependency}}
Engineering dependency: {{engineering_dependency}}
Security dependency: {{security_dependency}}
Data dependency: {{data_dependency}}
Third-party dependency: {{third_party_dependency}}
```

---

# 17. Risks and Open Questions

Risks:

```text
Risk 1: {{risk_1}}
Risk 2: {{risk_2}}
Risk 3: {{risk_3}}
```

Open questions:

```text
Question 1: {{open_question_1}}
Question 2: {{open_question_2}}
Question 3: {{open_question_3}}
```

---

# 18. Release Plan

Define release approach.

```text
Release type: {{release_type}}
Feature flag needed: {{feature_flag_needed}}
Beta users: {{beta_users}}
Rollout plan: {{rollout_plan}}
Rollback plan: {{rollback_plan}}
Support notes: {{support_notes}}
```

---

# 19. Review and Approval

```text
Product approval: {{product_approval}}
Design approval: {{design_approval}}
Engineering approval: {{engineering_approval}}
Security approval: {{security_approval}}
Operations approval: {{operations_approval}}
```

---

# 20. Final Principle

> A PRD should remove ambiguity before implementation begins.
