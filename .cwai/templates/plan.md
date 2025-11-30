## Execution Flow

```
1. Parse $DOCUMENT — Extract sections, distinct capabilities, and explicit requirements.
  - Apply `ARGUMENTS` (if provided) to adjust scope, emphasis, or defaults (e.g., MAX_ITEMS, ID_PREFIX, release naming, field emphasis, ordering) within Guardrails.
2. Choose Granularity — Decide top-level item type. See “Granularity selection” rules below.
3. Structure Items — Create the hierarchy according to the chosen granularity.
   - If you need > $MAX_ITEMS top-level items, pause and request confirmation with reasons.
   - Only break into sub-items when it adds delivery clarity (the `/breakdown` command can be used again later).
4. Map Dependencies — Build a dependency graph and detect cycles.
5. Prioritize — Assign Value/Effort/Risk and Priority.
6. Plan Releases — Stage items balancing risk and value; prefer thin vertical slices.
7. Ensure Traceability — Link each item back to a source section.
```

Overrides via ARGUMENTS:

- `ARGUMENTS` may refine how the plan is generated (e.g., prioritize non-functional work first, set a custom ID_PREFIX, change release naming to M1/M2, include/exclude certain fields, tweak MAX_ITEMS). Apply these hints conservatively and never violate Guardrails.

---

# [Definition Document Title] — Delivery Plan

Use the definition document title in this document title. Order top‑level items by Priority (HIGH → MEDIUM → LOW); break ties by source section order.

## EPIC `ID`: `Title`

- Description
- Source: [Section Name](../link/to/document)
- Value: high|medium|low
- Effort: XS|S|M|L|XL
- Risk: low|medium|high
- Priority: HIGH|MEDIUM|LOW
- Release: R1|R2|R3… (apply at the Story level by default; include at Epic if known)
- Dependencies (optional):
  - Parent: `ID`
  - Blocked By: [`ID`, …]
  - Blocking: [`ID`, …]
- Acceptance Criteria (bullet list)

### Story `ID`: `Title`

- Description
- Value: high|medium|low
- Effort: XS|S|M|L|XL
- Risk: low|medium|high
- Priority: HIGH|MEDIUM|LOW
- Release: R1|R2|R3…
- Dependencies: [`ID`, …]
- Acceptance Criteria:
  - 3–7 verifiable criteria, prefer Given/When/Then when useful

  - Task `ID`: `Title`
    - Effort: XS|S|M|L|XL
    - Dependencies: [`ID`, …]
    - Acceptance Criteria:
      - 1–3 concise verifiable checks

## JSON

Use this format when FORMAT=JSON:

```json
{
  "plan": {
    "document": {"title": "<Definition Document Title>", "type": "PRD|GDD|HLD|LLD"},
    "meta": {"idPrefix": "PLAN"}
  },
  "items": [
    {
      "id": "<ID>",
      "title": "<Title>",
      "type": "EPIC|STORY|TASK",
      "description": "Intent/Description",
      "source": {"title": "Section Name", "link": "../link/to/document"},
      "value": "high|medium|low",
      "effort": "XS|S|M|L|XL",
      "risk": "low|medium|high",
      "priority": "HIGH|MEDIUM|LOW",
      "release": "R1|R2|R3",
      "dependencies": {"parent": "<ID>", "blockedBy": ["<ID>"], "blocking": ["<ID>"]},
      "acceptance": ["criteria"],
      "children": []
    }
  ],
  "truncated": {"applied": false, "remaining": 0},
  "notes": {"assumptions": [], "openQuestions": []}
}
```

## Additional Information

Remove this section from the generated document.

### Definitions

- Epic: A large, cross-cutting capability or system. Deliverable across multiple stories.
- Story: A discrete user or system-facing functionality that can be delivered independently.
- Task: An implementation step (design, code, integration, testing, ops) typically owned by a single contributor.
- Capability: A distinct function, feature, or concern described in the source document.

### Output Requirements

Granularity selection (guidelines, not rules):

- PRD/GDD → Epics at top level (may include Stories/Tasks)
- HLD → Stories at top level (may include Tasks; introduce Epics if scope is broad)
- LLD → Tasks at top level (may group under Stories/Epics only if the doc spans multiple components)

General:

- Order top‑level items by Priority (HIGH → MEDIUM → LOW). Break ties by source section order.
- Provide traceability to the source: section title and anchor or hierarchical path.
- Include functional and non‑functional work (security, performance, reliability, usability, compliance, observability, tooling).
- Where the source is ambiguous, record assumptions and open questions.

IDs:

- Use stable IDs with type prefixes and incremental numbers. Example: E-001, S-001-01 (first story under E-001), T-001-01a (first task under S-001-01). Use ID_PREFIX if provided, e.g., PLAN-E-001.

Prioritization and estimates:

- Value: high|medium|low (brief justification inline)
- Effort: XS|S|M|L|XL (tasks inherit or specify their own)
- Risk: low|medium|high (technical/organizational)
- Priority score (optional): concise justification if used; avoid complex formulas.

Dependencies:

- Reference other items by ID. Ensure no cycles; if detected, break one edge and add a note: "dependency-cycle-detected" with involved IDs.

Releases and staging:

- Assign each Story (and its Tasks) to a release stage: R1 (MVP), R2, R3… Prefer thin vertical slices first.

Acceptance criteria:

- Provide 3–7 criteria per Story and 1–3 for Tasks. Prefer Given‑When‑Then where helpful. Keep verifiable and outcome‑focused.

### Output Format

- Order items by Priority. If creating > $MAX_ITEMS top‑level items, request confirmation with a brief justification.

### Guardrails

- Do not invent external links or APIs not present in the source.
- Call out ambiguous or conflicting requirements under “Assumptions” and “Open questions”.
- Keep acceptance criteria testable; avoid unnecessary implementation details.
- Keep total output size reasonable; focus on the highest‑priority items first.

### Examples

Minimal Markdown example:

```markdown
## EPIC E-001: Configuration Service

- Description: Provide centralized, dynamic configuration management.
- Source: HLD / Services / Config (#configuration-service)
- Value/Effort/Risk: high | L | medium — Core platform capability with moderate integration risk.
- Priority: HIGH
- Release: R1
- Dependencies: []

### Story S-001-01: Fetch config by key

- Description: Clients retrieve config via GET /config/{key} with caching.
- Value/Effort/Risk: high | M | low — High consumer value; straightforward implementation.
- Priority: HIGH
- Release: R1
- Dependencies: [E-001]
- Acceptance Criteria:
  - Given a valid key, when a client requests the config, then a 200 response returns the value within 150ms P95.
  - Given an unknown key, then a 404 with problem+json is returned.
  - Given prior access, when a second request is made within TTL, then a cached response is served.

  - Task T-001-01a: Define OpenAPI spec
    - Effort: S
    - Dependencies: []
    - Acceptance Criteria:
      - OpenAPI includes endpoint, parameters, and error responses.
```

Minimal JSON example (shape only):

```json
{
  "plan": {"document": {"type": "HLD"}, "meta": {"idPrefix": "PLAN"}},
  "items": [{"id": "PLAN-E-001", "type": "EPIC", "title": "Configuration Service", "children": []}],
  "truncated": {"applied": false, "remaining": 0}
}
```
