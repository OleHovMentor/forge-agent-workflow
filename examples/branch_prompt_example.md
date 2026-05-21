# Example Branch Prompt

## Role

You are a scoped coding agent working inside a supervised Forge Agent Workflow task.

## Goal

Add a small deterministic validator for evidence packs.

## Allowed files

- `forge_workflow/validate_evidence.py`
- `examples/evidence_pack_example.md`
- `tests/test_validate_evidence.py`

## Forbidden files

- `.github/`
- `LICENSE`
- `SECURITY.md`
- any file outside the allowed list

## Requirements

The validator must check that an evidence pack includes:

- `files_changed:`
- `checks_run:`
- `checks_passed:`
- `checks_failed:`
- `next_manual_action:`

If all fields exist, print:

```text
OK_FORGE_EVIDENCE_PACK
```

If any required field is missing, print a clear error and exit non-zero.

## Validation command

```bash
python -m forge_workflow.validate_evidence examples/evidence_pack_example.md
```

## Stop condition

Stop after local validation. Do not mark final acceptance. Return compact evidence only.

## Compact evidence format

```text
files_changed:
checks_run:
checks_passed:
checks_failed:
next_manual_action:
```