"""Validate a compact Forge evidence pack.

This validator intentionally checks structure, not business success.
It is a small example of deterministic validation for supervised AI coding workflows.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

REQUIRED_FIELDS = (
    "files_changed:",
    "checks_run:",
    "checks_passed:",
    "checks_failed:",
    "next_manual_action:",
)

OK_MARKER = "OK_FORGE_EVIDENCE_PACK"


def validate_text(text: str) -> list[str]:
    """Return a list of missing required evidence fields."""
    lowered = text.lower()
    return [field for field in REQUIRED_FIELDS if field not in lowered]


def validate_file(path: Path) -> list[str]:
    """Validate one evidence pack file."""
    if not path.exists():
        return [f"file_not_found: {path}"]
    if not path.is_file():
        return [f"not_a_file: {path}"]

    text = path.read_text(encoding="utf-8")
    return validate_text(text)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a Forge evidence pack.")
    parser.add_argument("path", help="Path to the evidence pack markdown file.")
    args = parser.parse_args(argv)

    missing = validate_file(Path(args.path))
    if missing:
        print("ERROR_FORGE_EVIDENCE_PACK")
        for item in missing:
            print(f"missing={item}")
        return 1

    print(OK_MARKER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
