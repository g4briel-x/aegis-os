## FILE: `templates/operations/runbook-template/variables.md`

# Runbook Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{runbook_name}}
{{system_or_service}}
{{owner}}
{{operational_owner}}
{{purpose}}
{{trigger_condition_1}}
{{required_role}}
{{prerequisite_1}}
{{step_1_title}}
{{step_1_action}}
{{step_1_expected_result}}
{{validation_check_1}}
{{rollback_condition}}
{{escalation_condition_1}}
```

---

# 2. Optional Variables

```text
{{default_severity}}
{{customer_impact}}
{{business_impact}}
{{security_impact}}
{{dashboard_link_1}}
{{log_location}}
{{metric_1}}
{{alert_1}}
{{evidence_location}}
{{support_contact}}
```

---

# 3. Variable Descriptions

## `{{runbook_name}}`

Purpose:

```text
Name of the operational procedure.
```

Example:

```text
Restart Failed Background Worker
```

---

## `{{system_or_service}}`

Purpose:

```text
Service, workflow, system or component covered by the runbook.
```

Example:

```text
Project Review Worker
```

---

## `{{trigger_condition_1}}`

Purpose:

```text
Specific condition that tells an operator to use this runbook.
```

Example:

```text
Reviewer assignment jobs are stuck in pending state for more than 15 minutes.
```

---

## `{{step_1_action}}`

Purpose:

```text
Concrete action the operator must perform.
```

Example:

```text
Check the worker queue depth in the production dashboard.
```

---

## `{{validation_check_1}}`

Purpose:

```text
Expected verification after the procedure.
```

Example:

```text
Queue depth decreases and new jobs are processed successfully.
```

---

# 4. Final Principle

> Runbook variables should make operational action explicit and verifiable.
