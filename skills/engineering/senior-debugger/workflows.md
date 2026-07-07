# Senior Debugger Workflows

## Overview

The Senior Debugger follows structured investigation workflows designed to transform unknown failures into verified solutions.

Every workflow prioritizes evidence collection, controlled experimentation and knowledge preservation.

---

# Workflow 1: Production Incident Investigation

## Objective

Restore system stability while identifying the underlying cause.

---

## Phase 1: Incident Classification

Collect:

- Error description
- Time of occurrence
- Affected components
- User impact
- Business impact
- Recent changes

Output:

Incident profile.

---

## Phase 2: Evidence Collection

Gather:

- Application logs
- Infrastructure logs
- Metrics
- Distributed traces
- Database activity
- Deployment history
- Configuration changes

Rule:

No hypothesis without evidence.

---

## Phase 3: Impact Analysis

Determine:

- Scope of failure
- Number of affected users
- Duration
- Critical functionality impacted

Classify:

- Critical
- High
- Medium
- Low

---

## Phase 4: Root Cause Investigation

Apply:

- Five Whys
- Fault Tree Analysis
- Timeline reconstruction
- Code inspection
- Environment comparison

Goal:

Find the first abnormal condition that created the failure.

---

## Phase 5: Solution Validation

Before deployment:

Validate:

- Fix correctness
- Regression risks
- Performance impact
- Security impact

---

## Phase 6: Post Incident Improvement

Produce:

- RCA document
- Prevention actions
- Monitoring improvements
- Engineering recommendations

---

# Workflow 2: Debugging a Software Defect

## Objective

Identify and eliminate a software defect.

---

## Step 1: Reproduce

Define:

- Expected behavior
- Actual behavior
- Reproduction steps
- Environment conditions

---

## Step 2: Isolate

Reduce the problem:

- component;
- function;
- dependency;
- input data;
- execution path.

---

## Step 3: Analyze Execution

Inspect:

- stack traces;
- variables;
- memory state;
- thread state;
- network communication.

---

## Step 4: Identify Root Cause

Classify:

- Logic error
- Design issue
- Data issue
- Integration failure
- Infrastructure problem

---

## Step 5: Implement Correction

Requirements:

- minimal change;
- clear rationale;
- tests added;
- documentation updated.

---

# Workflow 3: Performance Investigation

## Objective

Identify and remove system bottlenecks.

---

## Step 1: Establish Baseline

Measure:

- response time;
- throughput;
- CPU;
- memory;
- database latency.

---

## Step 2: Locate Bottleneck

Analyze:

- profiling data;
- traces;
- metrics;
- resource usage.

---

## Step 3: Optimize

Possible actions:

- algorithm improvement;
- caching;
- query optimization;
- concurrency improvement;
- architecture change.

---

## Step 4: Validate

Compare:

Before:

- baseline metrics.

After:

- improved metrics.

---

# Workflow 4: Memory Leak Investigation

## Detection

Indicators:

- increasing memory usage;
- crashes after long execution;
- degraded performance.

---

## Investigation

Tools:

- Valgrind
- AddressSanitizer
- heap profiling
- runtime analysis

---

## Resolution

Actions:

- release resources;
- fix ownership issues;
- improve lifecycle management.

---

# Workflow 5: Debugging Rules

The Senior Debugger always:

- reproduces before modifying;
- measures before optimizing;
- investigates before concluding;
- documents before closing;
- prevents recurrence.
