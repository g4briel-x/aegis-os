## FILE: `templates/operations/incident-report-template/TEMPLATE.md`

# Incident Report Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
Incident Name: {{incident_name}}
Incident ID: {{incident_id}}
Status: {{incident_status}}
Severity: {{severity}}
Created At: {{created_at}}
Last Updated: {{last_updated}}
Owner: {{owner}}
Incident Commander: {{incident_commander}}
Technical Lead: {{technical_lead}}
Communication Owner: {{communication_owner}}
```

---

# 2. Current Status

```text
{{current_status}}
```

Recommended format:

```text
As of {{last_updated}}, {{system_or_service}} is {{current_state}}. The team is currently {{current_action}}. Next update expected at {{next_update_time}}.
```

---

# 3. Executive Summary

```text
{{executive_summary}}
```

Include:

```text
what happened
who is affected
current severity
current mitigation state
known customer impact
next planned action
```

---

# 4. Impact Summary

```text
Customer impact:
{{customer_impact}}

Affected users or tenants:
{{affected_users_or_tenants}}

Affected workflows:
{{affected_workflows}}

Business impact:
{{business_impact}}

Security or privacy impact:
{{security_privacy_impact}}

Data integrity impact:
{{data_integrity_impact}}
```

---

# 5. Severity Classification

```text
Severity: {{severity}}
Severity reason: {{severity_reason}}
Initial severity: {{initial_severity}}
Current severity: {{current_severity}}
Severity change history:
{{severity_change_history}}
```

---

# 6. Systems Affected

```text
Primary system: {{primary_system}}

Affected services:
- {{affected_service_1}}
- {{affected_service_2}}

Affected endpoints:
- {{affected_endpoint_1}}
- {{affected_endpoint_2}}

Affected background jobs:
- {{affected_job_1}}
- {{affected_job_2}}
```

---

# 7. Detection

```text
Detected by: {{detected_by}}
Detection method: {{detection_method}}
Detection time: {{detection_time}}
Alert name: {{alert_name}}
Customer report: {{customer_report}}
```

---

# 8. Timeline

```text
Time | Event | Source / Owner
{{timeline_time_1}} | {{timeline_event_1}} | {{timeline_source_1}}
{{timeline_time_2}} | {{timeline_event_2}} | {{timeline_source_2}}
{{timeline_time_3}} | {{timeline_event_3}} | {{timeline_source_3}}
```

Timeline should include:

```text
first known symptom
first alert
incident declaration
severity assignment
mitigation action
customer communication
resolution confirmation
incident closure
```

---

# 9. Actions Taken

```text
Action | Owner | Time | Result
{{action_1}} | {{action_owner_1}} | {{action_time_1}} | {{action_result_1}}
{{action_2}} | {{action_owner_2}} | {{action_time_2}} | {{action_result_2}}
```

---

# 10. Current Mitigation

```text
Mitigation status: {{mitigation_status}}
Mitigation applied: {{mitigation_applied}}
Remaining issue: {{remaining_issue}}
Expected recovery path: {{expected_recovery_path}}
```

---

# 11. Workaround

```text
Workaround available: {{workaround_available}}
Workaround description: {{workaround_description}}
Who can use it: {{workaround_users}}
Limitations: {{workaround_limitations}}
```

---

# 12. Communication

## 12.1 Internal Communication

```text
Incident channel: {{incident_channel}}
Internal update frequency: {{internal_update_frequency}}
Stakeholders notified:
- {{stakeholder_1}}
- {{stakeholder_2}}
```

## 12.2 Customer Communication

```text
Customer communication required: {{customer_communication_required}}
Customer message sent: {{customer_message_sent}}
Customer update frequency: {{customer_update_frequency}}
Support script: {{support_script}}
```

---

# 13. Evidence and Links

```text
Dashboard: {{dashboard_link}}
Logs: {{logs_link}}
Trace: {{trace_link}}
Alert: {{alert_link}}
Deployment: {{deployment_link}}
Pull request: {{pull_request_link}}
Support tickets: {{support_tickets_link}}
Status page: {{status_page_link}}
```

---

# 14. Open Questions

```text
Question 1: {{open_question_1}}
Question 2: {{open_question_2}}
Question 3: {{open_question_3}}
```

---

# 15. Next Steps

```text
Next step | Owner | Due / ETA | Status
{{next_step_1}} | {{next_step_owner_1}} | {{next_step_eta_1}} | {{next_step_status_1}}
{{next_step_2}} | {{next_step_owner_2}} | {{next_step_eta_2}} | {{next_step_status_2}}
```

---

# 16. Resolution

Complete this section when the incident is resolved.

```text
Resolved at: {{resolved_at}}
Resolution summary: {{resolution_summary}}
Validation performed: {{validation_performed}}
Customer impact ended at: {{customer_impact_ended_at}}
Postmortem required: {{postmortem_required}}
Postmortem owner: {{postmortem_owner}}
```

---

# 17. Approval / Closure

```text
Incident Commander closure: {{incident_commander_closure}}
Technical Lead closure: {{technical_lead_closure}}
Support closure: {{support_closure}}
Security closure: {{security_closure}}
Operations closure: {{operations_closure}}
```

---

# 18. Final Principle

> Incident reports should communicate facts, decisions and next actions clearly during uncertainty.
