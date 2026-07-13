## FILE: `templates/operations/runbook-template/checklists.md`

# Runbook Template — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Completeness Checklist

```text
[ ] Runbook name is defined
[ ] Service or system is defined
[ ] Owner is assigned
[ ] Trigger conditions are defined
[ ] Required access is documented
[ ] Prerequisites are documented
[ ] Step-by-step procedure exists
[ ] Validation checks exist
[ ] Rollback or recovery is defined
[ ] Escalation contacts are listed
```

---

# 2. Safety Checklist

```text
[ ] Customer impact is described
[ ] Security impact is reviewed
[ ] Backup or recovery path is known if needed
[ ] Destructive actions are clearly marked
[ ] Stop conditions are defined
[ ] Required approvals are defined
[ ] Audit evidence is required where needed
```

---

# 3. Execution Checklist

```text
[ ] Operator can follow steps without guessing
[ ] Each step has expected result
[ ] Failure action exists for critical steps
[ ] Commands or queries are clear
[ ] Validation is measurable
[ ] Escalation path is practical
```

---

# 4. Review Checklist

```text
[ ] Engineering reviewed
[ ] Operations reviewed
[ ] Security reviewed if privileged
[ ] Support reviewed if customer-facing
[ ] Last review date is current
[ ] Owner confirmed accuracy
```

---

# 5. Final Principle

> Runbook checklists should prove that the document is usable during stress.
