Aegis OS — CLI Non-Interactive Mode

Version: 0.1
Status: CLI Document

1. Introduction

This document defines how the CLI behaves in non-interactive environments such as CI/CD, scripts and automated runners.

2. Non-Interactive Principles

The CLI should support automation without requiring prompts or manual confirmations.

3. Expected Features

Recommended flags:

--no-interactive
--yes
--json
--quiet
--force
4. Automation Rules

In non-interactive mode:

prompts must be disabled;
output should be machine-friendly when requested;
failures must return stable exit codes;
dangerous operations must require explicit flags.
5. Final Principle

A CLI is production-ready only when it works reliably without a human at the keyboard.