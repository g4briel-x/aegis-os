## FILE: `patterns/security/audit-logging-traceability/solution.md`

# Audit Logging Traceability — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Solution Overview

Create a structured audit logging system.

Core elements:

```text
audit event schema
action catalog
event producer rules
metadata safety rules
storage and retention
access policy
search and export
tests
```

---

# 2. Audit Event Schema

Recommended schema:

```yaml
audit_event:
  id: aud_123
  timestamp: 2026-07-12T10:00:00Z
  actor_id: usr_123
  actor_type: user
  tenant_id: wsp_456
  action: document.downloaded
  resource_type: document
  resource_id: doc_789
  result: success
  request_id: req_abc
  source: api
  metadata:
    document_type: pitch_deck
```

---

# 3. Action Catalog

Create a stable action catalog.

Examples:

```text
user.login_succeeded
user.login_failed
workspace.member_invited
workspace.member_removed
workspace.member_role_changed
project.submitted
project.approved
document.uploaded
document.downloaded
billing.plan_changed
api_key.created
api_key.deleted
support.access_started
support.access_ended
security.setting_changed
```

---

# 4. Event Producer Rules

Audit events should be emitted at the application service layer where business action succeeds or fails.

Rules:

```text
emit after successful sensitive action
emit failed attempts when security-relevant
include tenant and resource scope
include request id
avoid duplicate noisy events
do not emit secrets
```

---

# 5. Metadata Safety Rules

Metadata should be minimal and safe.

Safe examples:

```text
field names changed
old role and new role
file type
approval status
reason code
client application
```

Unsafe examples:

```text
tokens
passwords
private file contents
raw payment data
full personal messages
secret configuration values
```

---

# 6. Storage Model

Audit logs should be:

```text
append-only where possible
restricted for write access
searchable by tenant, actor, action and resource
retained according to policy
protected from normal deletion
exportable when appropriate
```

---

# 7. Access Policy

Define who can read audit logs.

Example:

```text
workspace_owner can view workspace audit events
security_admin can view security events
platform_admin can view platform events
support_admin can view limited events for assigned cases
```

---

# 8. Tests

Test that audit events are created for sensitive actions.

Examples:

```text
role change creates audit event
document download creates audit event
failed permission attempt creates audit event if required
support access creates start and end events
audit metadata excludes secrets
audit event includes tenant_id
```

---

# 9. Final Principle

> Audit logging should be implemented close enough to business action to be meaningful and close enough to security policy to be trusted.
