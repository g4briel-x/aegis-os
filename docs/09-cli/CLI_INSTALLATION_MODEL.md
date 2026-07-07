Aegis OS — CLI Installation Model

Version: 0.1
Status: CLI Document

1. Introduction

This document defines how the CLI should be installed and updated across environments.

2. Installation Targets

The CLI may be distributed through:

native binaries;
Python packages;
npm packages;
container images;
internal distribution channels.
3. Installation Goals

Installation should be:

simple;
reproducible;
version-aware;
easy to verify.
4. Post-Install Verification

Recommended verification:

aegis --version
aegis doctor
aegis help
5. Final Principle

Installation should get users to a working CLI quickly, safely and predictably.