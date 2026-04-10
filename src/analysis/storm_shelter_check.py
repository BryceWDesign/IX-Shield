#!/usr/bin/env python3
"""
IX-Shield storm-shelter screening analysis.

Purpose:
- Load a shelter add-on configuration.
- Compute local added areal density from shelter layers.
- Estimate concept-stage water-equivalent depth from the added layers.
- Write processed JSON and Markdown outputs.

This script is intentionally bounded to concept-stage screening.
It does not perform radiation transport validation.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List


DEFAULT_CONFIG_PATH = Path("configs/stacks/storm_shelter_addon_10cm_we_v1.json")
DEFAULT_OUTPUT_DIR = Path("results/T-SHLD-020/RUN_SIMULATED_STORM_SHELTER_10CM_V1/processed")


@dataclass
class ShelterLayerResult:
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


def validate_shelter_config(data: Dict[str, Any]) -> None:
    required_top_level = [
        "stack_id",
        "stack_name",
        "analysis_type",
        "based_on_stack_id",
        "units",
        "water_equivalent_target_cm",
        "addon_layers",
    ]
    for key in required_top_level:
        if key not in data:
            raise ValueError(f"Missing required top-level key: {key}")

    if not isinstance(data["addon_layers"], list) or not data["addon_layers"]:
        raise ValueError("Configuration must contain a non-empty 'addon_layers' list.")

    required_layer_fields = [
        "layer_id",
        "layer_name",
        "material",
        "thickness_cm",
        "density_g_cm3",
        "role",
        "notes",
    ]
    for idx, layer in enumerate(data["addon_layers"], start=1):
        for field in required_layer_fields:
            if field not in layer:
                raise ValueError(f"Add-on layer {idx} is missing required field: {field}")


def compute_layer_results(data: Dict[str, Any]) -> List[ShelterLayerResult]:
    results: List[ShelterLayerResult] = []

    for layer in data["addon_layers"]:
        thickness = float(layer["thickness_cm"])
        density = float(layer["density_g_cm3"])
        areal_density = thickness * density

        results.append(
            ShelterLayerResult(
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


def build_stack_summary(
    data: Dict[str, Any], config_path: Path, rows: List[ShelterLayerResult]
) -> Dict[str, Any]:
    total_addon_areal_density = sum(row.areal_density_g_cm2 for row in rows)
    estimated_water_equivalent_cm = total_addon_areal_density / 1.0
    delta_from_target_cm = estimated_water_equivalent_cm - float(
        data["water_equivalent_target_cm"]
    )

    return {
        "run_id": "RUN_SIMULATED_STORM_SHELTER_10CM_V1",
        "analysis_type": "storm_shelter_screen",
        "input_files": {
            "config": str(config_path).replace("\\", "/"),
            "script": "src/analysis/storm_shelter_check.py",
        },
        "stack": {
            "stack_id": data["stack_id"],
            "stack_name": data["stack_name"],
            "based_on_stack_id": data["based_on_stack_id"],
            "addon_layer_count": len(rows),
        },
        "key_outputs": {
            "total_addon_areal_density_g_cm2": round(total_addon_areal_density, 4),
            "estimated_water_equivalent_cm": round(estimated_water_equivalent_cm, 4),
            "target_water_equivalent_cm": round(float(data["water_equivalent_target_cm"]), 4),
            "delta_from_target_cm": round(delta_from_target_cm, 4),
        },
        "notes": data.get("notes", []),
        "limitations": [
            "screening output only",
            "water-equivalent estimate is a simple concept-stage proxy",
            "not transport validated",
            "not operational authorization",
        ],
    }


def build_shelter_check(summary: Dict[str, Any], rows: List[ShelterLayerResult]) -> Dict[str, Any]:
    estimated_we = float(summary["key_outputs"]["estimated_water_equivalent_cm"])
    target_we = float(summary["key_outputs"]["target_water_equivalent_cm"])
    ratio = estimated_we / target_we if target_we > 0 else 0.0

    return {
        "run_id": summary["run_id"],
        "analysis_type": "storm_shelter_check",
        "input_files": summary["input_files"],
        "key_outputs": {
            "estimated_water_equivalent_cm": round(estimated_we, 4),
            "target_water_equivalent_cm": round(target_we, 4),
            "target_achievement_ratio": round(ratio, 4),
            "meets_or_exceeds_target": estimated_we >= target_we,
        },
        "layer_contributions": [
            {
                "layer_id": row.layer_id,
                "layer_name": row.layer_name,
                "areal_density_g_cm2": round(row.areal_density_g_cm2, 4),
            }
            for row in rows
        ],
        "notes": [
            "Target comparison is based on simple concept-stage areal-density-to-water-equivalent proxy logic."
        ],
        "limitations": [
            "screening output only",
            "not a validated event-protection result",
            "not transport validated",
            "not operational authorization",
        ],
    }


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")


def write_markdown_stack_summary(
    path: Path, summary: Dict[str, Any], rows: List[ShelterLayerResult]
) -> None:
    lines: List[str] = [
        "# IX-Shield Storm Shelter Add-On Summary",
        "",
        "## Run Identification",
        "- Run ID: RUN_SIMULATED_STORM_SHELTER_10CM_V1",
        "- Analysis Type: storm_shelter_screen",
        "",
        "## Input Reference",
        f"- Config: {summary['input_files']['config']}",
        f"- Script: {summary['input_files']['script']}",
        "",
        "## Key Screening Values",
        f"- Total add-on areal density: {summary['key_outputs']['total_addon_areal_density_g_cm2']:.4f} g/cm^2",
        f"- Estimated water-equivalent depth: {summary['key_outputs']['estimated_water_equivalent_cm']:.4f} cm",
        f"- Target water-equivalent depth: {summary['key_outputs']['target_water_equivalent_cm']:.4f} cm",
        f"- Delta from target: {summary['key_outputs']['delta_from_target_cm']:.4f} cm",
        "",
        "## Add-On Layer Contributions",
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
            "This run estimates the concept-stage local shielding contribution of the shelter add-on. "
            "The water-equivalent depth used here is a simple screening proxy derived from areal density and "
            "is provided to support architecture comparison, not validated radiation-performance claims.",
            "",
            "## Limits",
            "- Screening output only",
            "- Water-equivalent estimate is a simple concept-stage proxy",
            "- Not transport validated",
            "- Not operational authorization",
            "",
        ]
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_markdown_shelter_check(path: Path, check_payload: Dict[str, Any]) -> None:
    lines: List[str] = [
        "# IX-Shield Storm Shelter Check",
        "",
        "## Run Identification",
        f"- Run ID: {check_payload['run_id']}",
        "- Analysis Type: storm_shelter_check",
        "",
        "## Input Reference",
        f"- Config: {check_payload['input_files']['config']}",
        f"- Script: {check_payload['input_files']['script']}",
        "",
        "## Key Screening Values",
        f"- Estimated water-equivalent depth: {check_payload['key_outputs']['estimated_water_equivalent_cm']:.4f} cm",
        f"- Target water-equivalent depth: {check_payload['key_outputs']['target_water_equivalent_cm']:.4f} cm",
        f"- Target achievement ratio: {check_payload['key_outputs']['target_achievement_ratio']:.4f}",
        f"- Meets or exceeds target: {check_payload['key_outputs']['meets_or_exceeds_target']}",
        "",
        "## Interpretation",
    ]

    if check_payload["key_outputs"]["meets_or_exceeds_target"]:
        lines.append(
            "The configured shelter add-on meets or exceeds the stated concept-stage target using the simple "
            "water-equivalent screening proxy adopted in this repository."
        )
    else:
        lines.append(
            "The configured shelter add-on does not reach the stated concept-stage target using the simple "
            "water-equivalent screening proxy adopted in this repository."
        )

    lines.extend(
        [
            "",
            "## Limits",
            "- Screening output only",
            "- Not a validated event-protection result",
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
        validate_shelter_config(data)
        rows = compute_layer_results(data)

        stack_summary = build_stack_summary(data, config_path, rows)
        shelter_check = build_shelter_check(stack_summary, rows)

        stack_summary_json_path = output_dir / "stack_summary.json"
        shelter_check_json_path = output_dir / "storm_shelter_check.json"
        stack_summary_md_path = output_dir / "summary.md"
        shelter_check_md_path = output_dir / "storm_shelter_check.md"

        write_json(stack_summary_json_path, stack_summary)
        write_json(shelter_check_json_path, shelter_check)
        write_markdown_stack_summary(stack_summary_md_path, stack_summary, rows)
        write_markdown_shelter_check(shelter_check_md_path, shelter_check)

        print("IX-Shield storm-shelter analysis complete.")
        print(f"Wrote: {stack_summary_json_path}")
        print(f"Wrote: {shelter_check_json_path}")
        print(f"Wrote: {stack_summary_md_path}")
        print(f"Wrote: {shelter_check_md_path}")
        return 0

    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
