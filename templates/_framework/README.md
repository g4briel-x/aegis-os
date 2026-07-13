## FILE: `templates/_framework/README.md`

# Aegis OS — Templates Framework

Version: 0.1.0  
Status: Foundation Draft  
Domain: Templates

---

# 1. Purpose

The Templates Framework defines how reusable output templates are created, organized, reviewed and maintained inside Aegis OS.

A Template provides a standardized structure for producing repeatable deliverables such as PRDs, runbooks, RFCs, test plans, API contracts, incident reports, postmortems, launch plans and architecture documents.

---

# 2. What a Template Provides

A Template should provide:

```text
document purpose
required inputs
standard sections
placeholder variables
output rules
quality checklist
example usage
related skills
related playbooks
related patterns
```

---

# 3. Template Categories

Recommended categories:

```text
templates/product
templates/engineering
templates/security
templates/operations
templates/business
templates/design
templates/management
templates/architecture
```

---

# 4. Standard Template Structure

Each Template should use this structure:

```text
README.md
TEMPLATE.md
metadata.yaml
variables.md
usage.md
checklists.md
examples/examples.md
```

---

# 5. Final Principle

> A Template should make high-quality output easier to produce without removing expert judgment.
