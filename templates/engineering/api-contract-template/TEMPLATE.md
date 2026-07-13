## FILE: `templates/engineering/api-contract-template/TEMPLATE.md`

# API Contract Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
API Name: {{api_name}}
Endpoint Owner: {{owner}}
Status: {{status}}
Version: {{api_version}}
Last Updated: {{last_updated}}
Target Release: {{target_release}}
```

---

# 2. Summary

Describe the API purpose.

```text
{{summary}}
```

Recommended format:

```text
This API allows {{client_or_user}} to {{action}} for {{business_purpose}}.
```

---

# 3. Endpoint

```text
Method: {{http_method}}
Path: {{endpoint_path}}
Version: {{api_version}}
Content Type: {{content_type}}
Authentication Required: {{authentication_required}}
Authorization Required: {{authorization_required}}
```

Example:

```text
POST /api/v1/projects/{{project_id}}/submit
```

---

# 4. Use Case

Describe the primary use case.

```text
As a {{user_role}}, I want to {{user_action}} so that {{user_outcome}}.
```

---

# 5. Authentication

Define authentication requirements.

```text
Authentication type: {{authentication_type}}
Token required: {{token_required}}
Session required: {{session_required}}
Service account supported: {{service_account_supported}}
```

---

# 6. Authorization

Define permission requirements.

```text
Required role: {{required_role}}
Required permission: {{required_permission}}
Resource scope: {{resource_scope}}
Tenant boundary: {{tenant_boundary}}
Ownership rule: {{ownership_rule}}
```

Example:

```text
User must have project.submit permission in the same workspace as the project.
```

---

# 7. Request Parameters

## 7.1 Path Parameters

```text
{{path_parameter_name}}:
  Type: {{path_parameter_type}}
  Required: {{path_parameter_required}}
  Description: {{path_parameter_description}}
```

## 7.2 Query Parameters

```text
{{query_parameter_name}}:
  Type: {{query_parameter_type}}
  Required: {{query_parameter_required}}
  Default: {{query_parameter_default}}
  Description: {{query_parameter_description}}
```

## 7.3 Headers

```text
{{header_name}}:
  Required: {{header_required}}
  Description: {{header_description}}
```

---

# 8. Request Body

```json
{{request_body_example}}
```

Schema:

```text
Field: {{field_name}}
Type: {{field_type}}
Required: {{field_required}}
Validation: {{field_validation}}
Description: {{field_description}}
```

---

# 9. Successful Response

HTTP status:

```text
{{success_status_code}}
```

Response body:

```json
{{success_response_example}}
```

Response schema:

```text
Field: {{response_field_name}}
Type: {{response_field_type}}
Nullable: {{response_field_nullable}}
Description: {{response_field_description}}
```

---

# 10. Error Responses

Use the standard API error envelope.

```json
{
  "error": {
    "code": "{{error_code}}",
    "message": "{{error_message}}",
    "details": [],
    "request_id": "{{request_id}}",
    "documentation_url": "{{documentation_url}}"
  }
}
```

Error table:

```text
Status | Code | Condition | Safe Message
400 | validation_failed | {{validation_condition}} | {{validation_message}}
401 | authentication_required | {{auth_condition}} | {{auth_message}}
403 | permission_denied | {{permission_condition}} | {{permission_message}}
404 | resource_not_found | {{not_found_condition}} | {{not_found_message}}
409 | conflict | {{conflict_condition}} | {{conflict_message}}
500 | internal_error | {{internal_condition}} | {{internal_message}}
```

---

# 11. Pagination

If the endpoint returns lists, define pagination.

```text
Pagination type: {{pagination_type}}
Page size default: {{page_size_default}}
Page size maximum: {{page_size_maximum}}
Cursor field: {{cursor_field}}
Sort order: {{sort_order}}
```

Response example:

```json
{
  "data": [],
  "pagination": {
    "next_cursor": "{{next_cursor}}",
    "has_more": true
  }
}
```

---

# 12. Filtering and Sorting

```text
Supported filters:
- {{filter_1}}
- {{filter_2}}

Supported sort fields:
- {{sort_field_1}}
- {{sort_field_2}}

Default sort:
{{default_sort}}
```

---

# 13. Idempotency

Define idempotency if the endpoint creates or triggers side effects.

```text
Idempotency required: {{idempotency_required}}
Idempotency key source: {{idempotency_key_source}}
Duplicate request behavior: {{duplicate_request_behavior}}
```

---

# 14. Rate Limits

```text
Rate limit: {{rate_limit}}
Scope: {{rate_limit_scope}}
Exceeded behavior: {{rate_limit_exceeded_behavior}}
```

---

# 15. Side Effects

List side effects.

```text
Database changes:
{{database_changes}}

Background jobs:
{{background_jobs}}

Notifications:
{{notifications}}

Audit events:
{{audit_events}}

External provider calls:
{{external_provider_calls}}
```

---

# 16. Observability

```text
Logs:
{{log_events}}

Metrics:
{{metrics}}

Trace fields:
{{trace_fields}}

Request id required:
{{request_id_required}}
```

---

# 17. Versioning and Compatibility

```text
API version: {{api_version}}
Backward compatible: {{backward_compatible}}
Breaking change: {{breaking_change}}
Deprecation notes: {{deprecation_notes}}
Migration notes: {{migration_notes}}
```

---

# 18. Test Cases

```text
TC-001 Success:
Given {{success_condition}}
When {{success_action}}
Then {{success_expected_result}}

TC-002 Validation:
Given {{validation_condition}}
When {{validation_action}}
Then {{validation_expected_result}}

TC-003 Authorization:
Given {{authorization_condition}}
When {{authorization_action}}
Then {{authorization_expected_result}}

TC-004 Tenant Isolation:
Given {{tenant_condition}}
When {{tenant_action}}
Then {{tenant_expected_result}}
```

---

# 19. Open Questions

```text
Question 1: {{open_question_1}}
Question 2: {{open_question_2}}
Question 3: {{open_question_3}}
```

---

# 20. Review and Approval

```text
Backend approval: {{backend_approval}}
Frontend approval: {{frontend_approval}}
Security approval: {{security_approval}}
QA approval: {{qa_approval}}
Product approval: {{product_approval}}
```

---

# 21. Final Principle

> API contracts should define behavior, not just routes.