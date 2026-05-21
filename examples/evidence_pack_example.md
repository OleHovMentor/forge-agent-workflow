# Evidence Pack Example

branch_id: example-001
status: locally_validated

files_changed:
- forge_workflow/validate_evidence.py
- examples/evidence_pack_example.md

checks_run:
- python -m forge_workflow.validate_evidence examples/evidence_pack_example.md

checks_passed:
- evidence_pack_required_fields_present

checks_failed:
- none

next_manual_action:
- Human reviews the evidence pack and decides whether to accept the task.

notes:
- This is a sample evidence pack for documentation and validator testing.
- The validator checks structure only; it does not prove business success.