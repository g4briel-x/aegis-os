## FILE: `playbooks/_framework/PLAYBOOK_DIRECTORY_STRUCTURE.md`

# Aegis OS — Playbook Directory Structure

Version: 0.1  
Status: Playbook Standard

---

# 1. Introduction

This document defines the standard folder structure for Aegis OS Playbooks.

---

# 2. Recommended Structure

```text
playbooks/
  engineering/
    debug-production-issue/
      README.md
      PLAYBOOK.md
      metadata.yaml
      steps.md
      decision-points.md
      checklists.md
      outputs.md
      examples/
        examples.md
```

---

# 3. Domain Folders

Recommended domains:

```text
engineering/
product/
design/
infrastructure/
security/
operations/
management/
business/
```

---

# 4. Naming Rules

Playbook folder names should:

- use lowercase;
- use hyphens;
- describe an action or recurring scenario;
- avoid vague names.

Good examples:

```text
debug-production-issue
define-saas-mvp
review-api-security
prepare-release
run-discovery-interviews
```

---

# 5. Final Principle

> Playbook names should describe what the user will execute.