# IX-Shield Test Matrix

## Purpose
This document defines the concept-stage test matrix for IX-Shield.

The purpose of this matrix is not to imply certified physical testing or mission qualification.
The purpose is to show that the repository’s claims are intended to be checked against structured review and bounded proof-of-concept activities.

## Scope
The IX-Shield test matrix covers concept-stage verification activities related to:

- repository coherence;
- configuration integrity;
- baseline stack screening;
- storm-shelter screening;
- zone mass-budget screening;
- documentation traceability;
- non-claims discipline.

It does not replace:
- formal qualification testing;
- radiation transport validation campaigns;
- structural certification testing;
- human-rating verification.

## Test Matrix Philosophy
The IX-Shield test matrix is built on three principles:

1. test what the repository actually claims;
2. keep concept-stage checks proportional to concept-stage maturity;
3. do not present analytical screening as though it were empirical qualification.

## Test Types Used
IX-Shield uses the following concept-stage test types:

- **DT** — Documentation Test  
  Confirms that required repository documents exist and are internally coherent.

- **CT** — Configuration Test  
  Confirms that machine-readable inputs are present, parseable, and aligned with documentation.

- **AT** — Analysis Test  
  Confirms that scripts run and produce expected categories of screening output.

- **RT** — Reviewability Test  
  Confirms that a technically literate manual reviewer can inspect the repository and understand the claim chain.

---

## T-SHLD-001 — Repository Scope Integrity

### Type
DT

### Objective
Verify that IX-Shield presents itself as a concept-stage proof of concept and not as a flight-ready or validated operational package.

### Method
Review charter, roadmap, architecture overview, and operational non-claims documents.

### Expected Result
All core repository documents consistently describe IX-Shield as concept-stage, non-operational, and non-flight-qualified.

### Pass Criteria
No contradictory language implying certification, crew rating, or validated operational readiness.

---

## T-SHLD-002 — Threat Model Presence

### Type
DT

### Objective
Verify that the repository separates solar particle events, galactic cosmic rays, and secondary-radiation concerns.

### Method
Review the threat-model document and cross-check architecture consequences.

### Expected Result
The threat categories are explicitly named and tied to design logic.

### Pass Criteria
The threat model document exists and includes the three threat categories with associated architectural consequences.

---

## T-SHLD-003 — Baseline Configuration Integrity

### Type
CT

### Objective
Verify that the baseline stack configuration exists in machine-readable form and contains the fields required for screening.

### Method
Inspect the baseline stack configuration file and verify that layer definitions, material names, thickness values, and density values are present.

### Expected Result
The file is parseable and contains a complete baseline stack definition.

### Pass Criteria
The baseline configuration loads successfully and contains all expected baseline layers.

---

## T-SHLD-004 — Baseline Analysis Execution

### Type
AT

### Objective
Verify that the baseline analysis script runs against the baseline stack configuration and produces processed outputs.

### Method
Execute the baseline analysis script using the defined baseline stack file.

### Expected Result
Processed output files are generated for:
- stack layer details;
- stack summary;
- human-readable summary.

### Pass Criteria
Output files are created and reflect the input configuration without script failure.

---

## T-SHLD-005 — Shelter Configuration Integrity

### Type
CT

### Objective
Verify that the storm-shelter add-on configuration exists in machine-readable form and is structurally consistent.

### Method
Inspect the shelter configuration file and verify expected fields for added shielding logic and water-equivalent-oriented interpretation.

### Expected Result
The file is parseable and suitable for the shelter-check script.

### Pass Criteria
The shelter configuration loads successfully and contains the expected additive shelter fields.

---

## T-SHLD-006 — Shelter Analysis Execution

### Type
AT

### Objective
Verify that the shelter analysis script runs and produces processed shelter outputs.

### Method
Execute the shelter analysis script using the shelter configuration.

### Expected Result
Processed shelter outputs are generated for:
- stack summary;
- shelter check summary;
- human-readable interpretation.

### Pass Criteria
All expected shelter output files are generated without script failure.

---

## T-SHLD-007 — Zone Reference Configuration Integrity

### Type
CT

### Objective
Verify that the zone reference configuration exists and contains analyzable zone mass-budget data.

### Method
Inspect the zone configuration file and verify zone identifiers, labels, and mass-allocation values.

### Expected Result
The file is parseable and suitable for zone-level analysis.

### Pass Criteria
All expected zone fields exist and load without error.

---

## T-SHLD-008 — Zone Mass-Budget Execution

### Type
AT

### Objective
Verify that the zone mass-budget analysis script runs and produces processed zone outputs.

### Method
Execute the zone mass-budget script using the zone reference configuration.

### Expected Result
Processed outputs are generated for:
- detailed zone budget table;
- summary markdown;
- summary JSON.

### Pass Criteria
Outputs are generated successfully and include all configured zones.

---

## T-SHLD-009 — Documentation Traceability Presence

### Type
DT

### Objective
Verify that the repository contains a source traceability map and references package.

### Method
Inspect the traceability map and references documents.

### Expected Result
Major architecture claims can be tied to public-domain source categories.

### Pass Criteria
Traceability and references documents both exist and are internally consistent.

---

## T-SHLD-010 — Manual Reviewability

### Type
RT

### Objective
Verify that a technically literate reviewer can understand the repository in a browser-based manual review.

### Method
Manually inspect repository folder structure, processed Markdown summaries, and top-level supporting documents.

### Expected Result
The repository is understandable without hidden tooling or undocumented assumptions.

### Pass Criteria
A reviewer can identify:
- repository purpose;
- concept boundaries;
- main configurations;
- analysis outputs;
- key non-claims.

---

## T-SHLD-011 — Non-Claims Discipline

### Type
DT

### Objective
Verify that non-claims and maturity boundaries are consistently preserved across core documents.

### Method
Review charter, requirements, risk, operational-use, and architecture documents.

### Expected Result
The repository does not contradict its own concept-stage framing.

### Pass Criteria
No document claims complete protection, operational validation, or crew certification.

---

## T-SHLD-012 — Licensing Visibility

### Type
DT

### Objective
Verify that evaluation-only licensing is visible and unambiguous.

### Method
Review the LICENSE file and confirm supporting documentation references the licensing posture.

### Expected Result
The license is present and concept-stage documents align with it.

### Pass Criteria
A manual reviewer can identify the evaluation-only posture without ambiguity.

---

## T-SHLD-013 — Bill Of Materials Presence

### Type
DT

### Objective
Verify that the repository includes a concept-stage bill of materials covering main architecture constituents.

### Method
Inspect the BOM document.

### Expected Result
The BOM identifies the main shielding, structural, shelter, and supporting elements of the concept.

### Pass Criteria
The BOM exists and is sufficiently complete for concept-stage external review.

---

## T-SHLD-014 — Contribution And Security Packaging

### Type
DT

### Objective
Verify that the repository contains serious supporting files for external review posture.

### Method
Inspect repository root for contribution and security files.

### Expected Result
Supporting files are present and aligned with repository maturity.

### Pass Criteria
At minimum, contribution guidance, security guidance, and citation metadata are present.

---

## T-SHLD-015 — Release Packaging Readiness

### Type
RT

### Objective
Verify that the repository can be packaged into a clean proof-of-concept release without unresolved structural gaps.

### Method
Review folder completeness, processed outputs, major docs, and support files.

### Expected Result
The repository can be tagged and reviewed as a coherent PoC package.

### Pass Criteria
No critical component of the intended PoC package is missing.

---

## Matrix Usage Guidance
This matrix should be used to answer a limited question:

**Is the repository complete and disciplined enough to be taken seriously as a concept-stage architecture package?**

It should not be used to answer:
- whether IX-Shield is flight-qualified;
- whether IX-Shield is safe for crew implementation;
- whether IX-Shield is transport-validated.

## Summary
The IX-Shield test matrix is intentionally modest.
It exists to ensure that the repository proves what it says it proves, no more and no less.
