Aegis OS — SDK Versioning Model

Version: 0.1
Status: SDK Document

1. Introduction

This document defines how SDK versions evolve in relation to Aegis OS platform versions.

The objective is to preserve:

compatibility;
predictability;
upgrade safety.
2. Versioning Philosophy

SDKs should follow semantic versioning while clearly documenting their relationship to platform versions.

3. Compatibility Model

Example:

sdk:
  version: 1.2.0
  compatible_with:
    - aegis-os >= 0.8.0
    - aegis-os < 1.0.0
4. Breaking Changes

Breaking SDK changes require:

major version increment;
migration notes;
interface diff documentation.
5. Final Principle

SDK versioning protects developers from unexpected interface drift.