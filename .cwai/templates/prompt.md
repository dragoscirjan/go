---
description: "Prompt Description"
---

Purpose: Purpose of the Prompt

## Input Definition

Variables available to you:

- `ARGUMENTS` – [MANDATORY] The raw feature description text supplied after `/command` (stripped by the rest of variables (`VARIABLE=value`) mentioned bellow).
  - If missing, return: `ERROR: input_unavailable` and describe the prompt (feel free to give an example as well)
- ...

## Execution Flow

```text
1. Summarize your role and requirement (max 100 wors).

2. Instruction 1
   - Sub-instruction 1.1
   - Sub-instruction 1.2
   - Sub-instruction 1.3
   - Sub-instruction 1.4

3. Instruction 2
   - Sub-instruction 2.1
   - Sub-instruction 2.2
   - Sub-instruction 2.3
   - Sub-instruction 2.4
```

If any step fails, emit only an error line: `ERROR: <error_code_[instruction_id]>` and no partial documents.

## Error Codes

- `ERROR: input_unavailable` – Missing or empty `ARGUMENTS`.
- `ERROR: <error_code_[instruction_id]>` - Step in execution flow failed

## Output Contract (Success)

```json
{
  "branch": "<BRANCH_NAME>",
  "documents": [{"file": "<FEATURE_FOLDER>/<file>.md", "type": "<DOCUMENT_TYPE>", "taskType": "<TASK_TYPE>"}],
  "ready": true,
  "next_action_hint": "review_and_create_pr"
}
```

## Acceptance Criteria

- [ ] Criteria 1
- [ ] Criteria 2
