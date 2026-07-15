# Aegis OS Runtime Foundation

Version: v0.6.0  
Status: usable foundation  
Branch: develop/v0.6-runtime

## Role of this file

This file documents the purpose, scope and architecture of the Aegis OS Python runtime introduced in v0.6.0.

## Purpose

The Aegis OS runtime is the Python execution layer responsible for reading, normalizing, resolving and validating Aegis registry assets.

Before v0.6, Aegis OS was mainly a PowerShell CLI and documentation-driven framework. With v0.6, Aegis OS gains a real executable runtime layer.

## Runtime architecture

```text
PowerShell CLI
      |
      v
Python Runtime
      |
      v
Registry YAML files
      |
      v
Assets, docs, skills, playbooks, patterns, templates, domains, tags and releases