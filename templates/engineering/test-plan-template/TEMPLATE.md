## FILE: `templates/engineering/test-plan-template/TEMPLATE.md`

# Test Plan Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
Feature / Change Name: {{change_name}}
Product Area: {{product_area}}
Owner: {{owner}}
Test Owner: {{test_owner}}
Status: {{status}}
Version: {{version}}
Last Updated: {{last_updated}}
Target Release: {{target_release}}
```

---

# 2. Summary

Describe what will be tested and why.

```text
{{summary}}
```

Recommended format:

```text
This test plan validates {{change_name}} to ensure {{quality_goal}} before {{release_context}}.
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

# 4. References

```text
PRD: {{prd_link}}
API Contract: {{api_contract_link}}
Design: {{design_link}}
Architecture Notes: {{architecture_link}}
Security Notes: {{security_link}}
Release Plan: {{release_plan_link}}
```

---

# 5. Test Objectives

```text
Objective 1: {{test_objective_1}}
Objective 2: {{test_objective_2}}
Objective 3: {{test_objective_3}}
```

---

# 6. Test Strategy

Define the testing approach.

```text
Unit tests: {{unit_test_strategy}}
Integration tests: {{integration_test_strategy}}
API tests: {{api_test_strategy}}
End-to-end tests: {{e2e_test_strategy}}
Manual tests: {{manual_test_strategy}}
Regression tests: {{regression_test_strategy}}
Security tests: {{security_test_strategy}}
Performance tests: {{performance_test_strategy}}
```

---

# 7. Test Environment

```text
Environment: {{test_environment}}
Application version: {{application_version}}
Database version: {{database_version}}
Feature flags: {{feature_flags}}
Test accounts: {{test_accounts}}
External providers: {{external_providers}}
Test data source: {{test_data_source}}
```

---

# 8. Test Data

Define required test data.

```text
Users:
- {{test_user_1}}
- {{test_user_2}}

Tenants / Workspaces:
- {{test_tenant_1}}
- {{test_tenant_2}}

Records:
- {{test_record_1}}
- {{test_record_2}}

Files:
- {{test_file_1}}
- {{test_file_2}}
```

---

# 9. Functional Test Cases

```text
TC-FUNC-001:
Scenario: {{scenario_name}}
Given {{condition}}
When {{action}}
Then {{expected_result}}
Priority: {{priority}}
Automation: {{automation_status}}
```

---

# 10. API Test Cases

```text
TC-API-001:
Endpoint: {{api_endpoint}}
Method: {{api_method}}
Case: {{api_case}}
Expected Status: {{expected_status}}
Expected Body: {{expected_body}}
Expected Error Code: {{expected_error_code}}
```

---

# 11. Authorization and Security Test Cases

```text
TC-SEC-001:
Scenario: {{security_scenario}}
Actor: {{actor}}
Permission: {{permission}}
Resource Scope: {{resource_scope}}
Expected Result: {{expected_result}}
```

Required checks:

```text
authenticated access
unauthenticated denial
wrong role denial
wrong tenant denial
wrong owner denial
sensitive field protection
audit event if required
```

---

# 12. Negative and Edge Cases

```text
Invalid input: {{invalid_input_case}}
Missing required field: {{missing_field_case}}
Duplicate request: {{duplicate_case}}
Expired state: {{expired_state_case}}
Rate limit: {{rate_limit_case}}
External dependency failure: {{dependency_failure_case}}
```

---

# 13. Regression Test Areas

```text
Area 1: {{regression_area_1}}
Area 2: {{regression_area_2}}
Area 3: {{regression_area_3}}
```

---

# 14. Performance and Reliability Checks

```text
Expected latency: {{expected_latency}}
Load condition: {{load_condition}}
Timeout behavior: {{timeout_behavior}}
Retry behavior: {{retry_behavior}}
Background job behavior: {{background_job_behavior}}
Observability checks: {{observability_checks}}
```

---

# 15. Acceptance Criteria Mapping

Map PRD or API acceptance criteria to test cases.

```text
Acceptance Criteria | Test Case | Status
{{acceptance_criteria_1}} | {{test_case_id_1}} | {{test_status_1}}
{{acceptance_criteria_2}} | {{test_case_id_2}} | {{test_status_2}}
```

---

# 16. Automation Plan

```text
Automated tests to add:
- {{automated_test_1}}
- {{automated_test_2}}

Manual tests to keep:
- {{manual_test_1}}
- {{manual_test_2}}

Automation gaps:
- {{automation_gap_1}}
- {{automation_gap_2}}
```

---

# 17. Entry Criteria

Testing can start when:

```text
[ ] PRD or requirements are approved
[ ] API contract is available if needed
[ ] Test environment is ready
[ ] Test data is available
[ ] Feature branch or build is deployed
[ ] Required feature flags are configured
```

---

# 18. Exit Criteria

Testing is complete when:

```text
[ ] Critical test cases pass
[ ] High-priority defects are resolved or accepted
[ ] Regression checks pass
[ ] Security tests pass if required
[ ] Observability checks are verified
[ ] Release owner accepts remaining risk
```

---

# 19. Risks

```text
Risk 1: {{test_risk_1}}
Risk 2: {{test_risk_2}}
Risk 3: {{test_risk_3}}
```

---

# 20. Approval

```text
Engineering approval: {{engineering_approval}}
QA approval: {{qa_approval}}
Product approval: {{product_approval}}
Security approval: {{security_approval}}
Operations approval: {{operations_approval}}
```

---

# 21. Final Principle

> A test plan should prove both expected behavior and safe failure behavior.
