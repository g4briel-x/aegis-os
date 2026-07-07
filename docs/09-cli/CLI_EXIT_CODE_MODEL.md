Aegis OS — CLI Exit Code Model

Version: 0.1
Status: CLI Document

1. Introduction

This document defines exit code behavior for the Aegis OS CLI.

Exit codes allow scripts and automation to detect command outcomes reliably.

2. Exit Code Philosophy

Aegis OS follows this principle:

A CLI command should not only say what happened. It should signal it programmatically.

3. Standard Exit Codes
0   Success
1   General failure
2   Invalid usage
3   Validation failure
4   Permission error
5   Configuration error
6   Dependency error
7   Runtime execution error
8   Timeout
9   Internal CLI error
4. Rules

Exit codes should be:

stable;
documented;
consistent across command families.
5. Final Principle

Exit codes are the automation contract of the CLI.