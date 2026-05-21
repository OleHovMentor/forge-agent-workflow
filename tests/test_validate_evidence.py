from pathlib import Path

from forge_workflow.validate_evidence import OK_MARKER, validate_text, validate_file


def test_validate_text_accepts_required_fields():
    text = """
    files_changed:
    checks_run:
    checks_passed:
    checks_failed:
    next_manual_action:
    """
    assert validate_text(text) == []


def test_validate_text_reports_missing_fields():
    text = "files_changed:\n"
    missing = validate_text(text)
    assert "checks_run:" in missing
    assert "next_manual_action:" in missing


def test_example_evidence_pack_is_valid():
    example_path = Path("examples/evidence_pack_example.md")
    assert validate_file(example_path) == []
