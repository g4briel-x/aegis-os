# Aegis OS — Approval Chain Model

Version: 0.1.0  
Status: Draft

## Purpose

This document defines how approvals should work for important Aegis OS changes.

## Approval Levels

```text
minor documentation change
asset update
new asset
registry change
CLI command change
security-sensitive change
release change
architecture change
```

## Approval Chain

A typical approval chain should include:

```text
author
domain reviewer
technical reviewer
governance reviewer
release approver
```

## Required Approval Examples

Registry changes require:

```text
domain review
metadata review
validation pass
```

CLI changes require:

```text
technical review
smoke test update
command reference update
```

Security changes require:

```text
security review
threat assessment
release note entry
```

## Final Principle

> The larger the impact of a change, the stronger the approval chain must be.