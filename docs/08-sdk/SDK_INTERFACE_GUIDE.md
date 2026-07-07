Aegis OS — SDK Interface Guide

Version: 0.1
Status: SDK Guide

1. Introduction

This guide defines how SDK interfaces should be designed across languages.

The goal is to preserve a consistent developer experience.

2. Interface Principles

SDK interfaces should be:

simple to discover;
consistent across modules;
explicit in behavior;
version-aware.
3. Common Interface Areas

All SDKs should expose similar domains:

skills
agents
workflows
runtime
registry
validation
config
memory
4. Standard Operations

Each interface family should prefer standard verbs:

list
get
create
update
delete
execute
validate
inspect
5. Input / Output Contracts

Every public method should define:

required parameters;
optional parameters;
result format;
possible errors.
6. Final Principle

SDK interfaces should make Aegis OS feel coherent, predictable and professional in every supported language.