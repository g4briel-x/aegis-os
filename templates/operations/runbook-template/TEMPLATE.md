## FILE: `templates/operations/runbook-template/TEMPLATE.md`

# Runbook Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
Runbook Name: {{runbook_name}}
System / Service: {{system_or_service}}
Owner: {{owner}}
Operational Owner: {{operational_owner}}
Status: {{status}}
Version: {{version}}
Last Updated: {{last_updated}}
Review Date: {{review_date}}
```

---

# 2. Purpose

Describe what this runbook helps operators do.

```text
{{purpose}}
```

Recommended format:

```text
This runbook explains how to {{operation}} for {{system_or_service}} when {{trigger_condition}}.
```

---

# 3. Scope

## 3.1 In Scope

```text
{{in_scope_item_1}}
{{in_scope_item_2}}
{{in_scope_item_3}}
```

## 3.2 Out of Scope

```text
{{out_of_scope_item_1}}
{{out_of_scope_item_2}}
{{out_of_scope_item_3}}
```

---

# 4. Trigger Conditions

Use this runbook when:

```text
{{trigger_condition_1}}
{{trigger_condition_2}}
{{trigger_condition_3}}
```

Do not use this runbook when:

```text
{{non_trigger_condition_1}}
{{non_trigger_condition_2}}
```

---

# 5. Severity and Priority

```text
Default Severity: {{default_severity}}
Priority: {{priority}}
Customer Impact: {{customer_impact}}
Business Impact: {{business_impact}}
Security Impact: {{security_impact}}
```

---

# 6. Required Access

```text
Required role: {{required_role}}
Required permission: {{required_permission}}
Required systems:
- {{required_system_1}}
- {{required_system_2}}

Sensitive access notes:
{{sensitive_access_notes}}
```

---

# 7. Prerequisites

Before starting, confirm:

```text
[ ] {{prerequisite_1}}
[ ] {{prerequisite_2}}
[ ] {{prerequisite_3}}
```

---

# 8. Safety Checks

Do not proceed unless:

```text
[ ] Backup or recovery path is understood if needed
[ ] Customer impact is understood
[ ] Required approval is obtained if needed
[ ] Current system state is captured
[ ] Operator understands rollback or stop condition
```

---

# 9. Step-by-Step Procedure

## Step 1 — {{step_1_title}}

Purpose:

```text
{{step_1_purpose}}
```

Action:

```text
{{step_1_action}}
```

Expected result:

```text
{{step_1_expected_result}}
```

If this fails:

```text
{{step_1_failure_action}}
```

---

## Step 2 — {{step_2_title}}

Purpose:

```text
{{step_2_purpose}}
```

Action:

```text
{{step_2_action}}
```

Expected result:

```text
{{step_2_expected_result}}
```

If this fails:

```text
{{step_2_failure_action}}
```

---

## Step 3 — {{step_3_title}}

Purpose:

```text
{{step_3_purpose}}
```

Action:

```text
{{step_3_action}}
```

Expected result:

```text
{{step_3_expected_result}}
```

If this fails:

```text
{{step_3_failure_action}}
```

---

# 10. Validation

After execution, validate:

```text
[ ] {{validation_check_1}}
[ ] {{validation_check_2}}
[ ] {{validation_check_3}}
```

Validation commands or queries:

```text
{{validation_command_or_query}}
```

---

# 11. Rollback or Recovery

Rollback condition:

```text
{{rollback_condition}}
```

Rollback steps:

```text
1. {{rollback_step_1}}
2. {{rollback_step_2}}
3. {{rollback_step_3}}
```

Recovery notes:

```text
{{recovery_notes}}
```

---

# 12. Escalation

Escalate when:

```text
{{escalation_condition_1}}
{{escalation_condition_2}}
{{escalation_condition_3}}
```

Escalation contacts:

```text
Technical Lead: {{technical_lead}}
Security Lead: {{security_lead}}
Operations Lead: {{operations_lead}}
Product Owner: {{product_owner}}
Support Contact: {{support_contact}}
```

---

# 13. Communication

Internal communication:

```text
{{internal_communication_channel}}
```

Customer communication:

```text
{{customer_communication_rule}}
```

Status update frequency:

```text
{{status_update_frequency}}
```

---

# 14. Observability

Relevant dashboards:

```text
{{dashboard_link_1}}
{{dashboard_link_2}}
```

Relevant logs:

```text
{{log_location}}
```

Relevant metrics:

```text
{{metric_1}}
{{metric_2}}
{{metric_3}}
```

Relevant alerts:

```text
{{alert_1}}
{{alert_2}}
```

---

# 15. Audit and Evidence

Record:

```text
operator
time started
time completed
commands executed
records changed
approval received
customer impact
final status
```

Evidence location:

```text
{{evidence_location}}
```

---

# 16. Known Risks

```text
Risk 1: {{risk_1}}
Mitigation: {{mitigation_1}}

Risk 2: {{risk_2}}
Mitigation: {{mitigation_2}}
```

---

# 17. Review History

```text
Date | Reviewer | Change | Decision
{{review_date}} | {{reviewer}} | {{review_change}} | {{review_decision}}
```

---

# 18. Final Principle

> A runbook should turn operational knowledge into safe repeatable action.
