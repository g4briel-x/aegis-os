# Aegis OS — Registry Index Bundle

Ce fichier regroupe l’index global de la couche Registry :

- `registry/INDEX.md`

---

## FILE: `registry/INDEX.md`

# Aegis OS — Registry Index

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

The Registry Index is the human-readable entry point for the Aegis OS registry layer.

It explains which machine-readable registries exist, what each registry is responsible for, and how registries connect Aegis OS documentation, skills, playbooks, patterns, templates, domains, tags and releases.

---

# 2. Why the Registry Layer Exists

Aegis OS has two kinds of navigation:

```text
Human navigation:
README.md
MANIFEST.md
docs/INDEX.md
skills/INDEX.md
playbooks/INDEX.md
patterns/INDEX.md
templates/INDEX.md

Machine navigation:
registry/foundation/foundation.registry.yaml
registry/skills/skills.registry.yaml
registry/playbooks/playbooks.registry.yaml
registry/patterns/patterns.registry.yaml
registry/templates/templates.registry.yaml
registry/docs/docs.registry.yaml
registry/domains/domains.registry.yaml
registry/tags/tags.registry.yaml
registry/releases/releases.registry.yaml
```

Human indexes explain the repository to people.

Machine registries allow tools, CLI commands, automation scripts, marketplaces and runtime systems to discover, filter, validate and connect assets.

---

# 3. Registry Framework

```text
registry/_framework
```

Role:

```text
Defines the rules, schema, directory structure, authoring process, validation model, versioning policy and template for all Aegis OS registries.
```

Files:

```text
registry/_framework/README.md
registry/_framework/REGISTRY_SPECIFICATION.md
registry/_framework/REGISTRY_DIRECTORY_STRUCTURE.md
registry/_framework/REGISTRY_METADATA_SCHEMA.md
registry/_framework/REGISTRY_AUTHORING_GUIDE.md
registry/_framework/REGISTRY_VALIDATION_MODEL.md
registry/_framework/REGISTRY_VERSIONING.md
registry/_framework/REGISTRY_TEMPLATE.md
```

---

# 4. Foundation Assets Registry

```text
registry/foundation/foundation.registry.yaml
```

Role:

```text
Registers the core components, asset frameworks, registry definitions, global indexes and CLI documentation referenced by the rest of Aegis OS.
```

It prevents foundational relationships from pointing to identifiers that exist
as repository files but are absent from the machine-readable catalog.

---

# 5. Skills Registry

```text
registry/skills/skills.registry.yaml
```

Role:

```text
Machine-readable catalog of Aegis OS skills.
```

It describes:

```text
skill id
skill name
domain
category
status
maturity
version
path
owner
summary
tags
related assets
```

Used for:

```text
finding expert capabilities
selecting the right skill for a task
connecting skills to playbooks and templates
future CLI skill discovery
future runtime skill routing
```

---

# 6. Playbooks Registry

```text
registry/playbooks/playbooks.registry.yaml
```

Role:

```text
Machine-readable catalog of Aegis OS playbooks.
```

It describes:

```text
available procedures
execution domains
playbook categories
workflow purpose
related skills
related templates
related patterns
```

Used for:

```text
selecting a step-by-step process
orchestrating repeatable workflows
connecting tasks to execution procedures
future CLI playbook listing
future runtime procedure execution
```

---

# 7. Patterns Registry

```text
registry/patterns/patterns.registry.yaml
```

Role:

```text
Machine-readable catalog of reusable Aegis OS patterns.
```

It describes:

```text
decision models
architecture patterns
security patterns
engineering patterns
operations patterns
design patterns
business patterns
related implementation assets
```

Used for:

```text
choosing reusable design decisions
connecting patterns to playbooks
explaining trade-offs
supporting architecture and security review
```

---

# 8. Templates Registry

```text
registry/templates/templates.registry.yaml
```

Role:

```text
Machine-readable catalog of Aegis OS templates.
```

It describes:

```text
output formats
document structures
artifact types
variables
usage areas
related skills
related playbooks
related patterns
```

Used for:

```text
generating consistent documents
selecting the right output structure
supporting future CLI artifact creation
connecting workflows to deliverables
```

---

# 9. Docs Registry

```text
registry/docs/docs.registry.yaml
```

Role:

```text
Machine-readable catalog of Aegis OS documentation sections and major documentation assets.
```

It describes:

```text
documentation sections
documentation categories
repository paths
major conceptual areas
relationships between docs and assets
```

Used for:

```text
documentation discovery
future docs search
CLI help systems
runtime reference lookup
marketplace documentation packaging
```

---

# 10. Domains Registry

```text
registry/domains/domains.registry.yaml
```

Role:

```text
Machine-readable catalog of Aegis OS functional domains.
```

Domains include:

```text
engineering
product
design
security
infrastructure
operations
architecture
business
management
documentation
registry
core
shared
```

Used for:

```text
domain filtering
ownership mapping
asset grouping
governance
routing tasks to the right domain
```

---

# 11. Tags Registry

```text
registry/tags/tags.registry.yaml
```

Role:

```text
Machine-readable catalog of standard tags used across Aegis OS assets.
```

It standardizes tags such as:

```text
security
api
database
pricing
ux
release
incident
rbac
tenant-isolation
automation
runtime
```

Used for:

```text
search
filtering
classification
automation
marketplace discovery
avoiding duplicate tag names
```

---

# 12. Releases Registry

```text
registry/releases/releases.registry.yaml
```

Role:

```text
Machine-readable catalog of Aegis OS releases.
```

It describes:

```text
release id
version
status
maturity
release type
release scope
included assets
completion status
release notes
future planned releases
```

Used for:

```text
release tracking
version planning
asset maturity review
roadmap alignment
future release automation
```

---

# 13. Registry Completion Status

```yaml
registry_layer:
  framework: complete
  foundation_registry: complete
  skills_registry: complete
  playbooks_registry: complete
  patterns_registry: complete
  templates_registry: complete
  docs_registry: complete
  domains_registry: complete
  tags_registry: complete
  releases_registry: complete
  registry_index: complete
```

---

# 14. Recommended Registry Validation Order

When validation scripts are introduced, registries should be checked in this order:

```text
1. foundation assets registry
2. tags registry
3. domains registry
4. docs registry
5. skills registry
6. playbooks registry
7. patterns registry
8. templates registry
9. releases registry
10. cross-registry relationships
11. repository path existence
```

Reason:

```text
Foundation assets, tags and domains are foundational.
Asset registries depend on tags, domains and paths.
Release registry depends on all assets.
Cross-registry checks should run last.
```

---

# 15. Future CLI Use Cases

The registry layer should later support commands such as:

```text
aegis registry list
aegis registry validate
aegis skill list
aegis playbook list
aegis template list
aegis pattern list
aegis docs list
aegis asset find --tag security
aegis asset find --domain engineering
aegis release status
```

---

# 16. Future Runtime Use Cases

The registry layer should later allow runtime systems to:

```text
select the right skill for a request
choose a playbook for a workflow
choose a template for the expected output
recommend relevant patterns
load docs as reference context
filter assets by domain and maturity
avoid deprecated assets
trace asset relationships
```

---

# 17. Registry Governance Rules

Registry entries should be updated when:

```text
a new asset is added
an asset path changes
an asset is renamed
an asset becomes deprecated
an asset reaches a higher maturity level
a relationship becomes inaccurate
a new tag or domain is introduced
a release includes new assets
```

---

# 18. Final Principle

> The registry layer turns Aegis OS from a folder of documents into a structured system that tools can understand.
