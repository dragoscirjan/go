---
description: Break down the provided design document into a set of epics, stories, tasks, etc
---

## Implementation Decomposition Planning Prompt

Purpose: Given a design/spec document, produce a structured delivery plan broken down into Epics → Stories → Tasks with clear acceptance criteria, traceability to source sections, dependencies, estimates, and release staging. Output must be deterministic, concise, and execution‑ready.

## Input Definition

Variables available to you:

- `DOCUMENT` — [MANDATORY] Path to spec file (e.g., `DOCUMENT=specs/00001-config-module/high-level-design.md`)
  - If missing, return: `ERROR: missing_document`

- `ARGUMENTS` - [OPTIONAL] The raw feature description text supplied after `/breakdown` (stripped by the rest of variables (`VARIABLE=value`) mentioned bellow).
- `DOCUMENT_TYPE` – [OPTIONAL] User hint: one of `prd|gdd|hld|lld|spec` (case-insensitive) (e.g. `DOCUMENT_TYPE=hld`).
  - If not mentioned, use heuristic detection on `ARGUMENTS` based on [Supported Doc Type Heuristics] section of this document and your experience
  - If unclear, return: `ERROR: document_type_ambiguous`
- `FORMAT` — [OPTIONAL] Default `markdown`. User hint: one of `markdown|json` (e.g. `FORMAT=markdown`)
- `MAX_ITEMS` — [OPTIONAL] Default: 6 — Maximum number of top‑level items (e.g. `MAX_ITEMS=12`)

## Execution Flow

**Mandatory actions** → Given the feature description (and `ARGUMENTS`), follow these steps **exactly**:

```
1. Validate Input
   - Confirm `DOCUMENT` path exists and is readable.
   - If missing or invalid, return `ERROR: invalid_document`.

2. Summarize your role and requirement (max 100 wors).

3. Produce Plan
   - Follow `.cwai/templates/plan.md` precisely (terminology, fields, ordering).
   - Select granularity based on `DOCUMENT_TYPE` and content.

4. Generate Output
   - Produce in requested `FORMAT`.
   - File location: same folder as `DOCUMENT`.
   - Filename: `<document-name>.plan.md` or `<document-name>.plan.json`.
   - Apply `MAX_ITEMS` to top‑level items; if exceeding, pause and request confirmation with a brief justification.

5. Clean Up
   - Remove instructional/placeholder sections not meant for final output.

6. Report Completion (stdout/log)
   - Count of top‑level items
   - List of item IDs with titles (ordered by priority)
```

If any step fails, emit only an error line: `ERROR: <error_code>` and no partial documents.
Also, return `ERROR: insufficient_signal` if `DOCUMENT` contains fewer than 2 distinct capabilities.

## Error Codes

- `ERROR: missing_document` – Mandatory `DOCUMENT` not provided.
- `ERROR: invalid_document` – `DOCUMENT` path does not exist or is unreadable.
- `ERROR: document_type_ambiguous` – Multiple candidate types with equal weight.
- `ERROR: insufficient_signal` – `DOCUMENT` contains fewer than 2 distinct capabilities.

## Supported Doc Type Heuristics

| Type | Required Identifier (any match)                   | Primary Template File                                     |
| ---- | ------------------------------------------------- | --------------------------------------------------------- |
| PRD  | `Product Requirements Document` / `PRD ID`        | `.cwai/templates/outline/product-requirement-document.md` |
| HLD  | `High-Level Design (HLD)` / `Target Architecture` | `.cwai/templates/outline/high-level-design.md`            |
| LLD  | `Low-Level Design (LLD)` / `Module Descriptions`  | `.cwai/templates/outline/low-level-design.md`             |
| GDD  | `Game Design Document (GDD)` / `Core Loop`        | `.cwai/templates/outline/game-design.md`                  |

If ambiguous (multiple heuristics) → determine a best fit for the document and act accordingly; analyze based on the $ARGUMENTS requirement.
