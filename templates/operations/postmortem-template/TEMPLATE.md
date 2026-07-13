## FILE: `templates/operations/postmortem-template/TEMPLATE.md`

# Postmortem Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
Incident Name: {{incident_name}}
Incident ID: {{incident_id}}
Severity: {{severity}}
Status: {{status}}
Incident Date: {{incident_date}}
Postmortem Date: {{postmortem_date}}
Owner: {{owner}}
Review Facilitator: {{review_facilitator}}
Contributors: {{contributors}}
```

---

# 2. Executive Summary

Summarize the incident in a few clear sentences.

```text
{{executive_summary}}
```

Recommended format:

```text
On {{incident_date}}, {{system_or_service}} experienced {{incident_summary}}. The incident affected {{affected_users_or_customers}} for {{duration}}. The issue was caused by {{root_cause_summary}} and resolved by {{resolution_summary}}.
```

---

# 3. Impact

Describe customer, business, technical and security impact.

```text
Customer impact:
{{customer_impact}}

Business impact:
{{business_impact}}

Technical impact:
{{technical_impact}}

Security or privacy impact:
{{security_privacy_impact}}

Data integrity impact:
{{data_integrity_impact}}
```

---

# 4. Severity Classification

```text
Severity: {{severity}}
Classification reason: {{severity_reason}}
Initial severity: {{initial_severity}}
Final severity: {{final_severity}}
Severity changes:
{{severity_changes}}
```

---

# 5. Timeline

Use chronological format.

```text
Time | Event | Owner / Source
{{timeline_time_1}} | {{timeline_event_1}} | {{timeline_owner_1}}
{{timeline_time_2}} | {{timeline_event_2}} | {{timeline_owner_2}}
{{timeline_time_3}} | {{timeline_event_3}} | {{timeline_owner_3}}
```

Timeline should include:

```text
first symptom
first alert
incident declaration
first customer report if any
mitigation start
root cause identified
fix deployed
recovery confirmed
customer communication
incident closed
```

---

# 6. Detection

Describe how the incident was detected.

```text
Detected by: {{detected_by}}
Detection time: {{detection_time}}
Detection method: {{detection_method}}
Alert fired: {{alert_fired}}
Monitoring gap: {{monitoring_gap}}
```

Questions:

```text
Was the incident detected by monitoring or by customers?
Did the alert fire early enough?
Was the alert actionable?
Was there a missing signal?
```

---

# 7. Response

Describe how the team responded.

```text
Incident commander: {{incident_commander}}
Technical lead: {{technical_lead}}
Communication owner: {{communication_owner}}
Support owner: {{support_owner}}
Security owner: {{security_owner}}
```

Response notes:

```text
{{response_notes}}
```

---

# 8. Root Cause Analysis

## 8.1 Direct Cause

```text
{{direct_cause}}
```

## 8.2 Contributing Factors

```text
Factor 1: {{contributing_factor_1}}
Factor 2: {{contributing_factor_2}}
Factor 3: {{contributing_factor_3}}
```

## 8.3 Root Cause

```text
{{root_cause}}
```

## 8.4 Why It Was Not Prevented

```text
{{prevention_gap}}
```

---

# 9. Resolution

Describe what fixed or mitigated the incident.

```text
Mitigation:
{{mitigation}}

Permanent fix:
{{permanent_fix}}

Rollback or recovery:
{{rollback_or_recovery}}

Validation:
{{validation_performed}}
```

---

# 10. What Went Well

```text
{{what_went_well_1}}
{{what_went_well_2}}
{{what_went_well_3}}
```

---

# 11. What Went Wrong

```text
{{what_went_wrong_1}}
{{what_went_wrong_2}}
{{what_went_wrong_3}}
```

---

# 12. Where We Got Lucky

```text
{{where_we_got_lucky_1}}
{{where_we_got_lucky_2}}
{{where_we_got_lucky_3}}
```

This section helps identify risks that could become worse next time.

---

# 13. Corrective Actions

```text
Action ID | Action | Owner | Due Date | Priority | Status
{{action_id_1}} | {{corrective_action_1}} | {{action_owner_1}} | {{due_date_1}} | {{priority_1}} | {{action_status_1}}
{{action_id_2}} | {{corrective_action_2}} | {{action_owner_2}} | {{due_date_2}} | {{priority_2}} | {{action_status_2}}
```

Action types:

```text
prevent recurrence
improve detection
improve response
improve communication
improve rollback
update runbook
add test coverage
add monitoring
fix documentation
```

---

# 14. Customer Communication

```text
Customer communication required: {{customer_communication_required}}
Communication sent: {{communication_sent}}
Communication summary: {{communication_summary}}
Support notes: {{support_notes}}
```

---

# 15. Follow-Up Review

```text
Follow-up date: {{follow_up_date}}
Review owner: {{review_owner}}
Completion criteria: {{completion_criteria}}
```

---

# 16. Links and Evidence

```text
Incident channel: {{incident_channel_link}}
Dashboard: {{dashboard_link}}
Logs: {{logs_link}}
Pull request: {{pull_request_link}}
Runbook: {{runbook_link}}
Support tickets: {{support_tickets_link}}
Customer communication: {{customer_communication_link}}
```

---

# 17. Approval

```text
Engineering approval: {{engineering_approval}}
Operations approval: {{operations_approval}}
Security approval: {{security_approval}}
Product approval: {{product_approval}}
Support approval: {{support_approval}}
```

---

# 18. Final Principle

> A postmortem is complete when corrective actions are clear, owned and tracked.
