## FILE: `templates/engineering/data-model-template/variables.md`

# Data Model Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{model_name}}
{{domain}}
{{owner}}
{{status}}
{{model_summary}}
{{business_process}}
{{entity_1}}
{{entity_1_purpose}}
{{field_1_name}}
{{field_1_type}}
{{tenant_model}}
{{tenant_boundary}}
{{ownership_rule}}
```

---

# 2. Optional Variables

```text
{{target_release}}
{{security_reviewer}}
{{retention_rule}}
{{deletion_rule}}
{{audit_event_1}}
{{migration_required}}
{{backfill_required}}
{{validation_query}}
```

---

# 3. Variable Descriptions

## `{{model_name}}`

Purpose:

```text
Name of the data model being designed.
```

Example:

```text
Project Readiness Data Model
```

---

## `{{entity_1}}`

Purpose:

```text
Main data object in the model.
```

Example:

```text
Project
```

---

## `{{tenant_boundary}}`

Purpose:

```text
Rule that defines how tenant data is separated.
```

Example:

```text
Every project must belong to one workspace_id. Users can access only projects in their active workspace.
```

---

## `{{ownership_rule}}`

Purpose:

```text
Rule that defines which actor, workspace or organization owns the data.
```

Example:

```text
A project is owned by the workspace that created it.
```

---

# 4. Final Principle

> Data Model variables should make ownership, access and persistence rules explicit.

