from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]


def run_script(script_rel_path: str, config_rel_path: str, output_dir: Path) -> subprocess.CompletedProcess[str]:
    script_path = REPO_ROOT / script_rel_path
    config_path = REPO_ROOT / config_rel_path

    return subprocess.run(
        [sys.executable, str(script_path), str(config_path), str(output_dir)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


@pytest.mark.parametrize(
    ("script_rel_path", "config_rel_path", "expected_files"),
    [
        (
            "src/analysis/stack_areal_density.py",
            "configs/stacks/baseline_zone_a_v1.json",
            [
                "stack_layer_details.csv",
                "stack_summary.json",
                "summary.md",
            ],
        ),
        (
            "src/analysis/storm_shelter_check.py",
            "configs/stacks/storm_shelter_addon_10cm_we_v1.json",
            [
                "stack_summary.json",
                "storm_shelter_check.json",
                "summary.md",
                "storm_shelter_check.md",
            ],
        ),
        (
            "src/analysis/zone_mass_budget.py",
            "configs/zones/reference_vehicle_zones_v1.json",
            [
                "zone_mass_budget.csv",
                "zone_mass_budget_summary.json",
                "zone_mass_budget.md",
            ],
        ),
    ],
)
def test_analysis_scripts_generate_expected_outputs(
    script_rel_path: str,
    config_rel_path: str,
    expected_files: list[str],
    tmp_path: Path,
) -> None:
    output_dir = tmp_path / "processed"

    result = run_script(script_rel_path, config_rel_path, output_dir)

    assert result.returncode == 0, (
        f"Script failed.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )

    for filename in expected_files:
        output_file = output_dir / filename
        assert output_file.exists(), f"Missing expected output file: {output_file}"


def test_baseline_summary_contains_expected_keys(tmp_path: Path) -> None:
    output_dir = tmp_path / "baseline"

    result = run_script(
        "src/analysis/stack_areal_density.py",
        "configs/stacks/baseline_zone_a_v1.json",
        output_dir,
    )

    assert result.returncode == 0, (
        f"Baseline script failed.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )

    summary = load_json(output_dir / "stack_summary.json")

    assert summary["run_id"] == "RUN_SIMULATED_BASELINE_V1"
    assert summary["analysis_type"] == "baseline_areal_density_screen"
    assert "key_outputs" in summary
    assert summary["key_outputs"]["total_areal_density_g_cm2"] > 0
    assert summary["stack"]["layer_count"] == 5


def test_shelter_check_reports_target_status(tmp_path: Path) -> None:
    output_dir = tmp_path / "shelter"

    result = run_script(
        "src/analysis/storm_shelter_check.py",
        "configs/stacks/storm_shelter_addon_10cm_we_v1.json",
        output_dir,
    )

    assert result.returncode == 0, (
        f"Shelter script failed.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )

    check_payload = load_json(output_dir / "storm_shelter_check.json")

    assert check_payload["run_id"] == "RUN_SIMULATED_STORM_SHELTER_10CM_V1"
    assert check_payload["analysis_type"] == "storm_shelter_check"
    assert check_payload["key_outputs"]["estimated_water_equivalent_cm"] > 0
    assert "meets_or_exceeds_target" in check_payload["key_outputs"]


def test_zone_mass_budget_totals_are_consistent(tmp_path: Path) -> None:
    output_dir = tmp_path / "zones"

    result = run_script(
        "src/analysis/zone_mass_budget.py",
        "configs/zones/reference_vehicle_zones_v1.json",
        output_dir,
    )

    assert result.returncode == 0, (
        f"Zone mass-budget script failed.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )

    summary = load_json(output_dir / "zone_mass_budget_summary.json")

    assert summary["run_id"] == "RUN_SIMULATED_ZONE_MASS_BUDGET_V1"
    assert summary["analysis_type"] == "zone_mass_budget"
    assert summary["zone_set"]["zone_count"] == 5
    assert summary["key_outputs"]["total_allocated_mass_kg"] > 0
    assert summary["key_outputs"]["largest_zone_mass_kg"] >= summary["key_outputs"]["smallest_zone_mass_kg"]


def test_scripts_fail_cleanly_on_missing_config(tmp_path: Path) -> None:
    missing_config = tmp_path / "missing.json"
    output_dir = tmp_path / "missing_out"

    result = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "src/analysis/stack_areal_density.py"),
            str(missing_config),
            str(output_dir),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "Configuration file not found" in result.stderr
