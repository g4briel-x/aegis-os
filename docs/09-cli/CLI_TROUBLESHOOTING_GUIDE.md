Aegis OS — CLI Troubleshooting Guide

Version: 0.1
Status: CLI Guide

1. Introduction

This document defines common troubleshooting patterns for CLI failures.

2. Common Failure Areas

Frequent issues include:

invalid configuration;
missing files;
permission problems;
dependency failures;
runtime connectivity issues;
schema validation failures.
3. Troubleshooting Flow
Failure Detected

    ↓

Read Error Output

    ↓

Check Exit Code

    ↓

Run Doctor Command

    ↓

Validate Config / Structure

    ↓

Retry or Escalate
4. Example Commands
aegis doctor
aegis config validate
aegis validate project
aegis runtime status
5. Final Principle

Troubleshooting guidance should reduce panic and shorten time-to-recovery.