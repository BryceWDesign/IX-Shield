# IX-Shield Radiation Threat Model and Environments

## Purpose
This document defines the radiation environment assumptions used by IX-Shield at the concept-screening stage.

The purpose is not to replace detailed mission-specific transport analysis.
The purpose is to establish a disciplined basis for architecture decisions, shelter logic, and proof-of-concept screening.

## Threat Model Scope
IX-Shield is concerned with crew exposure outside low Earth orbit in environments where geomagnetic protection is limited or absent.

The concept-stage threat model is built around three major categories:

1. solar particle events;
2. galactic cosmic rays;
3. secondary radiation produced when primary radiation interacts with vehicle materials and internal mass.

## Why The Threat Model Is Split
Not all radiation threats behave the same way.
A useful architecture must separate the major threat families instead of treating all exposure as one generic problem.

This matters because:
- event timing differs;
- particle energy distributions differ;
- shielding response differs;
- operational response differs;
- mass-efficient protection strategies differ.

## Threat Category 1 — Solar Particle Events

### Description
Solar particle events are intermittent radiation events driven by solar activity.
They can produce rapid increases in particle flux and create acute exposure concerns over relatively short time windows.

### Why They Matter
SPEs matter because:
- they can create dangerous dose accumulation quickly;
- they demand timely operational response;
- they are one of the strongest reasons to include a shelter-centered protection mode.

### IX-Shield Design Consequences
For IX-Shield, SPE logic supports:
- a concentrated refuge volume;
- additional water-equivalent mass near crew;
- reconfigurable shielding mass;
- operational shelter procedures;
- architecture choices that allow local protection to exceed baseline transit protection.

### Design Interpretation
At the concept stage, IX-Shield treats SPE protection as the most practical driver for concentrated shelter design.

## Threat Category 2 — Galactic Cosmic Rays

### Description
Galactic cosmic rays are persistent high-energy particles present in deep-space environments.
They represent a chronic background hazard rather than a short, isolated burst.

### Why They Matter
GCR matters because:
- crews may experience long-duration cumulative exposure;
- the environment is persistent during transit;
- passive shielding does not fully solve the problem;
- some shielding strategies produce diminishing returns.

### IX-Shield Design Consequences
For IX-Shield, GCR logic supports:
- use of hydrogen-rich mass where reasonable;
- geometry-aware placement of crew and mission mass;
- avoidance of simplistic dense-metal blanket instincts;
- conservative non-claims regarding total protection.

### Design Interpretation
At the concept stage, IX-Shield treats GCR as the limiting reason not to oversell passive shielding.

## Threat Category 3 — Secondary Radiation

### Description
Secondary radiation arises when incident radiation interacts with shielding materials, vehicle structure, habitat contents, or human tissue.

### Why It Matters
Secondary radiation matters because:
- shielding is not a purely subtractive problem;
- the wrong material instincts can create misleading confidence;
- material choice and layer order can change downstream effects.

### IX-Shield Design Consequences
For IX-Shield, secondary-radiation logic supports:
- caution around blanket dense high-Z concepts near crew;
- interest in low-Z and hydrogen-rich primary shielding roles;
- interest in tuned interlayers rather than arbitrary material stacking;
- disciplined separation between concept screening and validated transport claims.

## Environment Classes Used In IX-Shield
IX-Shield uses simplified environment classes for concept-stage framing.

### Environment Class A — Deep-Space Transit
Characteristics:
- persistent GCR background;
- possibility of major SPE exposure;
- crew inside a vehicle or habitat with finite launched shielding mass.

Architecture relevance:
- baseline transit shell matters;
- crew-core geometry matters;
- shelter mode is required.

### Environment Class B — Temporary Shelter Response
Characteristics:
- crew response to an elevated event condition;
- focus on concentrated protection over short duration.

Architecture relevance:
- storm shelter becomes the dominant protection feature;
- local water-equivalent logic becomes more important than full-volume uniformity.

### Environment Class C — Surface Safe-Haven Escalation
Characteristics:
- mission phase where local environmental mass may become available;
- long-duration occupancy concerns;
- potential use of local mass beyond launched shell mass.

Architecture relevance:
- IX-Shield concept may interface with safe-haven or covered-habitat logic;
- concept screening in this repository does not fully model this class, but acknowledges its importance.

## Exposure Logic In This Repository
At this phase, IX-Shield does not calculate full crew dose.
Instead, it uses concept-screening proxies such as:
- areal density;
- water-equivalent approximations;
- local mass concentration around crew zones;
- relative stack comparisons.

These proxies are useful for early architecture work but do not replace detailed transport evaluation.

## Threat Prioritization
For IX-Shield, the practical threat prioritization is:

1. preserve credible chronic protection logic for transit exposure;
2. improve concentrated shelter response for major event conditions;
3. avoid material choices that create unjustified confidence;
4. preserve mass efficiency and architectural realism.

## Architecture Implications Of The Threat Model
The threat model leads directly to the following IX-Shield choices:

- a hydrogen-rich-biased primary protection concept;
- a shelter-centered enhancement concept;
- geometry-aware crew-core logic;
- rejection of “one-layer solves everything” thinking;
- explicit non-claims regarding total protection.

## Screening Boundaries
This repository does not claim to answer:
- mission-certified crew dose;
- biological risk acceptance;
- transport-validated spectrum behavior;
- operational radiation safety approval.

This repository does claim to provide:
- a coherent environment split;
- architecture consequences tied to that split;
- disciplined concept-stage screening inputs.

## Reviewer Guidance
A reviewer should read IX-Shield’s threat model as:
- a concept-stage environment framework;
- a design driver for the architecture;
- a justification for shelter-centered mass concentration.

A reviewer should not read it as:
- a complete radiation textbook;
- a final mission analysis;
- a substitute for transport simulation or certification work.

## Summary
IX-Shield is built on the understanding that deep-space crew protection is a mixed-environment problem.

SPE drives concentrated emergency protection.  
GCR drives caution, geometry, and non-claims.  
Secondary radiation drives disciplined material choices.

That split is the foundation of the architecture.
