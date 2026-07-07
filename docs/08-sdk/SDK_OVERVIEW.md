# Aegis OS — 08-sdk Bundle

Ce fichier regroupe les documents du dossier `docs/08-sdk/`.

---

## FILE: `docs/08-sdk/SDK_OVERVIEW.md`

# Aegis OS — SDK Overview

Version: 0.1  
Status: SDK Document

---

# 1. Introduction

The SDK layer defines how developers, tools and external systems interact programmatically with Aegis OS.

The SDK provides a structured interface to:

- discover capabilities;
- load components;
- execute workflows;
- manage runtime context;
- validate outputs;
- integrate external tools.

---

# 2. SDK Philosophy

Aegis OS follows this principle:

> The SDK must expose the power of the system without exposing unnecessary internal complexity.

The SDK should be:

- stable;
- discoverable;
- strongly structured;
- portable;
- versioned.

---

# 3. SDK Objectives

The SDK enables:

- application integration;
- agent construction;
- custom orchestration;
- component execution;
- automation;
- ecosystem extension.

---

# 4. SDK Layers

```text
Application Code

    ↓

SDK Interface Layer

    ↓

Runtime / Registry / Orchestrator

    ↓

Skills / Agents / Playbooks / Knowledge

5. SDK Core Capabilities

A standard SDK should allow:

component discovery;
metadata access;
execution requests;
validation requests;
context creation;
configuration loading;
event subscription;
runtime inspection.
6. SDK Design Principles
Stable Surface

Public interfaces should evolve predictably.

Explicit Contracts

Inputs and outputs must be clear.

Language Compatibility

The SDK model should be portable across languages.

Runtime Safety

Unsafe or privileged operations must be explicitly controlled.

7. SDK Consumers

Typical users:

application developers;
automation engineers;
AI platform builders;
orchestration developers;
internal tooling systems.
8. Final Principle

The SDK is the programmable interface of Aegis OS. It transforms the platform into a usable development surface.