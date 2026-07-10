## FILE: `playbooks/_framework/PLAYBOOK_TEMPLATE.md`

# Aegis OS — Playbook Template

Version: 0.1  
Status: Playbook Template

---

# 1. Folder Template

```text
playbooks/<domain>/<playbook-name>/
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

# 2. README.md Template

```markdown
# <Playbook Name>

Version: 0.1.0  
Status: Draft  
Domain: <domain>

## Purpose

Describe what this Playbook helps execute.

## Trigger

Describe when this Playbook should be used.

## Scope

Define what is covered and what is not covered.

## Related Skills

List Skills that may execute or support the Playbook.
```

---

# 3. PLAYBOOK.md Template

```markdown
# <Playbook Name> — Playbook Definition

## Purpose

## Trigger

## Scope

## Inputs

## Outputs

## Execution Summary

## Completion Criteria

## Escalation or Fallback
```

---

# 4. metadata.yaml Template

```yaml
playbook:
  id:
  name:
  version: 0.1.0
  status: draft
  domain:
  category:
  maturity: draft
  owner:
  description:
  trigger:
  inputs: []
  outputs: []
  related_skills: []
  tags: []
```

---

# 5. Final Principle

> A reusable template makes Playbook creation faster while preserving execution quality.
