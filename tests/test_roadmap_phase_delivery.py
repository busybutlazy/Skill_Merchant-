import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from skill_forge.install import list_installed
from skill_forge.repository import load_skill, resolve_skill_install_set


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = REPO_ROOT / "canonical-skills" / "regular-skills" / "deliver-roadmap-phase"
DEPENDENCIES = [
    "plan-change", "triage-pending", "implement-task", "run-approved-change",
    "verify-change", "report-change", "review-change", "close-change",
]


class RoadmapPhaseDeliveryTests(unittest.TestCase):
    def test_facade_contract_is_one_phase_and_preserves_authority_gates(self) -> None:
        instruction = (SKILL_DIR / "instruction.md").read_text(encoding="utf-8")
        for required in (
            "one approved Roadmap Phase", "PHASE_WORKING.md",
            "one Phase Delivery Packet approval gate", "dependency order",
            "independent review", "Human Phase Acceptance",
            "Never commit, push, merge, release, or deploy implicitly",
        ):
            self.assertIn(required, instruction)
        self.assertIn("multiple phases", instruction)
        self.assertIn("Only separately authorized action may update Roadmap completion state", instruction)

    def test_package_declares_complete_atomic_workflow_bundle(self) -> None:
        skill = load_skill(REPO_ROOT, "deliver-roadmap-phase")
        self.assertEqual(skill.version, "1.0.0")
        self.assertEqual(skill.skill_dependencies, DEPENDENCIES)
        resolved = resolve_skill_install_set(
            REPO_ROOT, [skill.name], "codex", allowed_scopes={"public"}
        )
        names = [item.name for item in resolved]
        for dependency in DEPENDENCIES:
            self.assertIn(dependency, names)
        self.assertEqual(names[-1], skill.name)

    def test_catalog_exposes_facade_separately_from_atomic_skills(self) -> None:
        catalog = json.loads((REPO_ROOT / "canonical-skills" / "catalog.json").read_text(encoding="utf-8"))
        roadmap = next(group for group in catalog["groups"] if group["name"] == "Project Lifecycle")
        workflow = next(group for group in catalog["groups"] if group["name"] == "Change Workflow")
        self.assertEqual(
            roadmap["skills"],
            ["what-next", "work-on-change", "work-on-phase", "grill-with-docs", "define-project", "bootstrap-project", "deliver-roadmap-phase", "triage-pending", "close-change"],
        )
        self.assertEqual(workflow["skills"], ["plan-change", "implement-task", "run-approved-change", "verify-change", "report-change", "review-change", "close-change", "triage-pending"])
        self.assertNotIn("deliver-roadmap-phase", catalog["recommended"])

    def test_phase_decision_gates_block_planning_when_due(self) -> None:
        instruction = (SKILL_DIR / "instruction.md").read_text(encoding="utf-8")
        for required in (
            "Read every gate before planning",
            "A due blocker prevents planning",
            "route to `grill-with-docs`",
            "Pending item relevant to the Phase",
            "temporary `changes/<phase-run-id>/PHASE_WORKING.md`",
            "checkpoints",
            "failed or blocked child prevents dependent children",
            "required child must complete verification",
        ):
            self.assertIn(required, instruction)
        packet = (
            SKILL_DIR / "references" / "PHASE_DELIVERY_PACKET_TEMPLATE.md"
        ).read_text(encoding="utf-8")
        self.assertIn("## Decision Gate Checkpoints", packet)
        self.assertIn("| Decision | Required before | Blocks | Owner |", packet)

    def test_cli_installs_bundle_for_both_targets_idempotently(self) -> None:
        for target in ("codex", "claude"):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as tmp_dir:
                command = [
                    sys.executable, "-m", "skill_forge", "--repo-root", str(REPO_ROOT),
                    "install", "deliver-roadmap-phase", "--target", target,
                    "--project", tmp_dir, "--yes",
                ]
                env = dict(os.environ, PYTHONPATH=str(REPO_ROOT / "src"))
                first = subprocess.run(command, cwd=REPO_ROOT, env=env, text=True, capture_output=True)
                second = subprocess.run(command, cwd=REPO_ROOT, env=env, text=True, capture_output=True)
                self.assertEqual(first.returncode, 0, first.stderr)
                self.assertEqual(second.returncode, 0, second.stderr)
                self.assertIn("Installing dependency bundle", first.stderr)
                statuses = {item.name: item.status for item in list_installed(REPO_ROOT, Path(tmp_dir), target)}
                expected = [*DEPENDENCIES, "deliver-roadmap-phase"]
                self.assertEqual({name: statuses[name] for name in expected}, {name: "up_to_date" for name in expected})


if __name__ == "__main__":
    unittest.main()
