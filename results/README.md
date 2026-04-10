# IX-Shield Results

## Purpose
This directory stores processed concept-stage outputs generated from the IX-Shield screening scripts.

The goal is to preserve browser-reviewable artifacts so that a technically serious reviewer can inspect:
- what was run;
- which inputs were used;
- what outputs were produced;
- what the repository does and does not claim about those outputs.

## Directory Structure
Results are grouped by test or analysis package:

- `T-SHLD-010/` — baseline stack screening
- `T-SHLD-020/` — storm-shelter screening
- `T-SHLD-030/` — zone mass-budget screening

Within each package, run-specific folders contain:
- a run-level README;
- processed machine-readable outputs;
- processed human-readable summaries.

## Interpretation Boundary
All outputs in this directory are concept-stage screening artifacts.

They are:
- useful for repository review;
- useful for configuration-to-output traceability;
- useful for comparing bounded concept variants.

They are not:
- transport-validated radiation results;
- biological risk certification;
- operational authorization;
- implementation approval.

## Review Guidance
A reviewer should inspect each run in the following order:

1. run README;
2. human-readable Markdown summary;
3. machine-readable JSON summary;
4. detailed CSV output where applicable.

This order helps preserve context before looking at detailed values.

## Summary
This directory exists to make IX-Shield reviewable as a serious proof-of-concept repository rather than a collection of undocumented scripts.
