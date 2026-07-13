## FILE: `templates/design/ux-flow-template/TEMPLATE.md`

# UX Flow Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
Flow Name: {{flow_name}}
Product Area: {{product_area}}
Owner: {{owner}}
UX Owner: {{ux_owner}}
Product Owner: {{product_owner}}
Engineering Owner: {{engineering_owner}}
Status: {{status}}
Version: {{version}}
Last Updated: {{last_updated}}
Target Release: {{target_release}}
```

---

# 2. Flow Summary

Summarize the user flow.

```text
{{flow_summary}}
```

Recommended format:

```text
This flow helps {{primary_user}} move from {{entry_point}} to {{desired_outcome}} by completing {{core_actions}}.
```

---

# 3. User Goal

```text
Primary user: {{primary_user}}
User goal: {{user_goal}}
User motivation: {{user_motivation}}
Success for the user: {{user_success}}
```

---

# 4. Business Goal

```text
Business goal:
{{business_goal}}

Activation or conversion goal:
{{activation_or_conversion_goal}}

Success metric:
{{success_metric}}
```

---

# 5. Entry Points

```text
Entry point 1: {{entry_point_1}}
Entry point 2: {{entry_point_2}}
Entry point 3: {{entry_point_3}}
```

Examples:

```text
signup completion
empty dashboard
project detail page
email link
notification
admin console
```

---

# 6. Exit Points

```text
Successful exit:
{{successful_exit}}

Alternative exit:
{{alternative_exit}}

Abandonment point:
{{abandonment_point}}
```

---

# 7. Flow Steps

```text
Step | Screen / State | User Action | System Response | Next Step
1 | {{screen_1}} | {{user_action_1}} | {{system_response_1}} | {{next_step_1}}
2 | {{screen_2}} | {{user_action_2}} | {{system_response_2}} | {{next_step_2}}
3 | {{screen_3}} | {{user_action_3}} | {{system_response_3}} | {{next_step_3}}
```

---

# 8. Screen Requirements

## Screen 1 — {{screen_1}}

Purpose:

```text
{{screen_1_purpose}}
```

Required elements:

```text
{{screen_1_element_1}}
{{screen_1_element_2}}
{{screen_1_element_3}}
```

Primary action:

```text
{{screen_1_primary_action}}
```

Secondary actions:

```text
{{screen_1_secondary_actions}}
```

---

## Screen 2 — {{screen_2}}

Purpose:

```text
{{screen_2_purpose}}
```

Required elements:

```text
{{screen_2_element_1}}
{{screen_2_element_2}}
{{screen_2_element_3}}
```

Primary action:

```text
{{screen_2_primary_action}}
```

Secondary actions:

```text
{{screen_2_secondary_actions}}
```

---

# 9. States

Define all required states.

```text
Default state:
{{default_state}}

Empty state:
{{empty_state}}

Loading state:
{{loading_state}}

Success state:
{{success_state}}

Error state:
{{error_state}}

Permission denied state:
{{permission_denied_state}}

Offline or unavailable state:
{{unavailable_state}}
```

---

# 10. Validation and Errors

```text
Validation rule 1:
{{validation_rule_1}}

Validation rule 2:
{{validation_rule_2}}

Error message 1:
{{error_message_1}}

Error message 2:
{{error_message_2}}
```

Error messages should be:

```text
clear
specific
safe
actionable
non-technical where possible
```

---

# 11. Permissions and Access

```text
Roles allowed:
- {{allowed_role_1}}
- {{allowed_role_2}}

Roles denied:
- {{denied_role_1}}
- {{denied_role_2}}

Permission required:
{{permission_required}}

Tenant boundary:
{{tenant_boundary}}
```

---

# 12. Data Requirements

```text
Data displayed:
{{data_displayed}}

Data created:
{{data_created}}

Data updated:
{{data_updated}}

Data deleted:
{{data_deleted}}

Sensitive data:
{{sensitive_data}}
```

---

# 13. Notifications and Side Effects

```text
Notifications:
{{notifications}}

Background jobs:
{{background_jobs}}

Audit events:
{{audit_events}}

External integrations:
{{external_integrations}}
```

---

# 14. Analytics

Track events:

```text
{{event_1}}
{{event_2}}
{{event_3}}
```

Recommended event format:

```text
event name
actor
resource
workspace or tenant
timestamp
result
metadata
```

---

# 15. Edge Cases

```text
Edge case 1:
{{edge_case_1}}

Expected behavior:
{{edge_case_behavior_1}}

Edge case 2:
{{edge_case_2}}

Expected behavior:
{{edge_case_behavior_2}}
```

---

# 16. Accessibility Notes

```text
Keyboard navigation:
{{keyboard_navigation}}

Screen reader notes:
{{screen_reader_notes}}

Color contrast notes:
{{color_contrast_notes}}

Focus state notes:
{{focus_state_notes}}

Error accessibility:
{{error_accessibility}}
```

---

# 17. Acceptance Criteria

```text
AC-001:
Given {{condition_1}}
When {{action_1}}
Then {{expected_result_1}}

AC-002:
Given {{condition_2}}
When {{action_2}}
Then {{expected_result_2}}
```

---

# 18. Open Questions

```text
Question 1: {{open_question_1}}
Question 2: {{open_question_2}}
Question 3: {{open_question_3}}
```

---

# 19. Approval

```text
Product approval: {{product_approval}}
Design approval: {{design_approval}}
Engineering approval: {{engineering_approval}}
Security approval: {{security_approval}}
QA approval: {{qa_approval}}
```

---

# 20. Final Principle

> A UX flow should remove ambiguity between what the user sees, what the user does and what the system does.
