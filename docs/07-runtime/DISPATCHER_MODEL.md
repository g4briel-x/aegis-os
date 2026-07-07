Aegis OS — Dispatcher Model

Version: 0.1
Status: Runtime Document

1. Introduction

The Dispatcher routes executable tasks to the appropriate runtime components.

It decides where execution should occur.

2. Responsibilities

The Dispatcher must:

identify the correct execution target;
pass validated context;
enforce routing rules;
record dispatch history.
3. Dispatch Inputs

Dispatch decisions consider:

task type;
required Skill or Agent;
runtime load;
security policy;
environment.
4. Dispatch Flow
Task Ready

 ↓

Capability Match

 ↓

Dispatch Decision

 ↓

Execution Target

 ↓

Confirmation
5. Final Principle

Dispatching connects abstract planned work to real executable capabilities.

FILE: docs/07-runtime/RUNTIME_STATE_MANAGER.md
Aegis OS — Runtime State Manager

Version: 0.1
Status: Runtime Document

1. Introduction

The Runtime State Manager tracks the live state of executions, components and workflows.

It gives the Runtime situational awareness.

2. Responsibilities

The State Manager must track:

task states;
workflow states;
execution states;
resource states;
failure and recovery states.
3. State Update Flow
Execution Event

 ↓

State Transition

 ↓

Validation

 ↓

Persistence

 ↓

Notification
4. State Integrity Rules

State updates must be:

valid;
ordered;
auditable;
recoverable.
5. Final Principle

Runtime state is the operational truth that allows Aegis OS to remain coherent while executing.