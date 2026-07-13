## FILE: `registry/_framework/README.md`

# Aegis OS — Registry Framework

Version: 0.1.0  
Status: Draft  
Domain: Registry  
Category: Asset Catalog

---

# 1. Purpose

The Registry Framework defines how Aegis OS assets are indexed in a structured and machine-readable way.

It connects documentation, skills, playbooks, patterns and templates into discoverable registries that can later be used by a CLI, runtime engine, marketplace, automation scripts or AI orchestration layer.

---

# 2. Why Registry Exists

Indexes such as `skills/INDEX.md` and `templates/INDEX.md` are useful for humans.

Registries are useful for systems.

A registry allows Aegis OS to answer questions such as:

```text
Which skills exist?
Which playbooks are related to this skill?
Which template should be used after this playbook?
Which assets belong to the security domain?
Which assets are ready, draft or deprecated?
Which assets can be exposed in a marketplace?
```

---

# 3. Registry Scope

The Registry Framework covers:

```text
skills
playbooks
patterns
templates
docs
domains
tags
versions
maturity levels
relationships
status
ownership
```

---

# 4. Standard Registry Types

```text
skill registry
playbook registry
pattern registry
template registry
documentation registry
domain registry
tag registry
release registry
```

---

# 5. Registry Principle

> Aegis OS assets should be easy to discover by humans and easy to resolve by systems.
