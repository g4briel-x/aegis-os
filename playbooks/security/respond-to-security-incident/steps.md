## FILE: `playbooks/security/respond-to-security-incident/steps.md`

# Respond to Security Incident — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Confirm and Classify the Incident

Determine whether the signal indicates a security incident.

Classify:

- suspected incident;
- confirmed incident;
- false positive;
- abuse event;
- credential exposure;
- data exposure;
- unauthorized access;
- security-sensitive anomaly.

Output:

```text
Incident classification
```

---

# 2. Step 2 — Preserve Evidence

Capture evidence before making destructive changes.

Preserve:

- logs;
- audit events;
- alert details;
- timestamps;
- affected user or service accounts;
- IP addresses;
- access records;
- configuration snapshots;
- relevant deployment history.

Output:

```text
Evidence record
```

---

# 3. Step 3 — Assess Impact and Exposure

Determine what may be affected.

Assess:

- affected systems;
- affected users;
- affected data;
- compromised credentials;
- exposed files;
- privileged access;
- business impact;
- regulatory or contractual sensitivity.

Output:

```text
Impact and exposure assessment
```

---

# 4. Step 4 — Contain Active Risk

Stop ongoing exposure or abuse.

Containment actions may include:

- disable compromised accounts;
- revoke tokens;
- rotate secrets;
- block suspicious IPs;
- disable vulnerable feature;
- restrict access;
- pause risky workflows;
- isolate affected system.

Output:

```text
Containment plan and action log
```

---

# 5. Step 5 — Revoke and Rotate Access

Handle compromised or potentially exposed credentials.

Review:

- API keys;
- OAuth tokens;
- service account keys;
- database credentials;
- deployment tokens;
- user sessions;
- admin credentials.

Output:

```text
Credential revocation and rotation record
```

---

# 6. Step 6 — Investigate Root Cause

Identify how the incident happened.

Investigate:

- access path;
- vulnerability or misconfiguration;
- leaked secret source;
- authorization failure;
- phishing or account takeover;
- dependency or supply chain issue;
- deployment or configuration change.

Output:

```text
Root cause investigation summary
```

---

# 7. Step 7 — Recover Safely

Restore secure operation.

Recovery may include:

- deploy patch;
- restore safe configuration;
- re-enable service;
- validate permissions;
- verify secret rotation;
- confirm data integrity;
- run security checks.

Output:

```text
Recovery plan and verification notes
```

---

# 8. Step 8 — Monitor for Recurrence

Watch for continued attacker activity or regression.

Monitor:

- login attempts;
- authorization failures;
- API abuse;
- affected endpoints;
- suspicious IPs;
- admin actions;
- secret usage;
- unusual data access.

Output:

```text
Post-containment monitoring notes
```

---

# 9. Step 9 — Communicate Appropriately

Prepare communication based on scope and authority.

Communication may include:

- internal incident update;
- executive summary;
- customer support briefing;
- legal or compliance escalation;
- technical team instructions;
- post-incident summary.

Output:

```text
Communication notes
```

---

# 10. Step 10 — Define Prevention Actions

Reduce recurrence risk.

Examples:

- strengthen access controls;
- add audit logging;
- rotate secrets regularly;
- add secret scanning;
- improve alerting;
- patch vulnerability;
- add security tests;
- update runbooks;
- train team on handling secrets.

Output:

```text
Prevention action list
```

---

# 11. Final Principle

> Security incident steps should reduce exposure first, then explain cause, then prevent recurrence.
