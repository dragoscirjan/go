# Testing prompts

- [Testing prompts](#testing-prompts)
  - [`/outline`](#outline)
    - [ERROR: input_unavailable](#error-input_unavailable)
    - [Print back Inputs](#print-back-inputs)
    - [Print back instructions summary](#print-back-instructions-summary)
    - [Generate HLD](#generate-hld)

## `/outline`

### ERROR: input_unavailable

Running `/outline` should print `ERROR: input_unavailable` and stop

### Print back Inputs

Running `/outline --type lld --stack javascript,deno **stop execution** just after you detected all inputs and print them in JSON format` should print the inputs in JSON format

```json
{
  "SCRIPT": ".cwai/scripts/create-feature.sh",
  "TEMPLATE": "low-level-design",
  "TEMPLATE_PATH": ".cwai/templates/outline/low-level-design.md",
  "TASK_TYPE": "task",
  "DOCUMENT_TYPE": "lld",
  "LLD_STACK": "javascript,deno",
  "ARGUMENTS": "write a simple HLD about a config module"
}
```

### Print back instructions summary

Running

```
/outline --type lld --stack javascript,deno **stop execution** just before running `SCRIPT`, but print the command and summarize all the steps you need execute
```

should summarize the steps needed to excecute after the `SCRIPT` command is execute

### Generate HLD

Running

```
/outline --type hld --stack javascript,deno Generic Multi Purpose Config Module: Write a HLD for a config module for services. HLD should
- be agnostic of technology
- be agnostic of cloud versus on-prem usage

Module should
- be able to load configuration from files
- be able to support override from environment variables (define mapping standard between env vars and config paths)
- fail fast and loud on errors
- support hot reload
- emit events on hot reload (config change, hot reload errors, etc)
```

And follow the process.
To undo run

```bash
git checkout main && git branch | grep 000 | xargs git branch -D && rm -rf specs
```

## `/clarify`

### ERROR: input_unavailable

Running `/outline` should print `ERROR: input_unavailable` and stop

### Present 5 items to clarify

Running `/clarify specs/00001-generic-multi-purpose-config-module/high-level-design.md` should present 5 items that need to be clarified

## `/breakdown`

### ERROR: input_unavailable

Running `/outline` should print `ERROR: input_unavailable` and stop

### Plan 6 epics

Running `/breakdown specs/00001-generic-multi-purpose-config-module/high-level-design.md --format json` should create 6 epics under `high-level-desing.plan.json`
