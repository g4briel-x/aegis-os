## FILE: `templates/engineering/data-model-template/TEMPLATE.md`

# Data Model Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
Model Name: {{model_name}}
Domain: {{domain}}
Owner: {{owner}}
Database Owner: {{database_owner}}
Security Reviewer: {{security_reviewer}}
Status: {{status}}
Version: {{version}}
Last Updated: {{last_updated}}
Target Release: {{target_release}}
```

---

# 2. Model Summary

Summarize the data model.

```text
{{model_summary}}
```

Recommended format:

```text
This data model represents {{domain_object}} for {{business_purpose}} and is owned by {{owning_domain}}.
```

---

# 3. Business Context

```text
Business process:
{{business_process}}

User problem:
{{user_problem}}

Product capability:
{{product_capability}}

Primary users:
{{primary_users}}

Business rules:
{{business_rules}}
```

---

# 4. Domain Entities

List the main entities.

```text
Entity | Purpose | Owner | Tenant-Scoped | Lifecycle
{{entity_1}} | {{entity_1_purpose}} | {{entity_1_owner}} | {{entity_1_tenant_scoped}} | {{entity_1_lifecycle}}
{{entity_2}} | {{entity_2_purpose}} | {{entity_2_owner}} | {{entity_2_tenant_scoped}} | {{entity_2_lifecycle}}
```

---

# 5. Entity Detail

## Entity — {{entity_1}}

Purpose:

```text
{{entity_1_purpose}}
```

Table or collection name:

```text
{{entity_1_table_name}}
```

Primary key:

```text
{{entity_1_primary_key}}
```

Tenant key:

```text
{{entity_1_tenant_key}}
```

Owner relationship:

```text
{{entity_1_owner_relationship}}
```

Lifecycle states:

```text
{{entity_1_state_1}}
{{entity_1_state_2}}
{{entity_1_state_3}}
```

---

# 6. Fields

```text
Field | Type | Required | Default | Description | Sensitive
{{field_1_name}} | {{field_1_type}} | {{field_1_required}} | {{field_1_default}} | {{field_1_description}} | {{field_1_sensitive}}
{{field_2_name}} | {{field_2_type}} | {{field_2_required}} | {{field_2_default}} | {{field_2_description}} | {{field_2_sensitive}}
```

Field quality rules:

```text
field names are explicit
types are stable
required fields are justified
defaults are intentional
sensitive fields are marked
```

---

# 7. Relationships

```text
Relationship | From | To | Cardinality | Required | Delete Behavior
{{relationship_1}} | {{from_entity_1}} | {{to_entity_1}} | {{cardinality_1}} | {{required_1}} | {{delete_behavior_1}}
{{relationship_2}} | {{from_entity_2}} | {{to_entity_2}} | {{cardinality_2}} | {{required_2}} | {{delete_behavior_2}}
```

Cardinality examples:

```text
one_to_one
one_to_many
many_to_many
belongs_to
has_many
```

---

# 8. Tenant and Ownership Model

```text
Tenant model:
{{tenant_model}}

Tenant boundary:
{{tenant_boundary}}

Tenant identifier:
{{tenant_identifier}}

Ownership rule:
{{ownership_rule}}

Cross-tenant access rule:
{{cross_tenant_access_rule}}
```

Required checks:

```text
same-tenant access allowed
cross-tenant read denied
cross-tenant write denied
background jobs preserve tenant scope
exports preserve tenant scope
```

---

# 9. Constraints and Indexes

## 9.1 Constraints

```text
Constraint | Fields | Type | Reason
{{constraint_1}} | {{constraint_1_fields}} | {{constraint_1_type}} | {{constraint_1_reason}}
{{constraint_2}} | {{constraint_2_fields}} | {{constraint_2_type}} | {{constraint_2_reason}}
```

Constraint types:

```text
primary_key
foreign_key
unique
not_null
check
enum
```

## 9.2 Indexes

```text
Index | Fields | Type | Reason
{{index_1}} | {{index_1_fields}} | {{index_1_type}} | {{index_1_reason}}
{{index_2}} | {{index_2_fields}} | {{index_2_type}} | {{index_2_reason}}
```

---

# 10. Lifecycle and State Transitions

```text
State | Meaning | Allowed Transitions | Owner
{{state_1}} | {{state_1_meaning}} | {{state_1_transitions}} | {{state_1_owner}}
{{state_2}} | {{state_2_meaning}} | {{state_2_transitions}} | {{state_2_owner}}
```

Invalid transitions:

```text
{{invalid_transition_1}}
{{invalid_transition_2}}
```

---

# 11. Permissions

```text
Action | Required Permission | Allowed Roles | Tenant Rule
create | {{create_permission}} | {{create_roles}} | {{create_tenant_rule}}
read | {{read_permission}} | {{read_roles}} | {{read_tenant_rule}}
update | {{update_permission}} | {{update_roles}} | {{update_tenant_rule}}
delete | {{delete_permission}} | {{delete_roles}} | {{delete_tenant_rule}}
```

---

# 12. Audit Events

```text
Audit Event | Trigger | Required Fields
{{audit_event_1}} | {{audit_trigger_1}} | {{audit_fields_1}}
{{audit_event_2}} | {{audit_trigger_2}} | {{audit_fields_2}}
```

Recommended audit fields:

```text
actor_id
workspace_id
resource_type
resource_id
action
result
timestamp
request_id
```

---

# 13. Data Retention and Deletion

```text
Retention rule:
{{retention_rule}}

Deletion rule:
{{deletion_rule}}

Soft delete required:
{{soft_delete_required}}

Hard delete allowed:
{{hard_delete_allowed}}

Export required:
{{export_required}}

Anonymization required:
{{anonymization_required}}
```

---

# 14. API and Application Usage

```text
Used by APIs:
- {{api_1}}
- {{api_2}}

Used by screens:
- {{screen_1}}
- {{screen_2}}

Used by background jobs:
- {{background_job_1}}
- {{background_job_2}}

Used by reports:
- {{report_1}}
- {{report_2}}
```

---

# 15. Migration Plan

```text
Migration required: {{migration_required}}
Migration type: {{migration_type}}
Backward compatible: {{backward_compatible}}
Backfill required: {{backfill_required}}
Rollback or recovery: {{rollback_or_recovery}}
Validation query: {{validation_query}}
```

---

# 16. Risks and Open Questions

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

# 17. Approval

```text
Product approval: {{product_approval}}
Architecture approval: {{architecture_approval}}
Database approval: {{database_approval}}
Security approval: {{security_approval}}
Engineering approval: {{engineering_approval}}
```

---

# 18. Final Principle

> A data model should protect meaning, integrity and access boundaries at the same time.
