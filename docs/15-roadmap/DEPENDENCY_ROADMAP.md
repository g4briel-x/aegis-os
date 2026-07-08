# Aegis OS — Dependency Roadmap

Version: 0.1  
Status: Roadmap Document

---

# 1. Introduction

This document defines major dependency relationships across roadmap phases.

---

# 2. Dependency Philosophy

Aegis OS follows this principle:

> Work should be sequenced according to what depends on what, not only according to enthusiasm.

---

# 3. Major Dependencies

Examples:

- premium Skills depend on stable Skill specification;
- CLI and SDK depend on stable runtime and registry contracts;
- Marketplace depends on packaging, trust and lifecycle rules;
- certification depends on governance maturity.

---

# 4. Dependency Flow

```text
Specifications

   ↓

Core / Shared

   ↓

Skills / Playbooks / Templates

   ↓

Runtime / Registry

   ↓

SDK / CLI

   ↓

Marketplace / Ecosystem
```

---

# 5. Final Principle

> Dependency visibility reduces rework and protects architectural coherence.
