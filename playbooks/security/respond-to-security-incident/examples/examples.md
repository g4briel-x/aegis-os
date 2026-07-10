## FILE: `playbooks/security/respond-to-security-incident/examples/examples.md`

# Respond to Security Incident — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — API Key Leaked in Logs

## Trigger

An API key appears in application logs.

## Expected Execution

The Playbook should guide the team to:

- classify the incident as credential exposure;
- preserve log evidence;
- revoke and rotate the key;
- inspect usage during exposure window;
- verify service recovery;
- add log redaction and secret scanning.

## Expected Output

```text
Incident classification
Evidence record
Containment plan
Credential rotation record
Investigation summary
Prevention actions
```

---

# 2. Example — Suspicious Admin Login

## Trigger

A privileged admin account logs in from an unusual location.

## Expected Execution

The Playbook should guide the team to:

- preserve login and audit logs;
- disable or challenge the account if needed;
- review admin actions;
- rotate credentials if compromise is suspected;
- monitor for continued activity.

---

# 3. Example — Public File Exposure

## Trigger

A storage bucket or file path may expose private customer files.

## Expected Execution

The Playbook should guide the team to:

- restrict public access;
- identify affected files;
- preserve evidence;
- review access logs;
- validate permission configuration;
- define customer or legal escalation if needed.

---

# 4. Example — Authorization Bypass

## Trigger

A user can access another tenant's project record.

## Expected Execution

The Playbook should guide the team to:

- contain access path;
- preserve logs;
- identify affected tenants;
- patch object-level authorization;
- test tenant isolation;
- define prevention tests.

---

# 5. Final Principle

> Examples show that incident response must prioritize containment, evidence and verified recovery.
