## FILE: `templates/engineering/api-contract-template/variables.md`

# API Contract Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{api_name}}
{{owner}}
{{status}}
{{api_version}}
{{http_method}}
{{endpoint_path}}
{{summary}}
{{authentication_required}}
{{authorization_required}}
{{success_status_code}}
{{success_response_example}}
{{error_responses}}
```

---

# 2. Optional Variables

```text
{{target_release}}
{{content_type}}
{{service_account_supported}}
{{pagination_type}}
{{rate_limit}}
{{idempotency_required}}
{{background_jobs}}
{{audit_events}}
{{external_provider_calls}}
{{deprecation_notes}}
```

---

# 3. Variable Descriptions

## `{{api_name}}`

Purpose:

```text
Human-readable API contract name.
```

Example:

```text
Submit Project API
```

---

## `{{endpoint_path}}`

Purpose:

```text
HTTP path for the endpoint.
```

Example:

```text
/api/v1/projects/{{project_id}}/submit
```

---

## `{{required_permission}}`

Purpose:

```text
Permission needed to perform the API action.
```

Example:

```text
project.submit
```

---

## `{{request_body_example}}`

Purpose:

```text
Example JSON request body.
```

Example:

```json
{
  "submission_note": "Ready for review"
}
```

---

## `{{success_response_example}}`

Purpose:

```text
Example JSON response body for a successful request.
```

Example:

```json
{
  "project_id": "prj_123",
  "status": "submitted"
}
```

---

# 4. Final Principle

> API contract variables should make implementation and testing precise.
