## FILE: `templates/design/ux-flow-template/variables.md`

# UX Flow Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{flow_name}}
{{product_area}}
{{owner}}
{{ux_owner}}
{{status}}
{{flow_summary}}
{{primary_user}}
{{user_goal}}
{{entry_point_1}}
{{successful_exit}}
{{screen_1}}
{{user_action_1}}
{{system_response_1}}
{{success_metric}}
```

---

# 2. Optional Variables

```text
{{target_release}}
{{business_goal}}
{{permission_required}}
{{tenant_boundary}}
{{audit_events}}
{{external_integrations}}
{{screen_reader_notes}}
{{security_approval}}
```

---

# 3. Variable Descriptions

## `{{flow_name}}`

Purpose:

```text
Name of the user flow.
```

Example:

```text
Guided First Project Setup
```

---

## `{{primary_user}}`

Purpose:

```text
Main user following the flow.
```

Example:

```text
Independent film producer
```

---

## `{{entry_point_1}}`

Purpose:

```text
Where the user starts the flow.
```

Example:

```text
Empty dashboard after signup
```

---

## `{{successful_exit}}`

Purpose:

```text
Desired end state of the flow.
```

Example:

```text
User creates first project and reaches the project readiness checklist.
```

---

# 4. Final Principle

> UX Flow variables should clarify the path from user intent to product value.
