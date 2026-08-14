import json
import unittest
from pathlib import Path

from skill_forge.repository import load_skill


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS = ["plan-change", "implement-task", "run-approved-change", "verify-change", "report-change", "review-change"]
VERSIONS = {
    "plan-change": "1.0.0",
    "implement-task": "1.0.0",
    "run-approved-change": "1.0.0",
    "verify-change": "1.0.0",
    "report-change": "1.0.0",
    "review-change": "1.0.0",
}
UPDATED_AT = {
    "plan-change": "2026-08-14",
    "implement-task": "2026-08-14",
    "run-approved-change": "2026-08-14",
    "verify-change": "2026-08-14",
    "report-change": "2026-08-14",
    "review-change": "2026-08-14",
}
REFERENCES = {
    "plan-change": "IMPLEMENTATION_PLAN_TEMPLATE.md",
    "implement-task": "TASK_HANDOFF_CHECKLIST.md",
    "run-approved-change": "AUTO_EXECUTION_CHECKLIST.md",
    "verify-change": "VERIFICATION_REPORT_TEMPLATE.md",
    "report-change": "CHANGE_REPORT_TEMPLATE.md",
    "review-change": "REVIEW_REPORT_TEMPLATE.md",
}


class PhaseCWorkflowContractTests(unittest.TestCase):
    def test_packages_validate_and_include_owned_reference(self) -> None:
        for name in SKILLS:
            with self.subTest(skill=name):
                skill = load_skill(REPO_ROOT, name)
                self.assertEqual(skill.version, VERSIONS[name])
                self.assertEqual(skill.updated_at, UPDATED_AT[name])
                manifest = json.loads(
                    (REPO_ROOT / "canonical-skills" / "regular-skills" / name / "manifest.json")
                    .read_text(encoding="utf-8")
                )
                paths = {entry["path"] for entry in manifest["files"]}
                self.assertIn(f"references/{REFERENCES[name]}", paths)

    def test_instructions_use_one_working_record_and_stopping_handoff(self) -> None:
        for name in SKILLS:
            with self.subTest(skill=name):
                instruction = (
                    REPO_ROOT / "canonical-skills" / "regular-skills" / name / "instruction.md"
                ).read_text(encoding="utf-8")
                self.assertIn("stop", instruction.lower())
        for name in ("implement-task", "run-approved-change", "report-change"):
            instruction = (REPO_ROOT / "canonical-skills" / "regular-skills" / name / "instruction.md").read_text(encoding="utf-8")
            self.assertIn("handoff", instruction.lower())
        for name in ("plan-change", "implement-task", "run-approved-change", "verify-change", "report-change"):
            instruction = (REPO_ROOT / "canonical-skills" / "regular-skills" / name / "instruction.md").read_text(encoding="utf-8")
            self.assertIn("CHANGE_WORKING.md", instruction)

    def test_catalog_group_is_ordered_and_not_recommended(self) -> None:
        catalog = json.loads(
            (REPO_ROOT / "canonical-skills" / "catalog.json").read_text(encoding="utf-8")
        )
        group = next(group for group in catalog["groups"] if group["name"] == "Change Workflow")
        self.assertEqual(group["skills"], [*SKILLS, "close-change", "triage-pending"])
        self.assertTrue(set(SKILLS).isdisjoint(catalog["recommended"]))

    def test_guideline_marks_phase_c_skills_available(self) -> None:
        guideline = (
            REPO_ROOT / "canonical-configs" / "agent-guideline" / "guideline.md"
        ).read_text(encoding="utf-8")
        self.assertIn("已提供的 Workflow skills", guideline)
        for name in SKILLS:
            self.assertIn(f"`{name}`", guideline)

    def test_formal_review_requires_fresh_non_inherited_context(self) -> None:
        instruction = (
            REPO_ROOT / "canonical-skills" / "regular-skills" / "review-change" / "instruction.md"
        ).read_text(encoding="utf-8")
        self.assertIn("did not inherit the implementation conversation", instruction)
        self.assertIn("Same-context self-checks are not formal review", instruction)
        self.assertIn("one `changes/<change-id>/REVIEW.md`", instruction)

    def test_delivered_bootstrap_is_not_described_as_future_roadmap(self) -> None:
        stale_phrases = ("bootstrap-project` roadmap", "Phase D `bootstrap-project`", "future `bootstrap-project`")
        for name in ("plan-change", "implement-task", "verify-change"):
            instruction = (
                REPO_ROOT / "canonical-skills" / "regular-skills" / name / "instruction.md"
            ).read_text(encoding="utf-8")
            for phrase in stale_phrases:
                self.assertNotIn(phrase, instruction)


if __name__ == "__main__":
    unittest.main()
