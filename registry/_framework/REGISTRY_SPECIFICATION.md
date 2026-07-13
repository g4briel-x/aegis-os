## FILE: `registry/_framework/REGISTRY_SPECIFICATION.md`

# Registry Specification

Version: 0.1.0  
Status: Draft

---

# 1. Definition

A Registry is a structured catalog that lists Aegis OS assets and their metadata.

A registry must describe:

```text
asset identity
asset type
asset location
asset domain
asset status
asset version
asset maturity
asset relationships
asset tags
asset owner
```

---

# 2. Registry Goals

A Registry should:

```text
make assets discoverable
support automation
support validation
support dependency mapping
support runtime selection
support marketplace packaging
support governance and review
```

---

# 3. Registry Non-Goals

A Registry should not:

```text
replace the full asset document
duplicate all content from the asset
store implementation logic
hide incomplete or deprecated status
become a random notes file
```

---

# 4. Registry Entry Structure

Each registry entry should include:

```yaml
id: string
name: string
type: string
domain: string
category: string
status: string
maturity: string
version: string
path: string
owner: string
summary: string
tags: []
related_assets: []
```

---

# 5. Allowed Asset Types

```text
doc
skill
playbook
pattern
template
script
registry
```

---

# 6. Allowed Status Values

```text
draft
review
approved
deprecated
archived
```

---

# 7. Allowed Maturity Values

```text
experimental
usable
stable
certified
deprecated
```

---

# 8. Relationship Types

```text
uses
extends
supports
requires
replaces
related_to
generates
validates
```

---

# 9. Registry Quality Requirements

A Registry must be:

```text
consistent
machine-readable
human-readable
versioned
traceable
easy to validate
```

---

# 10. Final Principle

> A registry is the bridge between static knowledge and executable orchestration.
