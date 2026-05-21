# Roadmap

Forge Agent Workflow is intentionally conservative. The goal is not to build a magic autonomous agent first. The goal is to make supervised AI coding workflows safer, clearer, and easier to repeat.

## Stage 0: Public OSS bootstrap

Status: in progress

Goals:

- publish a clean public repository;
- explain the workflow model clearly;
- provide example branch prompts and evidence packs;
- add a small deterministic validator;
- document safety boundaries.

Acceptance marker:

```text
OK_FORGE_PUBLIC_BOOTSTRAP
```

## Stage 1: Workflow templates

Goals:

- branch prompt template;
- evidence pack template;
- repair loop template;
- project context template;
- safety policy template.

## Stage 2: Deterministic validators

Goals:

- evidence pack validator;
- branch prompt scope validator;
- forbidden action scanner;
- project context freshness checker;
- compact evidence checker.

## Stage 3: Local CLI

Goals:

- `forge init` for project skeletons;
- `forge make-task` for scoped agent tasks;
- `forge validate` for local checks;
- `forge evidence` for compact evidence packages.

## Stage 4: AI coding agent integrations

Goals:

- Claude Code workflow examples;
- Codex workflow examples;
- generic coding-agent prompt contract;
- human review workflow.

## Stage 5: Supervised session runner

Goals:

- run one scoped task at a time;
- collect logs safely;
- prevent unsafe commands by default;
- stop after validation;
- never auto-accept final results.

## Non-goals for early versions

Forge will not start with:

- autonomous production execution;
- hidden browser automation;
- automatic external messages;
- direct credential handling;
- real-money actions;
- unsafe shell execution without review.

Safety before fancy demos. Fancy demos are how people summon the chaos goblin.