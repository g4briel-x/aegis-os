## FILE: `playbooks/_framework/PLAYBOOK_DECISION_POINTS.md`

# Aegis OS — Playbook Decision Points

Version: 0.1  
Status: Playbook Standard

---

# 1. Introduction

This document defines how decision points should be represented in Playbooks.

---

# 2. Decision Point Purpose

Decision points guide execution when the next step depends on context, evidence, risk or user choice.

---

# 3. Decision Point Structure

A decision point should define:

```yaml
decision_point:
  question:
  options:
  criteria:
  recommended_action:
  fallback:
```

---

# 4. Final Principle

> Decision points keep Playbooks flexible without becoming vague.

---

## FILE: `playbooks/_framework/PLAYBOOK_OUTPUT_MODEL.md`

# Aegis OS — Playbook Output Model

Version: 0.1  
Status: Playbook Standard

---

# 1. Introduction

This document defines how Playbook outputs should be described.

---

# 2. Output Requirements

A Playbook output should be:

- named;
- structured;
- useful;
- reviewable;
- connected to completion criteria.

---

# 3. Output Examples

Possible outputs:

- diagnosis;
- implementation plan;
- risk register;
- status report;
- PRD;
- roadmap;
- security review;
- runbook;
- decision record.

---

# 4. Output Template

```yaml
output:
  name:
  purpose:
  format:
  required_sections:
  quality_criteria:
```

---

# 5. Final Principle

> A Playbook is only useful if its output is clear enough to act on.
