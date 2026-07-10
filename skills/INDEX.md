## FILE: `skills/INDEX.md`

# Aegis OS — Skills Index

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This index lists the expert Skills available in Aegis OS.

A Skill represents a reusable expert capability with structured knowledge, workflows, checklists, prompts and examples.

---

# 2. Skill Framework

```text
skills/_framework/README.md
skills/_framework/SKILL_V2_SPECIFICATION.md
skills/_framework/SKILL_DIRECTORY_STRUCTURE.md
skills/_framework/SKILL_METADATA_SCHEMA.md
skills/_framework/SKILL_AUTHORING_GUIDE.md
skills/_framework/SKILL_QUALITY_GATE.md
skills/_framework/SKILL_REVIEW_CHECKLIST.md
skills/_framework/SKILL_PROMPTING_GUIDE.md
skills/_framework/SKILL_EXAMPLES_GUIDE.md
skills/_framework/SKILL_VERSIONING.md
skills/_framework/SKILL_CERTIFICATION.md
skills/_framework/SKILL_V2_TEMPLATE.md
```

---

# 3. Engineering Skills

```text
skills/engineering/senior-developer
skills/engineering/software-architect
skills/engineering/database-engineer
skills/engineering/senior-debugger
```

Purpose:

```text
Covers software implementation, architecture, database design and advanced debugging.
```

---

# 4. Product Skills

```text
skills/product/product-manager-saas
skills/product/business-analyst
```

Purpose:

```text
Covers SaaS product strategy, requirements, discovery, analysis and product decision support.
```

---

# 5. Design Skills

```text
skills/design/ux-ui-designer-saas
```

Purpose:

```text
Covers SaaS UX flows, UI design, user journeys, screens and product usability.
```

---

# 6. Infrastructure Skills

```text
skills/infrastructure/devops-engineer
skills/infrastructure/cloud-architect
```

Purpose:

```text
Covers CI/CD, deployment, cloud architecture, environments, reliability and infrastructure operations.
```

---

# 7. Security Skills

```text
skills/security/security-engineer
```

Purpose:

```text
Covers security review, access control, threat analysis, hardening, incident response and secure engineering.
```

---

# 8. Management Skills

```text
skills/management/technical-project-manager
```

Purpose:

```text
Covers delivery planning, coordination, milestones, risk tracking and execution management.
```

---

# 9. Standard Skill File Structure

Each premium Skill should follow this structure:

```text
README.md
SKILL.md
metadata.yaml
expertise.md
workflows.md
checklists.md
prompts.md
examples/examples.md
```

---

# 10. Skill Completion Status

```yaml
skills:
  framework: complete
  engineering:
    senior_developer: complete
    software_architect: complete
    database_engineer: complete
    senior_debugger: complete
  product:
    product_manager_saas: complete
    business_analyst: complete
  design:
    ux_ui_designer_saas: complete
  infrastructure:
    devops_engineer: complete
    cloud_architect: complete
  security:
    security_engineer: complete
  management:
    technical_project_manager: complete
```

---

# 11. Final Principle

> Skills encode expert judgment so it can be reused consistently across projects.
