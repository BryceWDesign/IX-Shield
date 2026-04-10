# IX-Shield Zone Mass Budget Summary

## Run Identification
- Run ID: RUN_SIMULATED_ZONE_MASS_BUDGET_V1
- Analysis Type: zone_mass_budget

## Input Reference
- Config: configs/zones/reference_vehicle_zones_v1.json
- Script: src/analysis/zone_mass_budget.py

## Key Screening Values
- Total allocated mass: 7450.00 kg
- Zone count: 5
- Largest zone: Logistics Ring (2200.00 kg, 0.295302 fraction)
- Smallest zone: Storm Shelter Envelope (950.00 kg, 0.127517 fraction)

## Zone Allocation Details
- Z1 — Crew Core: 1800.00 kg (0.241611 fraction) — Most occupied central habitat region
- Z2 — Storm Shelter Envelope: 950.00 kg (0.127517 fraction) — Localized refuge enhancement region
- Z3 — Logistics Ring: 2200.00 kg (0.295302 fraction) — Surrounding consumables and supplies region
- Z4 — Equipment Bay: 1400.00 kg (0.187919 fraction) — Systems and equipment-adjacent region
- Z5 — Peripheral Hull Region: 1100.00 kg (0.147651 fraction) — Outer shell and peripheral structure region

## Interpretation
This run summarizes concept-stage mass allocation across reference protection zones. It is useful for reasoning about which regions receive the most local mass support, but it does not by itself predict radiation performance or crew dose.

## Limits
- Screening output only
- Mass allocation is a concept-stage proxy for geometry-aware protection reasoning
- Not transport validated
- Not operational authorization
