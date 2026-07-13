## FILE: `templates/operations/postmortem-template/variables.md`

# Postmortem Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{incident_name}}
{{incident_id}}
{{severity}}
{{incident_date}}
{{postmortem_date}}
{{owner}}
{{executive_summary}}
{{customer_impact}}
{{timeline_event_1}}
{{detected_by}}
{{root_cause}}
{{resolution_summary}}
{{corrective_action_1}}
{{action_owner_1}}
{{due_date_1}}
```

---

# 2. Optional Variables

```text
{{security_privacy_impact}}
{{data_integrity_impact}}
{{severity_changes}}
{{monitoring_gap}}
{{communication_owner}}
{{where_we_got_lucky_1}}
{{customer_communication_link}}
{{support_tickets_link}}
```

---

# 3. Variable Descriptions

## `{{incident_name}}`

Purpose:

```text
Clear human-readable name of the incident.
```

Example:

```text
Project Submission Outage
```

---

## `{{severity}}`

Purpose:

```text
Final incident severity according to the Incident Severity Model.
```

Example:

```text
SEV2
```

---

## `{{customer_impact}}`

Purpose:

```text
Description of how customers or users were affected.
```

Example:

```text
Creators could not submit completed project packages for readiness review for 42 minutes.
```

---

## `{{root_cause}}`

Purpose:

```text
Underlying cause that explains why the incident happened.
```

Example:

```text
A database migration added a required field before existing project records were backfilled.
```

---

## `{{corrective_action_1}}`

Purpose:

```text
Concrete action that reduces recurrence or improves detection or response.
```

Example:

```text
Add a pre-deployment migration validation checklist for required column changes.
```

---

# 4. Final Principle

> Postmortem variables should capture impact, causality and follow-up ownership.