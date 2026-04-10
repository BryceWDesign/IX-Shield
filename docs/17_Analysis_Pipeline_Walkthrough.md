# IX-Shield Analysis Pipeline Walkthrough

## Purpose
This document explains the IX-Shield analysis pipeline from configuration input through processed result output.

The purpose is to make the repository’s analytical behavior easy to inspect and difficult to misrepresent.

This is a screening pipeline walkthrough.
It is not a transport-validation workflow.

## Pipeline Philosophy
The IX-Shield analysis pipeline is intentionally simple.

It is designed to:
- load bounded machine-readable concept inputs;
- compute concept-stage screening values;
- write processed artifacts for browser-based review;
- preserve clear separation between screening and validation.

The pipeline is not designed to:
- generate mission-certified dose predictions;
- replace transport codes;
- imply operational readiness.

## Pipeline Stages
The IX-Shield pipeline is organized into five stages:

1. configuration definition;
2. configuration validation;
3. screening computation;
4. processed output generation;
5. manual review packaging.

## Stage 1 — Configuration Definition
The pipeline begins with machine-readable concept inputs stored in the `configs/` directory.

Current configuration classes include:
- baseline stack configuration;
- storm-shelter add-on configuration;
- zone reference configuration.

These files define the repository’s analyzable assumptions.

### Why This Stage Matters
A repository cannot claim reproducibility if the concept only exists in prose.
Configuration files turn the concept into inspectable inputs.

## Stage 2 — Configuration Validation
Each analysis script checks that its input file contains the minimum required fields.

Validation logic is intentionally modest but important.
It helps catch:
- missing fields;
- empty layer lists;
- malformed structure;
- incomplete zone definitions.

### Why This Stage Matters
A script that silently accepts broken inputs weakens the repository.
Basic validation is part of seriousness.

## Stage 3 — Screening Computation
After validation, the analysis scripts compute concept-stage summary values.

### Baseline Stack Analysis
The baseline analysis computes:
- per-layer areal density;
- total areal density;
- dominant layer contributions;
- a human-readable summary package.

### Shelter Analysis
The shelter analysis computes:
- add-on layer areal density;
- total local add-on areal density;
- simple water-equivalent proxy values;
- target-comparison logic for the configured shelter concept.

### Zone Mass-Budget Analysis
The zone analysis computes:
- zone-by-zone allocated mass;
- total configured mass;
- relative zone mass fractions;
- basic mass-distribution summaries.

### Why This Stage Matters
This stage transforms concept inputs into reviewable outputs without pretending that simple calculations equal validated performance.

## Stage 4 — Processed Output Generation
After computation, the pipeline writes processed artifacts to the `results/` directory.

Typical processed outputs include:
- CSV tables;
- JSON summaries;
- Markdown summaries.

This repository stores outputs so that a reviewer can inspect results directly without having to run code first.

### Why This Stage Matters
Stored outputs improve transparency and make manual review easier.
They also help expose whether the analysis scripts are producing coherent artifacts.

## Stage 5 — Manual Review Packaging
The final stage is not additional computation.
It is presentation and review readiness.

At this stage, the pipeline relies on:
- run-level README files;
- processed Markdown summaries;
- repository documentation;
- traceability and BOM support.

### Why This Stage Matters
IX-Shield is meant to be reviewed in a browser by technically literate humans.
The analysis pipeline must therefore end in artifacts that are understandable without hidden context.

## Current Analysis Scripts
The current IX-Shield analysis pipeline is centered on three scripts:

### `src/analysis/stack_areal_density.py`
Role:
- baseline stack screening;
- per-layer and total areal-density reporting.

### `src/analysis/storm_shelter_check.py`
Role:
- shelter add-on screening;
- simple water-equivalent proxy comparison.

### `src/analysis/zone_mass_budget.py`
Role:
- geometry-aware zone mass allocation summary.

Each script is intentionally narrow in scope.

## Current Input / Output Flow

### Baseline Flow
Input:
- `configs/stacks/baseline_zone_a_v1.json`

Script:
- `src/analysis/stack_areal_density.py`

Outputs:
- processed CSV details;
- processed JSON summary;
- processed Markdown summary.

### Shelter Flow
Input:
- `configs/stacks/storm_shelter_addon_10cm_we_v1.json`

Script:
- `src/analysis/storm_shelter_check.py`

Outputs:
- processed JSON summary;
- processed shelter-check JSON;
- processed Markdown summaries.

### Zone Flow
Input:
- `configs/zones/reference_vehicle_zones_v1.json`

Script:
- `src/analysis/zone_mass_budget.py`

Outputs:
- processed CSV budget table;
- processed JSON summary;
- processed Markdown summary.

## What The Pipeline Proves
The IX-Shield pipeline proves that the repository can:

- define a concept in machine-readable form;
- run bounded screening logic against that concept;
- preserve reviewable outputs;
- support consistency between documents and artifacts.

## What The Pipeline Does Not Prove
The IX-Shield pipeline does not prove:

- radiation transport accuracy;
- biological risk acceptance;
- mission-level safety;
- structural qualification;
- crew-safe implementation.

This distinction must be preserved whenever outputs are discussed publicly.

## Failure Conditions In The Pipeline
The pipeline should be treated as failed if any of the following occur:

- required config fields are missing;
- a script does not run successfully;
- outputs are absent or incomplete;
- processed summaries contradict the inputs;
- outputs overstate what the scripts actually computed.

## Pipeline Discipline Rules
Future additions to the pipeline should preserve these rules:

1. keep each script narrow in purpose;
2. validate inputs before computing outputs;
3. write machine-readable and human-readable results;
4. state limitations inside processed summaries;
5. avoid promotional language in outputs.

## Recommended Review Method
A reviewer should inspect the pipeline in this order:

1. read the architecture and threat-model documents;
2. inspect the configuration files;
3. inspect the analysis scripts;
4. inspect the processed outputs;
5. confirm that the outputs stay inside concept-stage claims.

This order helps prevent numerical outputs from being read without context.

## Summary
The IX-Shield analysis pipeline is intentionally modest, transparent, and review-oriented.

Its value is not that it solves radiation transport.
Its value is that it turns the concept into structured, inspectable, reproducible screening artifacts.
