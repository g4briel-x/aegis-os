Aegis OS — SLO / SLA Model

Version: 0.1
Status: Operations Document

1. Introduction

This document defines how service quality targets are represented in Aegis OS.

It distinguishes internal operational targets from external commitments.

2. Definitions
SLI

A Service Level Indicator is a measurable signal.

Examples:

request success rate;
p95 latency;
job completion rate.
SLO

A Service Level Objective is a target for an SLI.

SLA

A Service Level Agreement is an externally committed service promise.

3. Example
service_level:
  sli: request_success_rate
  slo: "99.9%"
  measurement_window: 30d
4. Final Principle

Service levels make reliability measurable instead of subjective.