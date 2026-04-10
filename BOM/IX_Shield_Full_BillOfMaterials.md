# IX-Shield Full Bill of Materials

## Purpose
This bill of materials records the concept-stage material, subsystem, and package constituents used in the IX-Shield proof-of-concept repository.

This BOM is intended for technical review and repository traceability.
It is not a procurement package.
It is not a manufacturing release.
It is not a flight hardware list.

## BOM Scope
This BOM covers:

- baseline transit-shell concept layers;
- storm-shelter add-on concept layers;
- zone-level architecture mass groupings;
- analysis and repository support items.

## BOM Conventions
- Quantities are concept-stage quantities, not procurement-authoritative quantities.
- Materials are described at the architecture level, not vendor-SKU level.
- Dimensions and masses are carried in their source configs and result files where applicable.
- “Status” indicates concept maturity inside this repository, not operational readiness.

---

## Section A — Baseline Transit Shell Constituents

| BOM ID | Item Name | Category | Primary Function | Status | Notes |
|---|---|---|---|---|---|
| IXB-001 | Aluminum Alloy Exterior Skin | Baseline Layer | Exterior-facing functional boundary | Defined in config | Thin practical exterior boundary; not treated as the primary shielding answer |
| IXB-002 | Polymer Honeycomb / Protective Intermediate Region | Baseline Layer | Spacing and multifunctional separation | Defined in config | Placeholder stand-off/protective region compatible with future stuffed-panel logic |
| IXB-003 | High-Density Polyethylene | Baseline Layer | Primary hydrogen-rich passive shielding mass | Defined in config | Main low-Z shielding contributor in baseline stack |
| IXB-004 | Borated Polyethylene Liner | Baseline Layer | Interior support and neutron-aware interlayer | Defined in config | Bounded concept-stage inner liner |
| IXB-005 | Interior Composite Panel | Baseline Layer | Crew-facing interior boundary | Defined in config | Habitable-side cleanable boundary |

### Baseline Stack Reference
Primary file:
- `configs/stacks/baseline_zone_a_v1.json`

Processed screening outputs:
- `results/T-SHLD-010/RUN_SIMULATED_BASELINE_V1/processed/stack_layer_details.csv`
- `results/T-SHLD-010/RUN_SIMULATED_BASELINE_V1/processed/stack_summary.json`
- `results/T-SHLD-010/RUN_SIMULATED_BASELINE_V1/processed/summary.md`

---

## Section B — Storm Shelter Add-On Constituents

| BOM ID | Item Name | Category | Primary Function | Status | Notes |
|---|---|---|---|---|---|
| IXS-001 | Contained Water Module | Shelter Layer | Primary local shelter mass | Defined in config | Used to represent concentrated water-equivalent refuge mass |
| IXS-002 | Hydrogel Matrix | Shelter Layer | Structured hydrogen-rich shelter mass | Defined in config | Supports shaped local hydrogen-rich add-on logic |
| IXS-003 | Borated Polyethylene Shelter Liner | Shelter Layer | Secondary neutron-aware local liner | Defined in config | Bounded local interior shelter layer |
| IXS-004 | Interior Composite Facing | Shelter Layer | Crew-facing refuge boundary | Defined in aspirational config | Included in aspirational 20 cm WE growth-path concept |

### Shelter Configuration References
Primary practical concept:
- `configs/stacks/storm_shelter_addon_10cm_we_v1.json`

Aspirational growth path:
- `configs/stacks/storm_shelter_addon_20cm_we_aspirational.json`

Processed screening outputs:
- `results/T-SHLD-020/RUN_SIMULATED_STORM_SHELTER_10CM_V1/processed/stack_summary.json`
- `results/T-SHLD-020/RUN_SIMULATED_STORM_SHELTER_10CM_V1/processed/storm_shelter_check.json`
- `results/T-SHLD-020/RUN_SIMULATED_STORM_SHELTER_10CM_V1/processed/summary.md`
- `results/T-SHLD-020/RUN_SIMULATED_STORM_SHELTER_10CM_V1/processed/storm_shelter_check.md`

---

## Section C — Zone-Level Architecture Mass Groupings

| BOM ID | Item Name | Category | Primary Function | Status | Notes |
|---|---|---|---|---|---|
| IXZ-001 | Crew Core | Zone Group | Most occupied central habitat region | Defined in config | Crew-adjacent mass concentration anchor |
| IXZ-002 | Storm Shelter Envelope | Zone Group | Localized refuge enhancement region | Defined in config | Concentrated additional mass surrounding smaller refuge |
| IXZ-003 | Logistics Ring | Zone Group | Surrounding supplies and consumables region | Defined in config | Multifunctional mission mass contributing to protection geometry |
| IXZ-004 | Equipment Bay | Zone Group | Systems and equipment-adjacent region | Defined in config | Non-crew systems mass affecting local geometry |
| IXZ-005 | Peripheral Hull Region | Zone Group | Outer shell and distributed structure region | Defined in config | Distributed outer vehicle mass |

### Zone Reference File
Primary file:
- `configs/zones/reference_vehicle_zones_v1.json`

Processed screening outputs:
- `results/T-SHLD-030/RUN_SIMULATED_ZONE_MASS_BUDGET_V1/processed/zone_mass_budget.csv`
- `results/T-SHLD-030/RUN_SIMULATED_ZONE_MASS_BUDGET_V1/processed/zone_mass_budget_summary.json`
- `results/T-SHLD-030/RUN_SIMULATED_ZONE_MASS_BUDGET_V1/processed/zone_mass_budget.md`

---

## Section D — Analysis Software Constituents

| BOM ID | Item Name | Category | Primary Function | Status | Notes |
|---|---|---|---|---|---|
| IXA-001 | `stack_areal_density.py` | Analysis Script | Baseline stack areal-density screening | Implemented | Computes per-layer and total areal density |
| IXA-002 | `storm_shelter_check.py` | Analysis Script | Shelter add-on areal-density and simple water-equivalent proxy screening | Implemented | Compares local add-on against configured target |
| IXA-003 | `zone_mass_budget.py` | Analysis Script | Zone-level mass-allocation screening | Implemented | Summarizes geometry-aware mass allocation |
| IXA-004 | `test_analysis.py` | Test Package | Repository analysis regression coverage | Implemented | Confirms scripts generate expected outputs |

---

## Section E — Documentation and Repository Support Constituents

| BOM ID | Item Name | Category | Primary Function | Status | Notes |
|---|---|---|---|---|---|
| IXD-001 | Project Charter | Core Doc | Defines scope and maturity | Implemented | `docs/00_Project_Charter.md` |
| IXD-002 | Architecture Overview | Core Doc | Defines system concept | Implemented | `docs/01_Architecture_Overview.md` |
| IXD-003 | Threat Model | Core Doc | Defines radiation environment framing | Implemented | `docs/02_Radiation_Threat_Model_and_Environments.md` |
| IXD-004 | Requirements and Acceptance Criteria | Core Doc | Defines PoC pass/fail logic | Implemented | `docs/03_Requirements_and_Acceptance_Criteria.md` |
| IXD-005 | Science Basis | Core Doc | Records bounded passive-shielding logic | Implemented | `docs/04_Science_Basis_Passive_Shielding.md` |
| IXD-006 | Geometry and Multifunctional Architecture | Core Doc | Defines geometry-driven architecture logic | Implemented | `docs/05_Geometry_and_Multifunctional_Architecture.md` |
| IXD-007 | Contamination Control Subsystem | Core Doc | Preserves habitat realism and bounded interfaces | Implemented | `docs/06_Contamination_Control_Subsystem.md` |
| IXD-008 | Failure Modes and Risks | Core Doc | Records concept-stage risk posture | Implemented | `docs/07_Failure_Modes_and_Risks.md` |
| IXD-009 | Test Matrix | Core Doc | Defines repository verification matrix | Implemented | `docs/08_Test_Matrix.md` |
| IXD-010 | PoC Build Walkthrough | Core Doc | Explains repository assembly logic | Implemented | `docs/09_PoC_Build_Walkthrough.md` |
| IXD-011 | PoC Test Procedures | Core Doc | Defines repeatable repository procedures | Implemented | `docs/10_PoC_Test_Procedures.md` |
| IXD-012 | Data and Results Template | Core Doc | Standardizes result packaging | Implemented | `docs/11_Data_and_Results_Template.md` |
| IXD-013 | Glossary | Support Doc | Stabilizes terminology | Implemented | `docs/12_Glossary.md` |
| IXD-014 | Roadmap | Support Doc | Defines phased build direction | Implemented | `docs/13_Roadmap.md` |
| IXD-015 | Source Traceability Map | Support Doc | Maps claims to source categories | Implemented | `docs/14_Source_Traceability_Map.md` |
| IXD-016 | Cross Section Baseline v1 | Support Doc | Defines baseline conceptual section | Implemented | `docs/15_Cross_Section_Baseline_v1.md` |
| IXD-017 | Storm Shelter Concept | Support Doc | Defines concentrated refuge architecture | Implemented | `docs/16_Storm_Shelter_Concept.md` |
| IXD-018 | Analysis Pipeline Walkthrough | Support Doc | Explains analysis flow | Implemented | `docs/17_Analysis_Pipeline_Walkthrough.md` |
| IXD-019 | Operational Use and Non-Claims | Support Doc | Defines interpretation boundary | Implemented | `docs/18_Operational_Use_and_Nonclaims.md` |
| IXD-020 | References | Support Doc | Lists public-domain grounding sources | Implemented | `docs/19_References.md` |
| IXD-021 | README | Root Doc | Root repository overview | Implemented | `README.md` |
| IXD-022 | Evaluation-Only License | Root Doc | Governs review/use permissions | Implemented | `LICENSE` |
| IXD-023 | Citation Metadata | Root Doc | Supports citation and attribution | Implemented | `CITATION.cff` |
| IXD-024 | Contribution Guidance | Root Doc | Defines contribution boundaries | Implemented | `CONTRIBUTING.md` |
| IXD-025 | Security Guidance | Root Doc | Defines reporting posture | Implemented | `SECURITY.md` |
| IXD-026 | Delta Report | Root Doc | Summarizes current package contents | Implemented | `DELTA_REPORT.md` |

---

## Section F — Concept-Stage BOM Notes

### Note 1 — No Procurement Claim
Nothing in this BOM should be treated as a procurement instruction, vendor selection, or fabrication release.

### Note 2 — No Flight Claim
Nothing in this BOM should be treated as evidence of qualification, certification, or human-rating approval.

### Note 3 — Architecture Value
The value of this BOM is traceability.
It allows a reviewer to see what the concept actually consists of and where those constituents appear in the repository.

## Summary
This BOM is a concept-stage material and repository accounting package for IX-Shield.
It exists to make the concept reviewable, bounded, and difficult to dismiss as hand-waving.
