Aegis OS — Marketplace Package Model

Version: 0.1
Status: Marketplace Document

1. Introduction

This document defines how reusable Marketplace artifacts are packaged.

A Marketplace package is a portable, versioned intelligence component bundle.

2. Package Definition

A package represents:

A distributable unit containing one or more Aegis OS components, their metadata and installation instructions.

Examples:

a Skill package;
a Playbook pack;
a Pattern library;
a plugin extension.
3. Package Structure

Example:

package-name/

├── MANIFEST.md
├── metadata.yaml
├── README.md
├── components/
├── dependencies/
├── checksums/
└── signatures/
4. Required Package Metadata

Example:

package:
  name:
  type:
  version:
  publisher:
  components:
  dependencies:
  compatibility:
  trust_level:
5. Package Types

Supported package types may include:

skill-package;
agent-package;
playbook-package;
pattern-package;
template-package;
plugin-package;
bundle-package.
6. Final Principle

A package is the operational shipping format of reusable intelligence.