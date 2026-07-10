## FILE: `playbooks/_framework/PLAYBOOK_QUALITY_GATE.md`

# Aegis OS — Playbook Quality Gate

Version: 0.1  
Status: Playbook Standard

---

# 1. Introduction

This document defines the quality gate for accepting Playbooks into Aegis OS.

---

# 2. Quality Dimensions

Each Playbook should be checked for:

- trigger clarity;
- input completeness;
- step sequence;
- decision-point usefulness;
- validation strength;
- output clarity;
- execution realism;
- maintainability.

---

# 3. Review Passes

Recommended review passes:

```text
Pass 1 — Structure Review
Pass 2 — Execution Review
Pass 3 — Decision and Risk Review
Pass 4 — Output and Quality Review
```

---

# 4. Acceptance Criteria

A Playbook is acceptable when:

- required files exist;
- metadata is valid;
- trigger is clear;
- steps are executable;
- decision points are useful;
- outputs are defined;
- completion criteria are explicit.

---

# 5. Final Principle

> A Playbook should not enter the ecosystem until it can reliably guide a real workflow.
