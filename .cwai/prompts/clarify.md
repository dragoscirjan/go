---
description: "Analyze an existing design spec (PRD / HLD / LLD / GDD) and produce structured clarifying questions & completion guidance"
---

Purpose: Given one or more already generated design documents (Product Requirement Document, High-Level Design, Low-Level Design, Game Design Document), analyze gaps, ambiguities, structural defects, and readiness for its downstream phase. Output ONLY questions and actionable recommendations—never fabricate answers.

## Input Definition

The user input is always available to you as raw text (even if `$ARGUMENTS` appears literally somewhere). If input is missing or invalid→ stop and report: `ERROR: input_unavailable`.

Variables available to you:

- `ARGUMENTS` - [OPTIONAL] The raw feature description text supplied after `/clarify` (stripped by the rest of variables (`VARIABLE=value`) mentioned bellow).
- `DOCUMENT` - [MANDATORY] Path to a single spec file (e.g. `DOCUMENT=specs/00001-generic-multi-purpose-config-module/high-level-design.md`)
  - If missing, return: `ERROR: missing_document`

- `DOCUMENT_TYPE` – [OPTIONAL] User hint: one of `prd|gdd|hld|lld|spec` (case-insensitive) (e.g. `DOCUMENT_TYPE=hld`).
  - If not mentioned, use heuristic detection on `ARGUMENTS` based on [Supported Doc Type Heuristics] section of this document and your experience
  - If unclear, return: `ERROR: document_type_ambiguous`
- `CLARIFY_FOCUS` - [OPTIONAL] Value looked up from the [Clarification Question Domains] - Limits question domains (e.g. `CLARIFY_FOCUS=security,performance`)
  - If missing or unclear, consider all values
- `CLARIFY_MAX_ITEMS` - [OPTIONAL] Default: 10. Limits the number of questions to be asked (.e.g `CLARIFY_MAX_ITEMS=5`)

## Execution Flow

**Mandatory actions** → Given the feature description (and `ARGUMENTS`), follow these steps **exactly**:

```
1. Summarize your role and requirement (max 100 wors).

2. Load $DOCUMENT, read the `issue.json` file present in the same folder as the $DOCUMENT and
  a. Detect type from $DOCUMENT_TYPE or (heuristics) $ARGUMENTS.
  b. If exists, load the corresponding template (from `.cwai/templates/...`) in memory (do NOT output it).
  c. Build Mandatory Section Inventory from template (section headings marked [MANDATORY]).
  d. Analyze document, parse for `[NEEDS CLARIFICATION]` tags.
  e. Analyze document, understand it based on the `issue.json` requirements, consider missing not discussed items.
  f. Analyze document, compare it with the original template, consider missing items.
  g. Prepare a list of unknowns based on $CLARIFY_FOCUS values; limit it to $CLARIFY_MAX_ITEMS most important ones

3. Consolidate document based on questions asked to user (use the list of unknowns) and answers received by user

4. Reformulate $DOCUMENT to include the clarifications and increase $DOCUMENT's version (overwrite or inline edit)
```

If any step fails, emit only an error line: `ERROR: <error_code>` and no partial documents.

## Error Codes

- `ERROR: input_unavailable` – Missing or empty `ARGUMENTS`.
- `ERROR: missing_document` – Mandatory `DOCUMENT` not provided.
- `ERROR: document_type_ambiguous` – Multiple candidate types with equal weight.

## Supported Doc Type Heuristics

| Type | Required Identifier (any match)                   | Primary Template File                                     |
| ---- | ------------------------------------------------- | --------------------------------------------------------- |
| PRD  | `Product Requirements Document` / `PRD ID`        | `.cwai/templates/outline/product-requirement-document.md` |
| HLD  | `High-Level Design (HLD)` / `Target Architecture` | `.cwai/templates/outline/high-level-design.md`            |
| LLD  | `Low-Level Design (LLD)` / `Module Descriptions`  | `.cwai/templates/outline/low-level-design.md`             |
| GDD  | `Game Design Document (GDD)` / `Core Loop`        | `.cwai/templates/outline/game-design.md`                  |

If ambiguous (multiple heuristics) → determine a best fit for the document and act accordingly; analyze based on the $ARGUMENTS requirement.

## Clarification Question Domains

Use only domains that apply (omit empty):
`requirements`, `scope`, `objectives`, `assumptions`, `constraints`, `dependencies`, `architecture-logical`, `architecture-physical`, `interfaces`, `data`, `algorithms`, `security`, `performance`, `reliability`, `continuity`, `costs`, `operations`, `risks`, `testing`, `compliance`, `gameplay`, `progression`, `mechanics`, `accessibility`, `metrics`, `diagrams`, `other`.

## Question Structure

Each question MUST:

```text
ID: Q-### (sequential, per document)
Domain: one of allowed domains
Severity: BLOCKER|HIGH|MEDIUM|LOW
Context: 1–2 line cite (quote or paraphrase fragment) OR `section-missing`
Question: Direct, specific, singular
Required Data Form: e.g. "Provide numeric target (p95 latency in ms)" / "List interface fields (name:type:direction)" / "Decision rationale (chosen vs alternatives)"
```

Never bundle multiple unknowns in one question. Avoid yes/no phrasing unless validating an assumption.
