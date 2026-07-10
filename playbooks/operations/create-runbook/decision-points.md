## FILE: `playbooks/operations/create-runbook/decision-points.md`

# Create Runbook — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is a Runbook Needed?

```yaml
decision_point:
  question: Does this process need a written operational runbook?
  options:
    - yes
    - no
    - automate_instead
  criteria:
    - recurring process
    - production impact
    - incident relevance
    - requires specific access
    - risk if done incorrectly
  recommended_action:
    yes: create runbook.
    no: document lightweight note if needed.
    automate_instead: automate and still document fallback.
  fallback: create a basic runbook for any high-risk manual process.
```

---

# 2. Decision Point — Is the Procedure Safe to Execute?

```yaml
decision_point:
  question: Can the documented procedure be executed safely by the intended operator?
  options:
    - yes
    - no
    - with_approval
  criteria:
    - destructive actions
    - production impact
    - access level
    - rollback availability
    - verification clarity
  recommended_action:
    yes: approve procedure.
    no: revise or require specialist execution.
    with_approval: add approval gate and escalation owner.
  fallback: require senior review for destructive production actions.
```

---

# 3. Decision Point — Is Rollback Required?

```yaml
decision_point:
  question: Does the runbook require rollback or recovery instructions?
  options:
    - yes
    - no
    - unclear
  criteria:
    - production change
    - customer impact
    - data mutation
    - deployment action
    - security control change
  recommended_action:
    yes: add rollback section.
    no: document why rollback is not relevant.
    unclear: add recovery or escalation fallback.
  fallback: include at least a stop-and-escalate recovery path.
```

---

# 4. Decision Point — Is Escalation Clear?

```yaml
decision_point:
  question: Does the operator know who to contact when execution fails?
  options:
    - yes
    - no
    - partially
  criteria:
    - owner listed
    - escalation threshold defined
    - communication channel listed
    - severity mapping available
  recommended_action:
    yes: proceed.
    no: add escalation path.
    partially: clarify thresholds and contacts.
  fallback: do not publish critical runbook without escalation owner.
```

---

# 5. Decision Point — Is the Runbook Verifiable?

```yaml
decision_point:
  question: Can the operator prove that the runbook succeeded?
  options:
    - yes
    - no
    - partially
  criteria:
    - expected result defined
    - metrics or logs available
    - validation command available
    - success criteria clear
  recommended_action:
    yes: publish.
    no: add verification checks.
    partially: strengthen evidence requirements.
  fallback: no runbook is complete without verification criteria.
```

---

# 6. Final Principle

> Runbook decisions should protect production safety and operator confidence.