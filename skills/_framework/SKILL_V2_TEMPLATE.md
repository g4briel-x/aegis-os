# Aegis OS — Skill v2 Template

Version: 0.2  
Status: Skill Template

---

# 1. Folder Template

```text
skills/<domain>/<skill-name>/
  README.md
  SKILL.md
  metadata.yaml
  expertise.md
  workflows.md
  checklists.md
  prompts.md
  examples/
    examples.md
```

---

# 2. README.md Template

```markdown
# <Skill Name>

Version: 0.2.0  
Status: Draft  
Domain: <domain>

## Purpose

Describe what this Skill does.

## Scope

Define what the Skill covers and what it does not cover.

## Files

List the Skill files.

## Usage

Explain how the Skill should be used.
```

---

# 3. SKILL.md Template

```markdown
# <Skill Name> — Skill Definition

## Role

Define the expert role.

## Mission

Define the mission of the Skill.

## Operating Principles

List the principles that guide behavior.

## Inputs

List expected inputs.

## Outputs

List expected outputs.

## Constraints

List constraints.

## Quality Standard

Define what good output looks like.
```

---

# 4. metadata.yaml Template

```yaml
skill:
  id:
  name:
  version: 0.2.0
  status: draft
  domain:
  category:
  maturity: draft
  owner:
  description:
  inputs: []
  outputs: []
  dependencies: []
  tags: []
```

---

# 5. Final Principle

> A reusable template accelerates Skill creation while preserving quality.