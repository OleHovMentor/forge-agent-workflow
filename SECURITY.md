# Security Policy

Forge Agent Workflow is built around supervised AI coding workflows. Safety is part of the product, not a decorative checkbox.

## Supported versions

This repository is currently in early public bootstrap. Security reports are welcome for the main branch.

## Reporting a vulnerability

Please open a GitHub issue if the report does not contain sensitive details.

If the issue involves secrets, unsafe execution, or private data exposure, do not publish the details publicly. Instead, create a minimal public issue saying that a private security report is needed.

## Safety model

Forge should be safe by default:

- no hidden autonomous execution;
- no secret collection;
- no credential storage;
- no live external actions without explicit human approval;
- no destructive commands by default;
- no fake validation;
- no silent scope expansion;
- no automatic final acceptance.

## Sensitive data

Do not commit:

- API keys;
- access tokens;
- private logs;
- personal data;
- local machine paths that reveal private information;
- production credentials;
- raw agent transcripts containing secrets.

## Unsafe workflow patterns

Please report workflow patterns that could cause:

- agents modifying files outside their allowed scope;
- validators passing without checking real conditions;
- command execution without approval;
- prompt injection through project files;
- evidence packs that hide failures;
- accidental leakage of private project context.

## Philosophy

AI agents should be treated like fast junior developers with shell access: useful, energetic, occasionally brilliant, and absolutely not allowed to run the company unsupervised.