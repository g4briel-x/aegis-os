## FILE: `playbooks/security/respond-to-security-incident/decision-points.md`

# Respond to Security Incident — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is This a Security Incident?

```yaml
decision_point:
  question: Does the signal indicate unauthorized access, credential exposure, abuse, data exposure or compromise?
  options:
    - yes
    - no
    - unknown
  criteria:
    - suspicious logs
    - exposed credential
    - abnormal access
    - data access anomaly
    - user report
    - security alert
  recommended_action:
    yes: start incident response.
    no: record false positive or operational issue.
    unknown: preserve evidence and investigate as security-sensitive.
  fallback: treat as suspected incident until ruled out.
```

---

# 2. Decision Point — Is Active Exposure Ongoing?

```yaml
decision_point:
  question: Is the attacker, exposed credential or vulnerable path still active?
  options:
    - yes
    - no
    - unknown
  criteria:
    - recent suspicious activity
    - valid exposed token
    - open vulnerable endpoint
    - active compromised account
    - continuing alerts
  recommended_action:
    yes: contain immediately.
    no: continue investigation and recovery.
    unknown: restrict or rotate access while preserving evidence.
  fallback: prioritize containment over convenience.
```

---

# 3. Decision Point — Are Credentials or Secrets Exposed?

```yaml
decision_point:
  question: Were credentials, API keys, tokens, session secrets or service keys exposed?
  options:
    - yes
    - no
    - unknown
  criteria:
    - secret in logs
    - secret in repository
    - token in shared message
    - suspicious token use
    - leaked config file
  recommended_action:
    yes: revoke and rotate immediately.
    no: document evidence.
    unknown: rotate high-risk credentials if impact is acceptable.
  fallback: assume exposure for any secret that left a trusted boundary.
```

---

# 4. Decision Point — Is Customer or Sensitive Data Involved?

```yaml
decision_point:
  question: Could customer, personal, payment, confidential or regulated data be affected?
  options:
    - yes
    - no
    - unknown
  criteria:
    - data access logs
    - affected tables
    - exposed files
    - unauthorized queries
    - privileged account use
  recommended_action:
    yes: escalate to legal, compliance or executive owner.
    no: continue technical response.
    unknown: investigate data access before closing incident.
  fallback: treat as sensitive until evidence proves otherwise.
```

---

# 5. Decision Point — Is Recovery Verified?

```yaml
decision_point:
  question: Has secure operation been restored and verified?
  options:
    - yes
    - no
    - partially
  criteria:
    - access revoked
    - patch deployed
    - monitoring clean
    - permissions verified
    - no active suspicious activity
  recommended_action:
    yes: proceed to post-incident review.
    no: continue containment and recovery.
    partially: keep incident open and monitor closely.
  fallback: do not close incident until verification evidence exists.
```

---

# 6. Final Principle

> Security incident decisions must be conservative when exposure, data risk or attacker activity is unclear.
