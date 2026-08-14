import json
import tempfile
import unittest
from pathlib import Path

from skill_forge.install import install_skill, list_installed
from skill_forge.repository import load_skill, resolve_skill_install_set


REPO_ROOT = Path(__file__).resolve().parents[1]


class WorkflowEntrypointTests(unittest.TestCase):
    def test_human_entrypoints_are_public_and_preserve_review_boundary(self) -> None:
        for name in ("what-next", "work-on-change", "work-on-phase"):
            with self.subTest(name=name):
                self.assertEqual(load_skill(REPO_ROOT, name).scope, "public")

        change = load_skill(REPO_ROOT, "work-on-change")
        self.assertIn("review-change", change.skill_dependencies)
        self.assertIn("fresh `review-change` session", change.instruction)
        self.assertIn("does not weaken", change.instruction)
        self.assertIn("Execute one atomic workflow by default", change.instruction)
        self.assertIn("Risk-Adaptive Ceremony", change.instruction)

        navigator = load_skill(REPO_ROOT, "what-next")
        self.assertIn("Pending item whose recorded trigger is due", navigator.instruction)
        self.assertIn("close-change", navigator.instruction)
        self.assertIn("current verification and a concise Review Handoff", navigator.instruction)

    def test_what_next_resolves_complete_development_workflow(self) -> None:
        resolved = resolve_skill_install_set(
            REPO_ROOT, ["what-next"], "codex", allowed_scopes={"public"}
        )
        names = [skill.name for skill in resolved]
        for required in (
            "grill-with-docs",
            "define-project",
            "bootstrap-project",
            "plan-change",
            "implement-task",
            "run-approved-change",
            "verify-change",
            "report-change",
            "review-change",
            "triage-pending",
            "close-change",
            "deliver-roadmap-phase",
            "work-on-change",
            "work-on-phase",
            "what-next",
        ):
            self.assertIn(required, names)
        self.assertEqual(names[-1], "what-next")
        self.assertEqual(len(names), len(set(names)))

    def test_catalog_exposes_one_development_workflow_bundle(self) -> None:
        catalog = json.loads(
            (REPO_ROOT / "canonical-skills" / "catalog.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            catalog["bundles"],
            [{
                "id": "development-workflow",
                "name": "Development Workflow",
                "description": "Install Pending-aware project navigation, risk-adaptive Change and Phase delivery, independent review, and durable closure as one managed package.",
                "entry_skill": "what-next",
            }],
        )

    def test_bundle_install_smoke_for_codex_and_claude(self) -> None:
        for target in ("codex", "claude"):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as tmp_dir:
                project = Path(tmp_dir)
                bundle = resolve_skill_install_set(
                    REPO_ROOT, ["what-next"], target, allowed_scopes={"public"}
                )
                for skill in bundle:
                    install_skill(REPO_ROOT, project, skill.name, target)
                states = {item.name: item.status for item in list_installed(REPO_ROOT, project, target)}
                self.assertEqual(states["what-next"], "up_to_date")
                self.assertEqual(states["work-on-change"], "up_to_date")
                self.assertEqual(states["work-on-phase"], "up_to_date")
                self.assertEqual(states["review-change"], "up_to_date")


if __name__ == "__main__":
    unittest.main()
