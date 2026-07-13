## FILE: `templates/operations/release-plan-template/variables.md`

# Release Plan Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{release_name}}
{{release_version}}
{{release_owner}}
{{technical_owner}}
{{product_owner}}
{{status}}
{{target_release_date}}
{{release_summary}}
{{included_change_1}}
{{risk_level}}
{{test_status}}
{{deployment_step_1}}
{{validation_check_1}}
{{rollback_trigger}}
{{monitoring_window}}
```

---

# 2. Optional Variables

```text
{{release_window}}
{{feature_flag_name}}
{{database_migration_included}}
{{security_reviewer}}
{{status_page_update_required}}
{{pre_release_message}}
{{rollback_message}}
{{review_date}}
```

---

# 3. Variable Descriptions

## `{{release_name}}`

Purpose:

```text
Human-readable name of the release.
```

Example:

```text
Project Submission Release
```

---

## `{{release_version}}`

Purpose:

```text
Version or release identifier.
```

Example:

```text
v0.2.0
```

---

## `{{risk_level}}`

Purpose:

```text
Overall release risk classification.
```

Recommended values:

```text
low
medium
high
critical
```

---

## `{{deployment_step_1}}`

Purpose:

```text
First concrete deployment action.
```

Example:

```text
Deploy backend service version v0.2.0 to production.
```

---

## `{{rollback_trigger}}`

Purpose:

```text
Condition that requires rollback or mitigation.
```

Example:

```text
Submission API error rate remains above 5% for more than 5 minutes.
```

---

# 4. Final Principle

> Release Plan variables should make production change explicit, owned and reversible where possible.
