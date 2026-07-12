## FILE: `patterns/security/audit-logging-traceability/PATTERN.md`

# Audit Logging Traceability Pattern

Version: 0.1.0  
Status: Draft

---

# 1. Problem

A SaaS platform needs a trustworthy record of sensitive actions.

Without audit logging, teams cannot reliably answer:

- who changed a permission;
- who downloaded a file;
- who accessed customer data;
- who changed billing settings;
- who disabled a security control;
- what happened before an incident;
- whether a customer boundary was respected.

Operational logs alone are not enough. Audit logs must be business-aware and security-aware.

---

# 2. Context

This Pattern applies to SaaS products with:

```text
customer accounts
tenant data
admin users
support access
RBAC permissions
file storage
billing settings
security settings
compliance needs
```

---

# 3. Forces

Key forces:

```text
traceability versus privacy
security evidence versus log volume
debuggability versus sensitive data protection
customer transparency versus internal confidentiality
immutability versus operational flexibility
retention cost versus audit value
```

---

# 4. Recommended Model

Use a structured audit event model:

```text
AuditEvent
  id
  timestamp
  actor_id
  actor_type
  action
  resource_type
  resource_id
  tenant_id
  result
  request_id
  metadata
  source
```

Example action:

```text
workspace.member_role_changed
document.downloaded
billing.plan_updated
support.customer_access_started
api_key.created
permission.granted
```

---

# 5. Event Selection

Audit events should be created for:

```text
authentication and session events
role and permission changes
tenant membership changes
admin actions
support access
billing changes
security setting changes
file downloads and exports
API key creation and deletion
data deletion or restoration
integration connection changes
```

Do not audit every low-value read unless the data is sensitive or regulated.

---

# 6. Safe Audit Metadata

Audit metadata should avoid secrets and sensitive payloads.

Good metadata:

```text
changed_fields
previous_role
new_role
resource_status
reason_code
request_id
workflow_state
```

Bad metadata:

```text
passwords
tokens
full document contents
payment card data
private message bodies
secret values
```

---

# 7. Access to Audit Logs

Audit logs should have restricted access.

Recommended roles:

```text
security_admin
workspace_owner
platform_admin
compliance_reviewer
support_admin with limited scope
```

Access to audit logs should itself be auditable when sensitive.

---

# 8. Retention

Define retention policy.

Typical options:

```text
90 days for operational audit
1 year for customer-facing audit
3 to 7 years for compliance-sensitive events
custom enterprise retention when contracted
```

Retention must respect legal, privacy and storage constraints.

---

# 9. Final Principle

> Audit logging should produce evidence without creating a new security liability.
