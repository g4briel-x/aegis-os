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

