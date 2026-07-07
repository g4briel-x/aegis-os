# Senior Debugger Examples

## Overview

This document provides practical examples of how the Senior Debugger Skill operates inside Aegis OS.

The examples demonstrate investigation methods, reasoning patterns and expected deliverables.

---

# Example 1: API Response Time Degradation

## Situation

An e-commerce API response time increased from 200ms to 5 seconds.

Users report slow checkout operations.

---

## Initial Symptoms

Observed:

- increased latency;
- timeout errors;
- customer complaints.

---

## Investigation

Collected evidence:

- API latency metrics;
- database query times;
- application traces;
- recent deployments.

Findings:
API Request
↓
Order Service
↓
Database Query
↓
Slow Query Detected


---

## Root Cause

A new database query introduced during a deployment was missing an optimization index.

The API was not the source of the problem.

The database execution plan was responsible.

---

## Resolution

Actions:

- Add missing index.
- Optimize query.
- Add performance test.
- Monitor query latency.

---

## Prevention

Implemented:

- database migration review;
- query performance checks;
- production monitoring alerts.

---

# Example 2: Memory Leak in Backend Service

## Situation

A service crashes every 72 hours.

Restarting the service temporarily resolves the issue.

---

## Symptoms

Observed:

- increasing memory usage;
- degraded response time;
- container restart.

---

## Investigation

Tools:

- memory profiler;
- heap analysis;
- application metrics.

Finding:

Objects created during requests were never released.

---

## Root Cause

A resource lifecycle problem caused continuous memory growth.

---

## Resolution

Actions:

- Fix object cleanup.
- Add resource management pattern.
- Add memory monitoring.

---

# Example 3: Race Condition

## Situation

A payment system occasionally creates duplicate transactions.

---

## Investigation

Evidence:

- application logs;
- thread analysis;
- transaction history.

Finding:

Two processes modified the same state simultaneously.

---

## Root Cause

Missing synchronization mechanism.

---

## Resolution

Actions:

- Introduce transaction locking.
- Add concurrency tests.
- Review critical sections.

---

# Example 4: Production Deployment Failure

## Situation

A new release causes application startup failure.

---

## Investigation Process

Reviewed:

- deployment logs;
- configuration changes;
- environment variables;
- dependency versions.

---

## Root Cause

A required environment variable was missing in production.

---

## Resolution

Actions:

- Correct deployment configuration.
- Add configuration validation.
- Improve deployment checklist.

---

# Expected Senior Debugger Output

Every investigation should produce:

## Technical Summary

What happened?

## Evidence

What proves it?

## Root Cause

Why did it happen?

## Solution

How is it fixed?

## Prevention

How do we avoid recurrence?

---

# Final Principle

A Senior Debugger does not hunt errors.

A Senior Debugger builds understanding.

Every failure becomes a source of engineering improvement.

