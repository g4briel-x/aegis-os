Aegis OS — SDK Error Model

Version: 0.1
Status: SDK Document

1. Introduction

This document defines how SDKs report failures to developers.

A good SDK error model should be:

explicit;
typed when possible;
actionable;
consistent.
2. Error Categories

Common categories:

configuration errors;
authentication errors;
validation errors;
execution errors;
timeout errors;
compatibility errors.
3. Error Contract

Errors should expose:

code;
message;
category;
suggested action;
underlying cause when safe.
4. Final Principle

SDK errors should help developers recover quickly, not simply report failure.