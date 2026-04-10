# IX-Shield Data and Results Template

## Purpose
This document defines the template used to structure IX-Shield processed outputs and result summaries.

The goal is to make every result package easy to inspect, compare, and review.

This template is not a scientific journal format.
It is a repository-facing results format for concept-stage consistency.

## Result Package Objectives
Each result package should make it easy for a reviewer to answer:

- what was analyzed;
- which input file was used;
- which script produced the output;
- what the main screening values were;
- what the repository does and does not claim about the result.

## Standard Result Package Elements
Each result package should contain, as applicable:

1. a run-level README;
2. machine-readable outputs;
3. human-readable summary output;
4. references to input files and scripts used;
5. non-claims language proportional to the result.

## Template — Run README

Use the following structure for run-level `README.md` files.

### Title
- Name of the run package

### Purpose
- Brief explanation of what this run represents

### Inputs
- configuration file path(s)
- script file path(s)

### Outputs
- list of generated files

### Notes
- assumptions specific to the run
- interpretation boundaries
- warnings if relevant

## Template — Markdown Summary

Use the following structure for human-readable result summaries.

### 1. Run Identification
Include:
- run identifier;
- analysis type;
- date or version if needed.

### 2. Input Reference
Include:
- configuration file path;
- script file path;
- supporting file paths if relevant.

### 3. Key Screening Values
Include the main computed values relevant to the run.

Examples:
- total areal density;
- estimated water-equivalent value;
- zone mass totals;
- layer contribution summary.

### 4. Interpretation
Include a short explanation of what the values suggest at concept stage.

### 5. Limits
Explicitly state:
- that this is a screening output;
- that it is not a validated mission result;
- that it should not be treated as implementation authorization.

## Template — JSON Summary

Use the following structure when practical for machine-readable summaries:

- run identifier;
- analysis type;
- input file paths;
- key numerical outputs;
- notes;
- limitations.

The exact field names may vary by script, but the intent should remain stable.

## Template — CSV Table

For detailed tabular outputs, prefer columns that are:

- clearly labeled;
- units-aware where relevant;
- traceable to the input configuration.

Examples:
- layer name;
- material;
- thickness;
- density;
- areal density;
- zone identifier;
- allocated mass.

## Recommended Result Summary Language
The following language style is recommended for Markdown summaries:

- factual;
- bounded;
- concept-stage;
- non-hyped;
- easy to inspect.

Avoid:
- claims of validation;
- inflated protection language;
- vague promotional language.

## Result Interpretation Guardrails
Every result summary should preserve these guardrails:

- do not imply flight readiness;
- do not imply crew safety certification;
- do not collapse mixed-radiation problems into a single generic claim;
- do not convert screening metrics into medical conclusions.

## Suggested Run README Template

```text
# <Run Name>

## Purpose
<What this run evaluates>

## Inputs
- <config path>
- <script path>

## Outputs
- <output path 1>
- <output path 2>
- <output path 3>

## Notes
- <assumption or limitation>
- <interpretation boundary>

Suggested Markdown Summary Template
# <Run Summary Title>

## Run Identification
- Run ID: <run_id>
- Analysis Type: <analysis_type>

## Input Reference
- Config: <config_path>
- Script: <script_path>

## Key Screening Values
- <key value 1>
- <key value 2>
- <key value 3>

## Interpretation
<Short, bounded concept-stage interpretation>

## Limits
- Screening output only
- Not transport validated
- Not operational authorization

Suggested JSON Summary Pattern
{
  "run_id": "<run_id>",
  "analysis_type": "<analysis_type>",
  "input_files": {
    "config": "<config_path>",
    "script": "<script_path>"
  },
  "key_outputs": {},
  "notes": [],
  "limitations": [
    "screening output only",
    "not transport validated",
    "not operational authorization"
  ]
}

Repository Consistency Rule

If a future result package departs from this template, it should still preserve the same core ideas:

identifiable run;
visible inputs;
visible outputs;
visible limitations.
Summary

The IX-Shield data and results template exists to keep processed outputs readable, comparable, and professionally bounded across the repository.
