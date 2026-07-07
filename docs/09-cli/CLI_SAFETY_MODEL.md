Aegis OS — CLI Safety Model

Version: 0.1
Status: CLI Document

1. Introduction

This document defines safety mechanisms for CLI operations.

Some commands can alter runtime, delete artifacts or publish releases. These require explicit safeguards.

2. Safety Rules

The CLI should protect users from:

accidental deletion;
invalid publication;
unsafe runtime actions;
irreversible changes.
3. Safety Mechanisms

Recommended mechanisms:

confirmation prompts;
--force for dangerous operations;
dry-run mode;
validation before execution;
permission checks.
4. Example Commands
aegis release publish --dry-run
aegis skill remove software-architect --force
aegis runtime recover --confirm
5. Final Principle

Safety in the CLI means making dangerous actions explicit, reviewable and hard to trigger by mistake.