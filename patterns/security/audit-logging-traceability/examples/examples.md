## FILE: `patterns/security/audit-logging-traceability/examples/examples.md`

# Audit Logging Traceability — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Financing SaaS

## Context

A SaaS platform manages film, series and documentary project files for financing readiness.

## Audit Events

```text
project.submitted
project.review_assigned
project.approved
document.uploaded
document.downloaded
workspace.member_role_changed
support.access_started
support.access_ended
```

## Event Example

```yaml
audit_event:
  actor_id: usr_creator_123
  actor_type: user
  tenant_id: wsp_prod_456
  action: project.submitted
  resource_type: project
  resource_id: prj_789
  result: success
  request_id: req_1001
  metadata:
    previous_status: draft
    new_status: submitted
```

---

# 2. Example — Role Change

```yaml
audit_event:
  actor_id: usr_owner_001
  actor_type: user
  tenant_id: wsp_001
  action: workspace.member_role_changed
  resource_type: workspace_membership
  resource_id: mem_002
  result: success
  request_id: req_1002
  metadata:
    previous_role: member
    new_role: admin
```

---

# 3. Example — File Download

```yaml
audit_event:
  actor_id: usr_reviewer_003
  actor_type: user
  tenant_id: wsp_001
  action: document.downloaded
  resource_type: document
  resource_id: doc_004
  result: success
  request_id: req_1003
  metadata:
    document_type: pitch_deck
```

---

# 4. Example — Support Access

```yaml
audit_event:
  actor_id: usr_support_010
  actor_type: support_admin
  tenant_id: wsp_001
  action: support.access_started
  resource_type: workspace
  resource_id: wsp_001
  result: success
  request_id: req_1004
  metadata:
    reason_code: customer_ticket
    ticket_id: ticket_456
```

---

# 5. Final Principle

> Examples show that audit logs should be structured enough for investigation and safe enough for long-term retention.
