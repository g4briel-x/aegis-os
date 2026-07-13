## FILE: `templates/operations/release-plan-template/TEMPLATE.md`

# Release Plan Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
Release Name: {{release_name}}
Release Version: {{release_version}}
Release Owner: {{release_owner}}
Technical Owner: {{technical_owner}}
Product Owner: {{product_owner}}
Status: {{status}}
Target Release Date: {{target_release_date}}
Release Window: {{release_window}}
Last Updated: {{last_updated}}
```

---

# 2. Release Summary

Describe what is being released.

```text
{{release_summary}}
```

Recommended format:

```text
This release delivers {{main_change}} for {{target_users}} and includes {{release_scope_summary}}.
```

---

# 3. Release Scope

## 3.1 Included Changes

```text
{{included_change_1}}
{{included_change_2}}
{{included_change_3}}
```

## 3.2 Excluded Changes

```text
{{excluded_change_1}}
{{excluded_change_2}}
{{excluded_change_3}}
```

---

# 4. Business and Customer Impact

```text
Customer impact:
{{customer_impact}}

Business impact:
{{business_impact}}

Support impact:
{{support_impact}}

Operational impact:
{{operational_impact}}
```

---

# 5. Release Type

```text
Release type: {{release_type}}
```

Recommended values:

```text
standard_release
hotfix
security_release
database_migration_release
feature_flag_release
beta_release
major_release
rollback_release
```

---

# 6. Dependencies

```text
Code dependencies:
{{code_dependencies}}

Data dependencies:
{{data_dependencies}}

Infrastructure dependencies:
{{infrastructure_dependencies}}

Third-party dependencies:
{{third_party_dependencies}}

Documentation dependencies:
{{documentation_dependencies}}

Support dependencies:
{{support_dependencies}}
```

---

# 7. Risk Assessment

```text
Risk level: {{risk_level}}
Risk reason: {{risk_reason}}
```

Risk categories:

```text
customer workflow risk
database risk
security risk
performance risk
integration risk
rollback risk
support risk
```

Risk table:

```text
Risk | Impact | Likelihood | Mitigation | Owner
{{risk_1}} | {{impact_1}} | {{likelihood_1}} | {{mitigation_1}} | {{risk_owner_1}}
{{risk_2}} | {{impact_2}} | {{likelihood_2}} | {{mitigation_2}} | {{risk_owner_2}}
```

---

# 8. Feature Flags

```text
Feature flag required: {{feature_flag_required}}
Feature flag name: {{feature_flag_name}}
Default state: {{feature_flag_default_state}}
Target audience: {{feature_flag_target_audience}}
Rollout stages: {{feature_flag_rollout_stages}}
Kill switch owner: {{kill_switch_owner}}
```

---

# 9. Database and Migration Plan

```text
Database migration included: {{database_migration_included}}
Migration summary: {{migration_summary}}
Migration risk: {{migration_risk}}
Backward compatible: {{migration_backward_compatible}}
Backup required: {{backup_required}}
Rollback or recovery: {{migration_rollback_or_recovery}}
Validation queries: {{migration_validation_queries}}
```

---

# 10. Security and Compliance Review

```text
Security review required: {{security_review_required}}
Security reviewer: {{security_reviewer}}
Authorization impact: {{authorization_impact}}
Tenant isolation impact: {{tenant_isolation_impact}}
Sensitive data impact: {{sensitive_data_impact}}
Audit logging impact: {{audit_logging_impact}}
Compliance notes: {{compliance_notes}}
```

---

# 11. Test Readiness

```text
Test plan: {{test_plan_link}}
Test status: {{test_status}}
Critical tests passed: {{critical_tests_passed}}
Regression status: {{regression_status}}
Security test status: {{security_test_status}}
Performance test status: {{performance_test_status}}
Known defects: {{known_defects}}
Accepted risks: {{accepted_risks}}
```

---

# 12. Deployment Plan

```text
Deployment environment: {{deployment_environment}}
Deployment method: {{deployment_method}}
Deployment owner: {{deployment_owner}}
Deployment start time: {{deployment_start_time}}
Expected duration: {{expected_duration}}
```

Steps:

```text
1. {{deployment_step_1}}
2. {{deployment_step_2}}
3. {{deployment_step_3}}
4. {{deployment_step_4}}
5. {{deployment_step_5}}
```

---

# 13. Validation Plan

Validate after deployment:

```text
[ ] {{validation_check_1}}
[ ] {{validation_check_2}}
[ ] {{validation_check_3}}
[ ] {{validation_check_4}}
```

Validation signals:

```text
Health checks: {{health_checks}}
Core workflow checks: {{core_workflow_checks}}
Error rate: {{error_rate_threshold}}
Latency: {{latency_threshold}}
Background jobs: {{background_job_checks}}
Logs: {{log_checks}}
```

---

# 14. Rollback and Recovery Plan

```text
Rollback owner: {{rollback_owner}}
Rollback trigger: {{rollback_trigger}}
Rollback method: {{rollback_method}}
Rollback expected duration: {{rollback_expected_duration}}
Recovery notes: {{recovery_notes}}
```

Rollback steps:

```text
1. {{rollback_step_1}}
2. {{rollback_step_2}}
3. {{rollback_step_3}}
```

Stop conditions:

```text
{{stop_condition_1}}
{{stop_condition_2}}
```

---

# 15. Monitoring Plan

```text
Monitoring window: {{monitoring_window}}
Dashboard: {{dashboard_link}}
Alerts: {{alerts}}
Metrics:
- {{metric_1}}
- {{metric_2}}
- {{metric_3}}
Logs:
- {{log_1}}
- {{log_2}}
```

---

# 16. Communication Plan

```text
Internal communication channel: {{internal_communication_channel}}
Support notification required: {{support_notification_required}}
Customer communication required: {{customer_communication_required}}
Release notes required: {{release_notes_required}}
Status page update required: {{status_page_update_required}}
```

Communication messages:

```text
Pre-release message:
{{pre_release_message}}

Post-release message:
{{post_release_message}}

Rollback message:
{{rollback_message}}
```

---

# 17. Approval

```text
Product approval: {{product_approval}}
Engineering approval: {{engineering_approval}}
QA approval: {{qa_approval}}
Security approval: {{security_approval}}
Operations approval: {{operations_approval}}
Support approval: {{support_approval}}
```

---

# 18. Post-Release Review

```text
Review date: {{review_date}}
Release outcome: {{release_outcome}}
Issues observed: {{issues_observed}}
Follow-up actions: {{follow_up_actions}}
Lessons learned: {{lessons_learned}}
```

---

# 19. Final Principle

> A release plan should prove that the team knows what changes, how to validate it and how to recover if it fails.
