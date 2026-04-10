# IX-Shield PoC Test Procedures

## Purpose
This document defines the concept-stage procedures used to inspect, execute, and review the IX-Shield proof-of-concept package.

These procedures are repository procedures.
They are not qualification procedures, crew-safety procedures, or mission-approval procedures.

## Procedure Philosophy
The procedures in this document are designed to answer a limited question:

**Can a technically serious reviewer inspect the repository, run the provided screening logic, and confirm that the stored outputs match the defined concept inputs?**

The procedures are intentionally modest and bounded to the repository’s actual maturity.

## Pre-Procedure Conditions
Before performing any IX-Shield PoC procedure, confirm the following:

- the repository is complete enough for review;
- the repository files are present in their expected paths;
- the reviewer understands that the repository is concept-stage and evaluation-only;
- the reviewer does not interpret screening output as validated operational performance.

If these conditions are not met, pause the procedure and resolve the repository gap first.

---

## Procedure PT-SHLD-001 — Documentation Integrity Review

### Objective
Confirm that the core documentation exists and is internally coherent.

### Inputs
- project charter
- roadmap
- architecture overview
- threat model
- requirements
- science basis
- risk and non-claims documents

### Steps
1. Open the core documents in the `docs/` folder.
2. Confirm that IX-Shield is consistently described as:
   - concept-stage;
   - proof of concept;
   - non-operational;
   - non-flight-qualified.
3. Confirm that no core document claims:
   - complete radiation protection;
   - validated crew safety;
   - certification or operational readiness.
4. Confirm that the architecture narrative is consistent with the threat model and requirements.

### Expected Result
The repository presents a stable, bounded concept narrative.

### Pass Condition
No contradiction is found between the repository’s maturity claims and its actual content.

---

## Procedure PT-SHLD-002 — Baseline Configuration Inspection

### Objective
Confirm that the baseline stack configuration is present and structurally inspectable.

### Inputs
- baseline stack configuration file

### Steps
1. Open the baseline stack configuration in the `configs/stacks/` folder.
2. Confirm that the file is machine-readable.
3. Confirm that each layer includes:
   - layer identifier;
   - material label;
   - thickness;
   - density;
   - notes or role field if used.
4. Confirm that the file represents a coherent baseline stack.

### Expected Result
The baseline configuration is readable and complete enough for the baseline analysis script.

### Pass Condition
The baseline configuration loads cleanly and contains all required baseline fields.

---

## Procedure PT-SHLD-003 — Baseline Analysis Run

### Objective
Run the baseline stack analysis and confirm that expected outputs are produced.

### Inputs
- baseline stack configuration
- baseline analysis script

### Steps
1. Execute the baseline analysis script using the baseline configuration file.
2. Confirm that the script completes without failure.
3. Confirm that the following processed outputs are generated:
   - layer-detail table;
   - stack summary JSON;
   - human-readable summary Markdown.
4. Open the processed outputs and confirm they reflect the baseline input stack.

### Expected Result
A complete baseline screening package is produced.

### Pass Condition
All expected baseline outputs are generated and internally consistent with the input file.

---

## Procedure PT-SHLD-004 — Shelter Configuration Inspection

### Objective
Confirm that the storm-shelter enhancement configuration is present and structurally inspectable.

### Inputs
- storm-shelter configuration file

### Steps
1. Open the shelter configuration in the `configs/stacks/` folder.
2. Confirm that the file is machine-readable.
3. Confirm that it clearly indicates:
   - baseline relationship or shelter add-on role;
   - added shielding logic;
   - water-equivalent-oriented interpretation fields if used.
4. Confirm that the shelter concept is coherent as a local enhancement rather than a disconnected file.

### Expected Result
The shelter configuration is understandable and suitable for screening.

### Pass Condition
The shelter configuration loads cleanly and exposes the expected shelter fields.

---

## Procedure PT-SHLD-005 — Shelter Analysis Run

### Objective
Run the shelter analysis and confirm that expected outputs are produced.

### Inputs
- shelter configuration
- shelter analysis script

### Steps
1. Execute the shelter analysis script using the shelter configuration.
2. Confirm that the script completes without failure.
3. Confirm that the following processed outputs are generated:
   - shelter stack summary;
   - shelter-check JSON summary;
   - shelter-check Markdown interpretation;
   - summary Markdown.
4. Confirm that the outputs reflect the configured shelter enhancement rather than the baseline alone.

### Expected Result
A complete shelter-screening package is produced.

### Pass Condition
All expected shelter outputs are generated and consistent with the shelter configuration.

---

## Procedure PT-SHLD-006 — Zone Configuration Inspection

### Objective
Confirm that the zone reference configuration is present and structurally inspectable.

### Inputs
- zone reference configuration file

### Steps
1. Open the zone configuration in the `configs/zones/` folder.
2. Confirm that the file is machine-readable.
3. Confirm that each zone includes:
   - zone identifier;
   - zone label;
   - mass-allocation value or equivalent field;
   - notes or interpretation field if present.
4. Confirm that the set of zones represents a coherent architecture framing.

### Expected Result
The zone configuration is ready for zone mass-budget screening.

### Pass Condition
The zone configuration loads cleanly and contains all expected zones and fields.

---

## Procedure PT-SHLD-007 — Zone Mass-Budget Run

### Objective
Run the zone mass-budget analysis and confirm that expected outputs are produced.

### Inputs
- zone reference configuration
- zone mass-budget analysis script

### Steps
1. Execute the zone mass-budget analysis script using the zone configuration.
2. Confirm that the script completes without failure.
3. Confirm that the following processed outputs are generated:
   - detailed zone mass-budget table;
   - summary Markdown;
   - summary JSON.
4. Confirm that the outputs include all configured zones.

### Expected Result
A complete zone mass-budget screening package is produced.

### Pass Condition
All expected zone outputs are generated and match the configured zone set.

---

## Procedure PT-SHLD-008 — Processed Output Review

### Objective
Confirm that stored processed outputs are readable by a manual reviewer.

### Inputs
- processed Markdown summaries
- processed JSON files
- processed CSV files

### Steps
1. Open the processed result folders.
2. Confirm that each run package contains:
   - a README or context note;
   - stored outputs;
   - human-readable summary material.
3. Confirm that the output package can be understood without rerunning scripts first.
4. Confirm that the output package remains consistent with the repository’s concept-stage framing.

### Expected Result
Manual inspection of stored results is practical.

### Pass Condition
A technically serious reviewer can inspect the output package directly in the repository.

---

## Procedure PT-SHLD-009 — Traceability Review

### Objective
Confirm that major technical claims are traceable to cited public-domain sources.

### Inputs
- source traceability map
- references document

### Steps
1. Open the traceability map.
2. Confirm that major architecture claims and design positions are linked to source categories or references.
3. Open the references document.
4. Confirm that the cited references correspond to the traceability map entries.
5. Confirm that traceability is broad enough to support repository review.

### Expected Result
The repository’s architecture logic is anchored to external sources rather than unsupported assertion.

### Pass Condition
Major claims can be traced from repository logic to cited references.

---

## Procedure PT-SHLD-010 — Packaging Completeness Review

### Objective
Confirm that IX-Shield is packaged as a serious concept-stage repository.

### Inputs
- repository root files
- support files
- BOM
- processed results

### Steps
1. Confirm that the root-level support files are present.
2. Confirm that the BOM exists and is reviewable.
3. Confirm that citation, contribution, and security files are present.
4. Confirm that the repository can be understood as a coherent package.
5. Confirm that the README, when added, does not contradict any underlying repository file.

### Expected Result
The repository is release-ready as a proof-of-concept package.

### Pass Condition
No critical packaging component is missing.

---

## Procedure PT-SHLD-011 — Non-Claims Confirmation

### Objective
Confirm that the repository does not overstate what it proves.

### Inputs
- architecture overview
- requirements
- risk document
- operational-use and non-claims document
- processed summaries

### Steps
1. Review the non-claims language across the repository.
2. Confirm that processed summaries do not introduce stronger claims than the source documents support.
3. Confirm that no document presents the concept as validated for real-world deployment.
4. Confirm that any numerical screening values are presented as concept-stage outputs only.

### Expected Result
Repository restraint is preserved from inputs through outputs.

### Pass Condition
No unsupported implementation, safety, or validation claim appears in the repository.

## General Recording Guidance
When performing any PoC procedure, record:

- procedure identifier;
- date performed;
- file paths used;
- pass or fail result;
- any anomalies or corrective notes.

This is optional at very early draft stage but recommended for serious review posture.

## Procedure Failure Handling
If a procedure fails:

1. record the failure clearly;
2. identify whether the cause is:
   - missing file;
   - broken script;
   - inconsistent document language;
   - incomplete output package;
   - packaging gap;
3. correct the repository issue;
4. rerun the affected procedure.

Do not silently ignore failed procedures.

## Summary
These procedures exist to ensure IX-Shield is not merely described as disciplined, but actually behaves like a disciplined concept-stage repository when inspected and run.
