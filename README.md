# Forge Agent Workflow

File-first workflow engine for supervised AI coding agents.

Forge Agent Workflow helps developers run AI coding agents with more structure, safety, and reproducibility. It is designed for workflows where an AI assistant plans work, a coding agent implements a narrow task, local validation checks the result, and a human reviews evidence before accepting changes.

The project is early, but it is built from real AI-assisted development workflows and focuses on a practical problem: coding agents can move fast, but teams still need context discipline, scoped tasks, deterministic checks, evidence packages, and human approval gates.

## Why this exists

AI coding agents are becoming powerful enough to edit projects, run commands, and produce large changes. That creates a new workflow problem:

- project context gets lost between chats, branches, and tools;
- prompts become too large and inconsistent;
- agents may inspect unrelated files or drift outside scope;
- validation can become vague or fake;
- risky actions need human approval, not silent automation;
- developers need compact evidence, not giant logs.

Forge Agent Workflow is a file-first framework for making these workflows safer and easier to repeat.

## Core ideas

- **Source-of-truth context**: project goals, roadmap, safety rules, branch registry, and status live in files, not chat memory.
- **Scoped agent tasks**: each coding-agent run gets a narrow task, allowed files, forbidden files, and a stop condition.
- **Deterministic validation**: local checkers produce clear pass/fail evidence.
- **Evidence packs**: every task should return compact evidence: files changed, checks run, checks passed, checks failed, and next manual action.
- **Human approval gates**: agents can prepare changes, but humans review and accept important transitions.
- **No hidden autonomy by default**: no live external actions, no unsafe execution, and no irreversible operations without explicit approval.

## Intended users

Forge is for:

- solo developers building with Claude Code, Codex, or other AI coding agents;
- small teams that want safer agent-assisted development workflows;
- maintainers who need reproducible context and validation around AI-generated code;
- builders experimenting with supervised multi-agent or orchestrator workflows.

## Current status

This public repository is a cleaned open-source packaging of a local workflow system. The initial release focuses on documentation, workflow templates, examples, and small deterministic validation utilities.

This is not a fully autonomous agent platform. Forge is intentionally conservative: it helps structure supervised work before trying to automate more of it.

## Repository layout

```text
.
├── docs/                  # Concepts and workflow documentation
├── examples/              # Example branch prompts and evidence packs
├── forge_workflow/        # Small Python utilities
├── tests/                 # Minimal validation tests
├── CONTRIBUTING.md
├── ROADMAP.md
├── SECURITY.md
└── README.md
```

## Quick start

Clone the repository:

```bash
git clone https://github.com/OleHovMentor/forge-agent-workflow.git
cd forge-agent-workflow
```

Run the example validator:

```bash
python -m forge_workflow.validate_evidence examples/evidence_pack_example.md
```

Expected result:

```text
OK_FORGE_EVIDENCE_PACK
```

## Example workflow

1. Define project goal and safety boundaries in files.
2. Create a narrow branch/task prompt for an AI coding agent.
3. Run the agent only on the allowed scope.
4. Run deterministic local validation.
5. Collect compact evidence.
6. Human reviews and accepts or sends the task back for repair.

## What Forge is not

Forge is not:

- a trading bot;
- a browser automation bot;
- an autonomous production operator;
- a replacement for code review;
- a system for bypassing human approval;
- a framework for hiding risky execution behind AI.

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## Contributing

Contributions are welcome, especially around examples, workflow templates, safety checks, and integrations with AI coding tools. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

If you find a vulnerability or unsafe workflow pattern, please read [SECURITY.md](SECURITY.md).

## License

Apache License 2.0
