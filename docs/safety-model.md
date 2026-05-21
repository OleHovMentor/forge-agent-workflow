# Safety Model

Forge Agent Workflow is designed around supervised automation.

The default assumption is simple: AI agents can help prepare and validate changes, but they should not silently execute risky actions or accept their own work.

## Safety boundaries

Default boundaries:

- no credential handling;
- no private key access;
- no real-money actions;
- no production deployment;
- no external messages;
- no destructive shell commands;
- no browser automation without explicit review;
- no final acceptance by the coding agent.

## Agent role boundaries

A coding agent is allowed to:

- edit files inside the allowed scope;
- run local checks requested by the task;
- report compact evidence;
- stop when validation is complete.

A coding agent is not allowed to:

- redefine the roadmap;
- change safety rules;
- broaden its own scope;
- mark final acceptance;
- hide failures;
- claim business results without evidence.

## Approval gates

Approval gates should exist before:

- live external actions;
- irreversible operations;
- production deployments;
- deleting data;
- sending messages;
- changing credentials;
- changing safety policy.

## Evidence quality

A task result should not be accepted just because an agent says it is done.

A good result includes:

- changed files;
- validation commands;
- checker output;
- failures if any;
- remaining manual actions.

## Conservative by design

Forge is intentionally not a full autonomy framework at the start. The project first tries to make human-supervised agent work reliable. More autonomy can come later, but only behind stronger validation and approval layers.