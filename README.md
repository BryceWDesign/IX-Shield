# IX-Shield

**Documentation-first engineering proof of concept for a multifunctional crew-protection architecture focused on deep-space radiation risk reduction, geometry-aware mass placement, and concentrated storm-shelter logic.**

## Status
IX-Shield is a **concept-stage** repository.

It is:
- a proof-of-concept architecture package;
- a reviewable repository for bounded screening logic;
- a documentation-first engineering build.

It is **not**:
- flight qualified;
- crew rated;
- transport validated;
- operationally approved;
- a complete solution to deep-space radiation.

## Why This Repo Exists
IX-Shield exists to package a technically serious crew-protection concept in a form that can be reviewed without hype.

The repository is built around a simple idea:

**crew protection is not just a wall-thickness problem.**  
It is a combined problem involving:
- shielding mass choice;
- crew location;
- surrounding mission mass;
- local refuge design;
- emergency shelter concentration;
- disciplined non-claims.

## Core Architecture Logic
IX-Shield is organized around three linked concepts:

### 1. Baseline Transit Shell
A low-Z / hydrogen-rich-biased conceptual shell intended for concept-stage passive-shielding screening.

### 2. Storm Shelter
A concentrated refuge enhancement intended to improve local protection during elevated event conditions through additional water-equivalent and hydrogen-rich mass near crew.

### 3. Geometry-Aware Protection
A zone-based view of the habitat that treats crew-core placement and surrounding mass distribution as part of the protection architecture.

## What Is In This Repository

### Documentation
The `docs/` directory contains:
- project charter;
- architecture overview;
- threat model;
- requirements and acceptance criteria;
- science basis;
- geometry, contamination, risk, and operational boundary documents;
- test matrix and procedure documents;
- traceability and references.

### Configurations
The `configs/` directory contains:
- baseline stack configuration;
- storm-shelter add-on configurations;
- reference vehicle zone configuration.

### Analysis
The `src/analysis/` directory contains:
- baseline areal-density screening;
- storm-shelter screening;
- zone mass-budget screening.

### Tests
The `tests/` directory contains regression coverage for the analysis scripts.

### Processed Results
The `results/` directory stores processed outputs for manual review.

### BOM
The `BOM/` directory contains the concept-stage bill of materials.

## Current Proof-of-Concept Output Snapshot
The current stored proof-of-concept outputs include:

- **Baseline stack total areal density:** 20.7000 g/cm^2  
- **Practical shelter add-on screening depth:** 10.1160 cm water-equivalent proxy  
- **Reference zone mass allocation total:** 7450.00 kg across five zones

These are repository screening values only.
They are not validated crew-protection performance values.

## Recommended Review Order
For a clean first review, read the repo in this order:

1. `docs/00_Project_Charter.md`
2. `docs/01_Architecture_Overview.md`
3. `docs/02_Radiation_Threat_Model_and_Environments.md`
4. `docs/03_Requirements_and_Acceptance_Criteria.md`
5. `docs/16_Storm_Shelter_Concept.md`
6. `docs/17_Analysis_Pipeline_Walkthrough.md`
7. `results/`

## Repository Layout

```text
IX-Shield/
├─ BOM/
├─ configs/
│  ├─ stacks/
│  └─ zones/
├─ docs/
├─ results/
├─ src/
│  └─ analysis/
├─ tests/
├─ LICENSE
├─ CITATION.cff
├─ CONTRIBUTING.md
├─ SECURITY.md
├─ DELTA_REPORT.md
└─ README.md

What This Repo Is Good For

IX-Shield is most useful for:

concept review;
architecture critique;
early trade-study framing;
proof-of-concept shielding logic discussion;
geometry-aware crew-protection discussion;
portfolio or research-positioning review.
What This Repo Is Not Good For

IX-Shield should not be used as:

a direct implementation package;
a flight design release;
a safety certification artifact;
a transport-validation substitute;
an operational decision package.
License

This repository is distributed under an evaluation-only license.

You may inspect, review, and perform bounded non-operational evaluation under the license terms.

You may not use the repository for unrestricted real-world implementation, deployment, commercialization, or operational integration without prior written permission from the repository owner.

See:

LICENSE
Citation

If you reference the repository in technical discussion or evaluation work, use:

CITATION.cff
Author

Bryce Lovell

Final Note

IX-Shield is meant to be taken seriously because it is bounded, reviewable, and honest about what it does not prove.
It is a disciplined architecture package, not a miracle-shield claim.
