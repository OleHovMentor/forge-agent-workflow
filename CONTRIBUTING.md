# Contributing

Thanks for considering a contribution to Forge Agent Workflow.

This project is about supervised AI coding workflows: clear context, narrow tasks, deterministic validation, compact evidence, and human approval gates.

## Good contributions

Useful contributions include:

- better examples for Claude Code, Codex, or other coding agents;
- safer branch prompt templates;
- deterministic validators;
- documentation improvements;
- issue templates;
- small utilities that make supervised workflows easier;
- safety checks for risky commands or out-of-scope agent behavior.

## Contribution principles

Please keep changes:

- small;
- reviewable;
- deterministic where possible;
- documented;
- safe by default.

A good pull request should explain:

- what changed;
- why it changed;
- how it was tested;
- what risks remain.

## What not to contribute

Please do not add:

- code that executes external actions without review;
- credential collection or secret storage;
- real-money automation;
- trading execution;
- spam, scraping, or cold outreach automation;
- hidden browser control;
- large unrelated rewrites.

## Pull request checklist

Before opening a pull request:

- [ ] The change is scoped.
- [ ] The README or docs are updated if behavior changed.
- [ ] A validator or test is included where appropriate.
- [ ] No secrets, tokens, private paths, or personal data are included.
- [ ] The evidence is clear and compact.

## Development

For now, the project uses standard Python with no heavy dependency stack.

Run the example validator:

```bash
python -m forge_workflow.validate_evidence examples/evidence_pack_example.md
```

Expected output:

```text
OK_FORGE_EVIDENCE_PACK
```