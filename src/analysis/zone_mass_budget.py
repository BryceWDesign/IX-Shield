#!/usr/bin/env python3
"""
IX-Shield zone mass-budget screening analysis.

Purpose:
- Load a machine-readable zone reference configuration.
- Compute zone-level mass totals and fractions.
- Write processed CSV, JSON, and Markdown outputs.

This script is intentionally bounded to concept-stage screening.
It does not perform radiation transport validation.
"""

from __future__ import annotations

import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List


DEFAULT_CONFIG_PATH = Path("configs/zones/reference_vehicle_zones_v1.json")
DEFAULT_OUTPUT_DIR = Path("results/T-SHLD-030/RUN_SIMULATED_ZONE_MASS_BUDGET_V1/processed")


@dataclass
class ZoneResult:
    zone_id: str
    zone_name: str
    allocated_mass_kg: float
    role: str
    notes: str
    mass_fraction: float


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_zone_config(data: Dict[str, Any]) -> None:
    required_top_level = ["zone_set_id", "zone_set_name", "analysis_type", "units", "zones"]
    for key in required_top_level:
        if key not in data:
            raise ValueError(f"Missing required top-level key: {key}")

    if not isinstance(data["zones"], list) or not data["zones"]:
        raise ValueError("Configuration must contain a non-empty 'zones' list.")

    required_zone_fields = [
        "zone_id",
        "zone_name",
        "allocated_mass_kg",
        "role",
        "notes",
    ]
    for idx, zone in enumerate(data["zones"], start=1):
        for field in required_zone_fields:
            if field not in zone:
                raise ValueError(f"Zone {idx} is missing required field: {field}")


def compute_zone_results(data: Dict[str, Any]) -> List[ZoneResult]:
    total_mass = sum(float(zone["allocated_mass_kg"]) for zone in data["zones"])
    if total_mass <= 0:
        raise ValueError("Total configured mass must be greater than zero.")

    results: List[ZoneResult] = []
    for zone in data["zones"]:
        mass = float(zone["allocated_mass_kg"])
        fraction = mass / total_mass
        results.append(
            ZoneResult(
                zone_id=str(zone["zone_id"]),
                zone_name=str(zone["zone_name"]),
                allocated_mass_kg=mass,
                role=str(zone["role"]),
                notes=str(zone["notes"]),
                mass_fraction=fraction,
            )
        )

    return results


def write_csv(path: Path, rows: List[ZoneResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "zone_id",
                "zone_name",
                "allocated_mass_kg",
                "mass_fraction",
                "role",
                "notes",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row.zone_id,
                    row.zone_name,
                    f"{row.allocated_mass_kg:.2f}",
                    f"{row.mass_fraction:.6f}",
                    row.role,
                    row.notes,
                ]
            )


def build_summary_payload(
    data: Dict[str, Any], config_path: Path, rows: List[ZoneResult]
) -> Dict[str, Any]:
    total_mass = sum(row.allocated_mass_kg for row in rows)
    largest_zone = max(rows, key=lambda r: r.allocated_mass_kg)
    smallest_zone = min(rows, key=lambda r: r.allocated_mass_kg)

    return {
        "run_id": "RUN_SIMULATED_ZONE_MASS_BUDGET_V1",
        "analysis_type": "zone_mass_budget",
        "input_files": {
            "config": str(config_path).replace("\\", "/"),
            "script": "src/analysis/zone_mass_budget.py",
        },
        "zone_set": {
            "zone_set_id": data["zone_set_id"],
            "zone_set_name": data["zone_set_name"],
            "zone_count": len(rows),
        },
        "key_outputs": {
            "total_allocated_mass_kg": round(total_mass, 4),
            "largest_zone_name": largest_zone.zone_name,
            "largest_zone_mass_kg": round(largest_zone.allocated_mass_kg, 4),
            "largest_zone_fraction": round(largest_zone.mass_fraction, 6),
            "smallest_zone_name": smallest_zone.zone_name,
            "smallest_zone_mass_kg": round(smallest_zone.allocated_mass_kg, 4),
            "smallest_zone_fraction": round(smallest_zone.mass_fraction, 6),
        },
        "notes": data.get("notes", []),
        "limitations": [
            "screening output only",
            "mass allocation is a concept-stage proxy for geometry-aware protection reasoning",
            "not transport validated",
            "not operational authorization",
        ],
    }


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")


def write_markdown(path: Path, payload: Dict[str, Any], rows: List[ZoneResult]) -> None:
    lines: List[str] = [
        "# IX-Shield Zone Mass Budget Summary",
        "",
        "## Run Identification",
        "- Run ID: RUN_SIMULATED_ZONE_MASS_BUDGET_V1",
        "- Analysis Type: zone_mass_budget",
        "",
        "## Input Reference",
        f"- Config: {payload['input_files']['config']}",
        f"- Script: {payload['input_files']['script']}",
        "",
        "## Key Screening Values",
        f"- Total allocated mass: {payload['key_outputs']['total_allocated_mass_kg']:.2f} kg",
        f"- Zone count: {payload['zone_set']['zone_count']}",
        f"- Largest zone: {payload['key_outputs']['largest_zone_name']} "
        f"({payload['key_outputs']['largest_zone_mass_kg']:.2f} kg, "
        f"{payload['key_outputs']['largest_zone_fraction']:.6f} fraction)",
        f"- Smallest zone: {payload['key_outputs']['smallest_zone_name']} "
        f"({payload['key_outputs']['smallest_zone_mass_kg']:.2f} kg, "
        f"{payload['key_outputs']['smallest_zone_fraction']:.6f} fraction)",
        "",
        "## Zone Allocation Details",
    ]

    for row in rows:
        lines.append(
            f"- {row.zone_id} — {row.zone_name}: {row.allocated_mass_kg:.2f} kg "
            f"({row.mass_fraction:.6f} fraction) — {row.role}"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "This run summarizes concept-stage mass allocation across reference protection zones. "
            "It is useful for reasoning about which regions receive the most local mass support, "
            "but it does not by itself predict radiation performance or crew dose.",
            "",
            "## Limits",
            "- Screening output only",
            "- Mass allocation is a concept-stage proxy for geometry-aware protection reasoning",
            "- Not transport validated",
            "- Not operational authorization",
            "",
        ]
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> int:
    config_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CONFIG_PATH
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT_DIR

    try:
        data = load_json(config_path)
        validate_zone_config(data)
        rows = compute_zone_results(data)

        csv_path = output_dir / "zone_mass_budget.csv"
        json_path = output_dir / "zone_mass_budget_summary.json"
        md_path = output_dir / "zone_mass_budget.md"

        write_csv(csv_path, rows)
        summary_payload = build_summary_payload(data, config_path, rows)
        write_json(json_path, summary_payload)
        write_markdown(md_path, summary_payload, rows)

        print("IX-Shield zone mass-budget analysis complete.")
        print(f"Wrote: {csv_path}")
        print(f"Wrote: {json_path}")
        print(f"Wrote: {md_path}")
        return 0

    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
