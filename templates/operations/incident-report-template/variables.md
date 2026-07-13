## FILE: `templates/operations/incident-report-template/variables.md`

# Incident Report Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{incident_name}}
{{incident_id}}
{{incident_status}}
{{severity}}
{{created_at}}
{{last_updated}}
{{owner}}
{{current_status}}
{{customer_impact}}
{{affected_workflows}}
{{detected_by}}
{{timeline_event_1}}
{{action_1}}
{{next_step_1}}
```

---

# 2. Optional Variables

```text
{{incident_commander}}
{{technical_lead}}
{{communication_owner}}
{{security_privacy_impact}}
{{data_integrity_impact}}
{{workaround_available}}
{{incident_channel}}
{{status_page_link}}
{{postmortem_owner}}
```

---

# 3. Variable Descriptions

## `{{incident_name}}`

Purpose:

```text
Clear name of the incident.
```

Example:

```text
Project Submission API Degradation
```

---

## `{{incident_status}}`

Purpose:

```text
Current incident lifecycle state.
```

Recommended values:

```text
investigating
identified
monitoring
resolved
closed
```

---

## `{{severity}}`

Purpose:

```text
Incident severity according to the severity model.
```

Example:

```text
SEV2
```

---

## `{{current_status}}`

Purpose:

```text
Current operational state and action being taken.
```

Example:

```text
The submission API is degraded for some users. The team has identified a database lock issue and is applying mitigation.
```

---

# 4. Final Principle

> Incident report variables should capture what is known, what is affected and what happens next.
