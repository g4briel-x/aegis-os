## FILE: `templates/security/security-review-template/TEMPLATE.md`

# Security Review Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
Review Name: {{review_name}}
Feature / System: {{feature_or_system}}
Review Owner: {{review_owner}}
Engineering Owner: {{engineering_owner}}
Security Reviewer: {{security_reviewer}}
Status: {{status}}
Version: {{version}}
Review Date: {{review_date}}
Target Release: {{target_release}}
```

---

# 2. Review Summary

Summarize what is being reviewed.

```text
{{review_summary}}
```

Recommended format:

```text
This review evaluates {{feature_or_system}} for {{security_scope}} before {{release_context}}.
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

# 4. System Context

```text
System or feature: {{feature_or_system}}
User roles involved: {{user_roles}}
Resources involved: {{resources}}
Data involved: {{data_involved}}
External systems: {{external_systems}}
Deployment environment: {{deployment_environment}}
```

---

# 5. Security Classification

```text
Security risk level: {{security_risk_level}}
Classification reason: {{classification_reason}}
Sensitive data involved: {{sensitive_data_involved}}
Customer data involved: {{customer_data_involved}}
Tenant-scoped data involved: {{tenant_scoped_data_involved}}
Privileged action involved: {{privileged_action_involved}}
```

Recommended risk levels:

```text
low
medium
high
critical
```

---

# 6. Authentication Review

```text
Authentication required: {{authentication_required}}
Authentication method: {{authentication_method}}
Session or token behavior: {{session_or_token_behavior}}
Service account access: {{service_account_access}}
Unauthenticated behavior: {{unauthenticated_behavior}}
```

Review questions:

```text
Can anonymous users access protected resources?
Are tokens validated correctly?
Are expired sessions rejected?
Are service accounts scoped correctly?
```

---

# 7. Authorization Review

```text
Required roles:
- {{required_role_1}}
- {{required_role_2}}

Required permissions:
- {{required_permission_1}}
- {{required_permission_2}}

Resource ownership rule:
{{resource_ownership_rule}}

Denied behavior:
{{denied_behavior}}
```

Review questions:

```text
Can users access only allowed resources?
Are admin actions protected?
Are permission checks enforced server-side?
Are role changes audited?
```

---

# 8. Tenant Isolation Review

```text
Tenant model: {{tenant_model}}
Tenant boundary: {{tenant_boundary}}
Tenant identifier: {{tenant_identifier}}
Cross-tenant access prevention: {{cross_tenant_access_prevention}}
Tenant isolation tests: {{tenant_isolation_tests}}
```

Required checks:

```text
same-tenant access allowed
cross-tenant read denied
cross-tenant write denied
cross-tenant file access denied
cross-tenant background job processing denied
```

---

# 9. Data Protection Review

```text
Data types:
{{data_types}}

Sensitive fields:
{{sensitive_fields}}

Storage location:
{{storage_location}}

Encryption at rest:
{{encryption_at_rest}}

Encryption in transit:
{{encryption_in_transit}}

Retention rule:
{{retention_rule}}

Deletion rule:
{{deletion_rule}}
```

---

# 10. API and Input Validation Review

```text
API endpoints:
- {{api_endpoint_1}}
- {{api_endpoint_2}}

Input validation:
{{input_validation}}

Output filtering:
{{output_filtering}}

Error behavior:
{{error_behavior}}

Rate limiting:
{{rate_limiting}}
```

Required checks:

```text
invalid input rejected
unsafe file type rejected
oversized payload rejected
internal errors hidden
safe error code returned
request id included
```

---

# 11. File Upload and Export Review

Use this section if files are involved.

```text
File upload allowed: {{file_upload_allowed}}
Allowed file types: {{allowed_file_types}}
Max file size: {{max_file_size}}
File scanning required: {{file_scanning_required}}
Private storage: {{private_storage}}
Signed URL behavior: {{signed_url_behavior}}
Export controls: {{export_controls}}
```

---

# 12. Audit Logging Review

```text
Audit events required:
- {{audit_event_1}}
- {{audit_event_2}}

Audit fields:
{{audit_fields}}

Audit retention:
{{audit_retention}}

Audit access control:
{{audit_access_control}}
```

Audit events should capture:

```text
actor
action
resource
tenant
timestamp
result
request_id
source_ip if appropriate
```

---

# 13. Abuse and Threat Scenarios

```text
Threat 1: {{threat_1}}
Impact: {{threat_impact_1}}
Mitigation: {{threat_mitigation_1}}

Threat 2: {{threat_2}}
Impact: {{threat_impact_2}}
Mitigation: {{threat_mitigation_2}}
```

Common scenarios:

```text
privilege escalation
cross-tenant data access
mass assignment
insecure direct object reference
unsafe file upload
token misuse
rate limit abuse
data export abuse
```

---

# 14. Dependency and Integration Review

```text
Third-party systems: {{third_party_systems}}
Secrets required: {{secrets_required}}
Webhook verification: {{webhook_verification}}
Provider permissions: {{provider_permissions}}
Failure behavior: {{provider_failure_behavior}}
```

---

# 15. Security Test Cases

```text
TC-SEC-001:
Scenario: {{security_test_scenario_1}}
Given {{condition_1}}
When {{action_1}}
Then {{expected_result_1}}

TC-SEC-002:
Scenario: {{security_test_scenario_2}}
Given {{condition_2}}
When {{action_2}}
Then {{expected_result_2}}
```

---

# 16. Findings

```text
Finding ID | Severity | Finding | Recommendation | Owner | Status
{{finding_id_1}} | {{finding_severity_1}} | {{finding_1}} | {{recommendation_1}} | {{finding_owner_1}} | {{finding_status_1}}
{{finding_id_2}} | {{finding_severity_2}} | {{finding_2}} | {{recommendation_2}} | {{finding_owner_2}} | {{finding_status_2}}
```

---

# 17. Release Decision

```text
Security decision: {{security_decision}}
Decision reason: {{decision_reason}}
Accepted risks: {{accepted_risks}}
Required fixes before release: {{required_fixes_before_release}}
Follow-up fixes after release: {{follow_up_fixes_after_release}}
```

Recommended decision values:

```text
approved
approved_with_conditions
blocked
needs_more_review
```

---

# 18. Approval

```text
Security approval: {{security_approval}}
Engineering approval: {{engineering_approval}}
Product approval: {{product_approval}}
Operations approval: {{operations_approval}}
```

---

# 19. Final Principle

> A security review should end with a clear release decision, not only a list of concerns.
