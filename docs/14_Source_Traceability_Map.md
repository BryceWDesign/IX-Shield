# IX-Shield Source Traceability Map

## Purpose
This document maps the main technical positions in IX-Shield to broad public-domain source categories and supporting repository files.

The goal is traceability, not false precision.
This map does not claim that every repository sentence is a direct quotation from one source.
It shows the evidence lanes that support the architecture’s main positions.

## Traceability Method
Each claim family below is mapped to:
- the repository files that use the claim;
- the reference IDs listed in `docs/19_References.md`;
- the way the source is used.

---

## TM-001 — Mixed Deep-Space Radiation Must Be Split Into SPE, GCR, and Secondary-Radiation Logic

### Repository Files
- `docs/01_Architecture_Overview.md`
- `docs/02_Radiation_Threat_Model_and_Environments.md`
- `docs/03_Requirements_and_Acceptance_Criteria.md`
- `docs/18_Operational_Use_and_Nonclaims.md`

### Reference IDs
- REF-001
- REF-002
- REF-003

### Evidence Use
Used to justify separating event-driven shelter logic from chronic exposure logic and to justify conservative non-claims about passive shielding.

---

## TM-002 — Hydrogen-Rich / Low-Z Mass Is The Baseline Passive-Shielding Instinct For Crew-Centric Architecture

### Repository Files
- `docs/01_Architecture_Overview.md`
- `docs/03_Requirements_and_Acceptance_Criteria.md`
- `docs/04_Science_Basis_Passive_Shielding.md`
- `docs/16_Storm_Shelter_Concept.md`
- `configs/stacks/baseline_zone_a_v1.json`

### Reference IDs
- REF-001
- REF-004
- REF-005
- REF-006

### Evidence Use
Used to justify a baseline concept centered on hydrogen-rich passive mass rather than dense blanket crew-wall instincts.

---

## TM-003 — Concentrated Storm Shelters Are More Practical Than Uniformly Thickening The Entire Vehicle

### Repository Files
- `docs/01_Architecture_Overview.md`
- `docs/04_Science_Basis_Passive_Shielding.md`
- `docs/16_Storm_Shelter_Concept.md`
- `configs/stacks/storm_shelter_addon_10cm_we_v1.json`
- `configs/stacks/storm_shelter_addon_20cm_we_aspirational.json`

### Reference IDs
- REF-001
- REF-007
- REF-008

### Evidence Use
Used to justify the local refuge strategy, water-equivalent framing, and the distinction between baseline shell and shelter enhancement.

---

## TM-004 — Geometry And Mass Placement Matter, Not Just Nominal Wall Thickness

### Repository Files
- `docs/01_Architecture_Overview.md`
- `docs/05_Geometry_and_Multifunctional_Architecture.md`
- `docs/16_Storm_Shelter_Concept.md`
- `configs/zones/reference_vehicle_zones_v1.json`
- `src/analysis/zone_mass_budget.py`

### Reference IDs
- REF-001
- REF-002
- REF-007
- REF-008

### Evidence Use
Used to justify crew-core logic, surrounded-architecture thinking, zone mass-budget screening, and refuge placement reasoning.

---

## TM-005 — Secondary Radiation And Diminishing Returns Are Reasons To Avoid Blanket Dense High-Z Crew Walls

### Repository Files
- `docs/01_Architecture_Overview.md`
- `docs/04_Science_Basis_Passive_Shielding.md`
- `docs/07_Failure_Modes_and_Risks.md`

### Reference IDs
- REF-001
- REF-003
- REF-009
- REF-010

### Evidence Use
Used to support conservative treatment of dense metallic blanket layers and to preserve a bounded low-Z-biased architecture.

---

## TM-006 — Shelter And Shielding Should Be Multifunctional Where Possible

### Repository Files
- `docs/05_Geometry_and_Multifunctional_Architecture.md`
- `docs/09_PoC_Build_Walkthrough.md`
- `docs/16_Storm_Shelter_Concept.md`
- `BOM/IX_Shield_Full_BillOfMaterials.md`

### Reference IDs
- REF-005
- REF-007
- REF-011

### Evidence Use
Used to justify integrating water, logistics, polymers, intermediate regions, and habitat mass into protection logic instead of relying on pure dead-mass additions.

---

## TM-007 — Stuffed / Layered Intermediate Protection Concepts Have More Serious Potential Than Decorative Surface Coatings

### Repository Files
- `docs/05_Geometry_and_Multifunctional_Architecture.md`
- `docs/06_Contamination_Control_Subsystem.md`
- `docs/15_Cross_Section_Baseline_v1.md`
- `BOM/IX_Shield_Full_BillOfMaterials.md`

### Reference IDs
- REF-011
- REF-012
- REF-013

### Evidence Use
Used to justify a bounded stand-off/protective intermediate region and to reject loose particulate or decorative coating instincts as the main crew-radiation answer.

---

## TM-008 — Concept Screening Must Be Distinguished From Transport Validation

### Repository Files
- `docs/03_Requirements_and_Acceptance_Criteria.md`
- `docs/04_Science_Basis_Passive_Shielding.md`
- `docs/08_Test_Matrix.md`
- `docs/10_PoC_Test_Procedures.md`
- `docs/17_Analysis_Pipeline_Walkthrough.md`
- `docs/18_Operational_Use_and_Nonclaims.md`

### Reference IDs
- REF-003
- REF-014

### Evidence Use
Used to justify the repository’s modest analysis pipeline, strong non-claims posture, and repeated screening-versus-validation boundary.

---

## TM-009 — Active Shielding Is A Future Research Lane, Not The Present Baseline Of This Repository

### Repository Files
- `docs/13_Roadmap.md`
- `docs/18_Operational_Use_and_Nonclaims.md`
- `DELTA_REPORT.md`

### Reference IDs
- REF-003
- REF-015

### Evidence Use
Used to keep active magnetic or electrostatic shielding outside the claimed baseline while acknowledging it as a future R&D branch.

---

## TM-010 — Surface Safe-Haven Escalation Using Local Mass Is A Stronger Long-Duration Surface Path Than Endless Launched Hull Thickening

### Repository Files
- `docs/02_Radiation_Threat_Model_and_Environments.md`
- `docs/13_Roadmap.md`
- `DELTA_REPORT.md`

### Reference IDs
- REF-002
- REF-016

### Evidence Use
Used to acknowledge that long-duration surface protection may benefit more from local mass and safe-haven logic than further transit-shell thickening.

---

## Summary
This traceability map shows that IX-Shield is not presented as unsupported intuition.
It is presented as a bounded architecture package assembled from recognizable public-domain engineering lanes.
