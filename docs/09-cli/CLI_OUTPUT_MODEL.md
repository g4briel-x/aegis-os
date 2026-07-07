Aegis OS — CLI Output Model

Version: 0.1
Status: CLI Document

1. Introduction

This document defines how CLI output should be formatted for humans and automation systems.

2. Output Modes

The CLI should support:

human-readable output;
structured JSON output;
quiet mode;
machine-only mode.
3. Human Output Rules

Human output should be:

readable;
grouped logically;
concise;
explicit about success, warning and failure states.
4. Machine Output Rules

Machine-readable output should be:

valid;
deterministic;
schema-consistent;
free of decorative noise.

Example:

{
  "status": "ok",
  "component": "software-architect",
  "version": "1.0.0"
}
5. Final Principle

CLI output should serve both humans and automation without forcing either one to parse ambiguity.