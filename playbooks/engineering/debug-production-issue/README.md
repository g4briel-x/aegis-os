## FILE: `playbooks/engineering/debug-production-issue/README.md`

# Debug Production Issue Playbook

Version: 0.1.0  
Status: Premium Draft  
Domain: Engineering  
Category: Debugging / Incident Response

---

# 1. Purpose

The Debug Production Issue Playbook provides a structured procedure for diagnosing, mitigating and resolving production issues.

It is designed for situations where a live service is degraded, failing, producing unexpected behavior or affecting users.

---

# 2. Trigger

Use this Playbook when:

- a production service is failing;
- users report broken behavior;
- monitoring alerts show degradation;
- error rate increases;
- latency becomes abnormal;
- a recent deployment caused regressions;
- business-critical workflows stop working.

---

# 3. Scope

This Playbook covers:

- impact assessment;
- evidence collection;
- triage;
- root cause investigation;
- mitigation;
- fix validation;
- prevention actions.

This Playbook does not replace a full security incident process when malicious activity is suspected.

---

# 4. Related Skills

```text
engineering.senior-debugger
infrastructure.devops-engineer
security.security-engineer
management.technical-project-manager
```

---

# 5. Final Principle

> Production debugging must prioritize user impact, evidence, safe mitigation and verified recovery.