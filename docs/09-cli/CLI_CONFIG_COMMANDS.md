# Aegis OS — 09-cli Advanced Bundle


---

## FILE: `docs/09-cli/CLI_CONFIG_COMMANDS.md`

# Aegis OS — CLI Config Commands

Version: 0.1  
Status: CLI Document

---

# 1. Introduction

This document defines commands related to configuration management in the Aegis OS CLI.

The CLI must allow users to inspect, validate and update configuration safely.

---

# 2. Example Commands

```text
aegis config show
aegis config get runtime.default
aegis config set runtime.default local
aegis config validate
aegis config reset
3. Responsibilities

Configuration commands should support:

reading effective configuration;
setting values;
validating configuration state;
resetting invalid configuration;
showing environment overrides.
4. Final Principle

Configuration commands should make system behavior visible and controllable without encouraging unsafe changes.

FILE: docs/09-cli/CLI_AUTH_COMMANDS.md
Aegis OS — CLI Auth Commands

Version: 0.1
Status: CLI Document

1. Introduction

This document defines commands related to authentication and identity handling in the CLI.

2. Example Commands
aegis auth login
aegis auth logout
aegis auth status
aegis auth whoami
aegis auth token rotate
3. Responsibilities

Authentication commands should support:

sign-in flows;
token inspection;
session status;
identity confirmation;
safe logout.
4. Security Rules

Auth commands must:

avoid printing secrets by default;
require confirmation for destructive auth actions;
log security-relevant events.
5. Final Principle

Authentication commands should confirm identity without exposing sensitive credentials.