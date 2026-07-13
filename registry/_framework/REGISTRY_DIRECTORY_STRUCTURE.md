## FILE: `registry/_framework/REGISTRY_DIRECTORY_STRUCTURE.md`

# Registry Directory Structure

Version: 0.1.0  
Status: Draft

---

# 1. Standard Structure

Recommended structure:

```text
registry/
  _framework/
    README.md
    REGISTRY_SPECIFICATION.md
    REGISTRY_DIRECTORY_STRUCTURE.md
    REGISTRY_METADATA_SCHEMA.md
    REGISTRY_AUTHORING_GUIDE.md
    REGISTRY_VALIDATION_MODEL.md
    REGISTRY_VERSIONING.md
    REGISTRY_TEMPLATE.md

  skills/
    skills.registry.yaml

  playbooks/
    playbooks.registry.yaml

  patterns/
    patterns.registry.yaml

  templates/
    templates.registry.yaml

  docs/
    docs.registry.yaml

  domains/
    domains.registry.yaml

  tags/
    tags.registry.yaml

  releases/
    releases.registry.yaml
```

---

# 2. Naming Rules

Registry files should follow this naming format:

```text
<asset-type>.registry.yaml
```

Examples:

```text
skills.registry.yaml
playbooks.registry.yaml
patterns.registry.yaml
templates.registry.yaml
docs.registry.yaml
```

---

# 3. Folder Rule

Each registry category should have its own folder.

Good:

```text
registry/skills/skills.registry.yaml
```

Avoid:

```text
registry/all-assets.yaml
```

---

# 4. Index Rule

Human-readable indexes remain in the asset folders.

Machine-readable registries live in the `registry/` folder.

Example:

```text
skills/INDEX.md = human readable
registry/skills/skills.registry.yaml = system readable
```

---

# 5. Final Principle

> Directory structure should make the difference between documentation, assets and registries obvious.
