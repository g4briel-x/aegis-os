# Senior Debugger Checklists

## Overview

These checklists ensure that debugging activities follow a rigorous and repeatable process.

A debugging task is considered complete only when investigation, correction and prevention requirements are satisfied.

---

# Incident Investigation Checklist

## Initial Assessment

[ ] Incident description collected

[ ] Affected systems identified

[ ] User impact evaluated

[ ] Business impact evaluated

[ ] Severity level assigned


---

# Evidence Collection Checklist

## Logs

[ ] Application logs collected

[ ] Infrastructure logs collected

[ ] Error patterns identified

[ ] Relevant timestamps correlated


## Metrics

[ ] CPU usage analyzed

[ ] Memory usage analyzed

[ ] Network metrics analyzed

[ ] Database metrics analyzed


## Traces

[ ] Distributed traces reviewed

[ ] Slow operations identified

[ ] Service dependencies mapped


---

# Root Cause Analysis Checklist

## Problem Understanding

[ ] Symptom clearly defined

[ ] Expected behavior documented

[ ] Actual behavior documented

[ ] Reproduction conditions identified


## Investigation

[ ] Multiple hypotheses considered

[ ] Hypotheses validated with evidence

[ ] Root cause separated from symptoms

[ ] Contributing factors identified


---

# Code Debugging Checklist

## Before Modification

[ ] Issue reproduced

[ ] Relevant code identified

[ ] Execution flow understood

[ ] Dependencies analyzed


## During Fix

[ ] Minimal change applied

[ ] Code quality maintained

[ ] Tests created or updated

[ ] Side effects evaluated


## After Fix

[ ] Fix validated

[ ] Regression tests passed

[ ] Performance impact checked

[ ] Documentation updated


---

# Performance Debugging Checklist

[ ] Performance baseline established

[ ] Bottleneck identified

[ ] Profiling performed

[ ] Optimization hypothesis created

[ ] Improvement measured


---

# Production Deployment Checklist

Before deployment:

[ ] Solution reviewed

[ ] Rollback plan prepared

[ ] Monitoring configured

[ ] Risk assessment completed


After deployment:

[ ] Metrics monitored

[ ] Errors checked

[ ] User impact verified

[ ] Incident closed


---

# RCA Quality Checklist

A Root Cause Analysis document must contain:

[ ] Incident summary

[ ] Timeline

[ ] Technical cause

[ ] Contributing factors

[ ] Resolution

[ ] Prevention actions

[ ] Lessons learned


---

# Final Validation

The debugging mission is complete when:

[ ] Root cause is proven

[ ] Solution is validated

[ ] Knowledge is documented

[ ] Future recurrence risk is reduced
