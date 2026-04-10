#!/usr/bin/env python3
"""
IX-Shield baseline stack areal-density screening.

Purpose:
- Load a machine-readable stack configuration.
- Compute per-layer and total areal density.
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


DEFAULT_CONFIG_PATH = Path("configs/stacks/baseline_zone_a_v1.json")
DEFAULT_OUTPUT_DIR = Path("results/T-SHLD-010/RUN_SIMULATED_BASELINE_V1/processed")


@dataclass
class LayerResult:
    layer_id: str
    layer_name: str
    material: str
    thickness_cm: float
    density_g_cm3: float
    areal_density_g_cm2: float
    role: str
    notes: str


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_stack_config(data: Dict[str, Any]) -> None:
    required_top_level = ["stack_id", "stack_name", "analysis_type", "units", "layers"]
    for key in required_top_level:
        if key not in data:
            raise ValueError(f"Missing required top-level key: {key}")

    if not isinstance(data["layers"], list) or not data["layers"]:
        raise ValueError("Configuration must contain a non-empty 'layers' list.")

    required_layer_fields = [
        "layer_id",
        "layer_name",
        "material",
        "thickness_cm",
        "density_g_cm3",
        "role",
        "notes",
    ]
    for idx, layer in enumerate(data["layers"], start=1):
        for field in required_layer_fields:
            if field not in layer:
                raise ValueError(f"Layer {idx} is missing required field: {field}")


def compute_layer_results(data: Dict[str, Any]) -> List[LayerResult]:
    results: List[LayerResult] = []

    for layer in data["layers"]:
        thickness = float(layer["thickness_cm"])
        density = float(layer["density_g_cm3"])
        areal_density = thickness * density

        results.append(
            LayerResult(
                layer_id=str(layer["layer_id"]),
                layer_name=str(layer["layer_name"]),
                material=str(layer["material"]),
                thickness_cm=thickness,
                density_g_cm3=density,
                areal_density_g_cm2=areal_density,
                role=str(layer["role"]),
                notes=str(layer["notes"]),
            )
        )

    return results


def write_csv(path: Path, rows: List[LayerResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "layer_id",
                "layer_name",
                "material",
                "thickness_cm",
                "density_g_cm3",
                "areal_density_g_cm2",
                "role",
                "notes",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row.layer_id,
                    row.layer_name,
                    row.material,
                    f"{row.thickness_cm:.2f}",
                    f"{row.density_g_cm3:.4f}",
                    f"{row.areal_density_g_cm2:.4f}",
                    row.role,
                    row.notes,
                ]
            )


def build_summary_payload(
    data: Dict[str, Any], config_path: Path, rows: List[LayerResult]
) -> Dict[str, Any]:
    total_areal_density = sum(row.areal_density_g_cm2 for row in rows)
    thickest_layer = max(rows, key=lambda r: r.thickness_cm)
    dominant_areal_density_layer = max(rows, key=lambda r: r.areal_density_g_cm2)

    return {
        "run_id": "RUN_SIMULATED_BASELINE_V1",
        "analysis_type": "baseline_areal_density_screen",
        "input_files": {
            "config": str(config_path).replace("\\", "/"),
            "script": "src/analysis/stack_areal_density.py",
        },
        "stack": {
            "stack_id": data["stack_id"],
            "stack_name": data["stack_name"],
            "layer_count": len(rows),
        },
        "key_outputs": {
            "total_areal_density_g_cm2": round(total_areal_density, 4),
            "thickest_layer_name": thickest_layer.layer_name,
            "thickest_layer_thickness_cm": round(thickest_layer.thickness_cm, 4),
            "dominant_areal_density_layer_name": dominant_areal_density_layer.layer_name,
            "dominant_areal_density_layer_g_cm2": round(
                dominant_areal_density_layer.areal_density_g_cm2, 4
            ),
        },
        "notes": data.get("notes", []),
        "limitations": [
            "screening output only",
            "not transport validated",
            "not operational authorization",
        ],
    }


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")


def write_markdown(
    path: Path, payload: Dict[str, Any], rows: List[LayerResult]
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    total = payload["key_outputs"]["total_areal_density_g_cm2"]

    lines: List[str] = [
        "# IX-Shield Baseline Stack Summary",
        "",
        "## Run Identification",
        "- Run ID: RUN_SIMULATED_BASELINE_V1",
        "- Analysis Type: baseline_areal_density_screen",
        "",
        "## Input Reference",
        f"- Config: {payload['input_files']['config']}",
        f"- Script: {payload['input_files']['script']}",
        "",
        "## Key Screening Values",
        f"- Total areal density: {total:.4f} g/cm^2",
        f"- Layer count: {payload['stack']['layer_count']}",
        f"- Thickest layer: {payload['key_outputs']['thickest_layer_name']} "
        f"({payload['key_outputs']['thickest_layer_thickness_cm']:.2f} cm)",
        f"- Dominant areal-density layer: {payload['key_outputs']['dominant_areal_density_layer_name']} "
        f"({payload['key_outputs']['dominant_areal_density_layer_g_cm2']:.4f} g/cm^2)",
        "",
        "## Layer Contributions",
    ]

    for row in rows:
        lines.append(
            f"- {row.layer_id} — {row.layer_name}: "
            f"{row.areal_density_g_cm2:.4f} g/cm^2 "
            f"({row.thickness_cm:.2f} cm × {row.density_g_cm3:.4f} g/cm^3)"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "This run provides a concept-stage areal-density summary for the IX-Shield baseline stack. "
            "It is useful for comparing stack composition and mass-per-area logic, but it is not a "
            "radiation transport result and should not be interpreted as a validated crew-protection outcome.",
            "",
            "## Limits",
            "- Screening output only",
            "- Not transport validated",
            "- Not operational authorization",
            "",
        ]
    )

    with path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> int:
    config_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CONFIG_PATH
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT_DIR

    try:
        data = load_json(config_path)
        validate_stack_config(data)
        rows = compute_layer_results(data)

        csv_path = output_dir / "stack_layer_details.csv"
        json_path = output_dir / "stack_summary.json"
        md_path = output_dir / "summary.md"

        write_csv(csv_path, rows)
        summary_payload = build_summary_payload(data, config_path, rows)
        write_json(json_path, summary_payload)
        write_markdown(md_path, summary_payload, rows)

        print("IX-Shield baseline analysis complete.")
        print(f"Wrote: {csv_path}")
        print(f"Wrote: {json_path}")
        print(f"Wrote: {md_path}")
        return 0

    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
