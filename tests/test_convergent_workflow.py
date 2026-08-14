import unittest
from pathlib import Path

from skill_forge.repository import load_skill, resolve_skill_install_set


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "canonical-skills" / "regular-skills"


class ConvergentWorkflowTests(unittest.TestCase):
    def test_pending_triage_is_controlled_inbox_not_scope_authority(self) -> None:
        instruction = (SKILLS_ROOT / "triage-pending" / "instruction.md").read_text(encoding="utf-8")
        for marker in (
            "controlled inbox",
            "blocking trigger",
            "Unrelated items do not block",
            "Do not use to invent a solution",
            "Do not create or accept an ADR",
        ):
            self.assertIn(marker, instruction)

    def test_closure_requires_absorption_and_human_adr_retention(self) -> None:
        instruction = (SKILLS_ROOT / "close-change" / "instruction.md").read_text(encoding="utf-8")
        for marker in (
            "Absorption Matrix",
            "Decision Retention Packet",
            "mandatory Human Retention Gate",
            "Silence is not approval",
            "second explicit human confirmation",
            "narrow closure-integrity check",
        ):
            self.assertIn(marker, instruction)

    def test_review_budget_and_cosmetic_boundary_are_explicit(self) -> None:
        instruction = (SKILLS_ROOT / "review-change" / "instruction.md").read_text(encoding="utf-8")
        self.assertIn("one full review and one targeted confirmation", instruction)
        self.assertIn("document cosmetics", instruction)
        self.assertIn("rather than creating `review_report_2`", instruction.lower())

    def test_development_bundle_installs_pending_and_closure(self) -> None:
        names = [
            skill.name
            for skill in resolve_skill_install_set(
                REPO_ROOT, ["what-next"], "codex", allowed_scopes={"public"}
            )
        ]
        self.assertIn("triage-pending", names)
        self.assertIn("close-change", names)
        self.assertEqual(names[-1], "what-next")
        self.assertEqual(load_skill(REPO_ROOT, "triage-pending").version, "1.0.0")
        self.assertEqual(load_skill(REPO_ROOT, "close-change").version, "1.0.0")


if __name__ == "__main__":
    unittest.main()
