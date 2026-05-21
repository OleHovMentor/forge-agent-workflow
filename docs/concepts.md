# Concepts

Forge Agent Workflow uses a few simple concepts.

## Source-of-truth context

Important project information should live in files, not only in a chat thread.

Examples:

- project goal;
- roadmap;
- safety policy;
- branch registry;
- current status;
- validation rules.

This makes agent work easier to resume, audit, and reproduce.

## Scoped task

A scoped task is a small unit of work for a coding agent.

It should include:

- goal;
- allowed files;
- forbidden files;
- exact expected output;
- validation command;
- stop condition.

The agent should not inspect unrelated files or broaden the task.

## Deterministic validation

A deterministic validator produces a clear result from local files or command output.

Good result:

```text
OK_FORGE_EVIDENCE_PACK
```

Bad result:

```text
ERROR: missing checks_run
```

The point is to avoid vague validation such as "looks good".

## Evidence pack

An evidence pack is a compact report after a task.

It should answer:

- what changed;
- which files changed;
- which checks ran;
- which checks passed;
- which checks failed;
- what manual review is still needed.

## Human approval gate

A human approval gate is the point where a person reviews evidence before accepting a result or allowing a risky action.

Forge assumes that AI agents can prepare work, but humans decide when important states become accepted.

## Repair loop

When validation fails, the task should go back to the agent with a narrow repair prompt. The repair prompt should focus only on the failing evidence, not reopen the whole project.