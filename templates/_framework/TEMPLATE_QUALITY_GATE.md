## FILE: `templates/_framework/TEMPLATE_QUALITY_GATE.md`

# Template Quality Gate

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This document defines the minimum quality criteria for accepting a Template into Aegis OS.

---

# 2. Required Checks

A Template passes the quality gate only if:

```text
[ ] Purpose is clear
[ ] Output type is defined
[ ] Inputs are listed
[ ] Variables are documented
[ ] Required sections are defined
[ ] Optional sections are marked
[ ] Usage instructions are included
[ ] Quality checklist exists
[ ] Example output exists
[ ] Metadata is complete
[ ] Related assets are linked
```

---

# 3. Review Criteria

Reviewers should assess:

- clarity;
- completeness;
- reuse value;
- output quality;
- domain alignment;
- automation readiness;
- maintainability.

---

# 4. Rejection Reasons

Reject a Template when:

- it is too generic;
- it has no clear output;
- variables are missing;
- sections are unclear;
- example is absent;
- it duplicates an existing Template;
- it is really a Playbook or Pattern.

---

# 5. Final Principle

> A Template should be accepted only when it reliably improves repeated output creation.
