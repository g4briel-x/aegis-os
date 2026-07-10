## FILE: `playbooks/_framework/PLAYBOOK_METADATA_SCHEMA.md`

# Aegis OS — Playbook Metadata Schema

Version: 0.1  
Status: Playbook Standard

---

# 1. Introduction

This document defines the metadata schema for Playbooks.

Metadata allows Playbooks to be indexed, routed, validated and reused.

---

# 2. Required Metadata

```yaml
playbook:
  id:
  name:
  version:
  status:
  domain:
  category:
  maturity:
  owner:
  description:
  trigger:
  inputs:
  outputs:
  related_skills:
  tags:
```

---

# 3. Example

```yaml
playbook:
  id: engineering.debug-production-issue
  name: Debug Production Issue
  version: 0.1.0
  status: draft
  domain: engineering
  category: debugging
  maturity: usable
  owner: aegis-os
  description: Structured procedure for diagnosing and resolving production issues.
  trigger: A production service is failing, degraded or producing unexpected behavior.
  inputs:
    - incident_summary
    - logs
    - metrics
    - recent_changes
  outputs:
    - diagnosis
    - mitigation_plan
    - verification_steps
    - prevention_actions
  related_skills:
    - engineering.senior-debugger
    - infrastructure.devops-engineer
  tags:
    - debugging
    - production
    - incident
    - operations
```

---

# 4. Final Principle

> Playbook metadata makes recurring procedures discoverable and executable.
