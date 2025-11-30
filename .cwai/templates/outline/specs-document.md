# Spec: <Feature or Module Name>

> One-sentence purpose, or “elevator pitch”.

## 1. Intent & Context

- **Problem / Opportunity**: What gap or need does this address?
- **Users / Actors**: Who interacts with this (user roles, systems)?
- **Success Criteria / Metrics**: How will we know this worked?

## 2. User Journeys & Scenarios

List _key flows_ the system must support, in narrative form:

- As **UserRole**, when **Event**, I want **Outcome**, so that **Benefit**
- _(Optional)_ Alternate or edge flows, failure cases.

## 3. API / Interface Contract _(if applicable)_

Define the shape of the external interface(s):

```yaml
'POST /resource':
  body:
    fieldA: string # description
    fieldB: integer # description
  returns:
    status: 200
    body:
      id: string
      fieldA: string
```

Or alternate forms (CLI, message bus, etc.)

## 4. Architecture & Components

- Modules / Layers: List high-level components.
- Dependencies & Integrations: External services, databases, or libraries.
- Data Models / Domain Entities: Names, key fields, relationships.
- Core Logic Overview: Brief flow or algorithm description.

## 5. Component / Module Spec

For each module (or the “main” one), a mini Low-Level spec:

| Name    | Responsibility         | Inputs      | Outputs   | Notes / Constraints      |
| ------- | ---------------------- | ----------- | --------- | ------------------------ |
| ModuleX | Handles authentication | credentials | userToken | Must enforce rate limits |

Also describe crucial functions / classes:

```text
authenticateUser(credentials: Credentials) → AuthResult
validateToken(token: string) → boolean / error
saveSession(userId: string, sessionData) → void
```

Include edge / failure cases.

## 6. Configuration & Parameters

- List feature flags, timeouts, thresholds, toggleable behaviors.
- Default values and valid ranges.

## 7. Assumptions, Constraints & Boundaries

- Assumptions you’re making for now (e.g., “single-tenant”, “no offline mode”).
- Known limitations or out-of-scope items.
- Constraints (performance, security, data scale).

## 8. Testing & Validation

- Critical paths / flows to test.
- Edge / negative cases.
- Behavior expectations (what happens on error, fallback).
- Possible invariants or assertions the system must always maintain.

## 9. Evolution / Next Phases (Optional)

- Ideas for extension, scaling, or variant behaviors.
- Features you plan to add later.

## 10. Revision / Change Log

| Date       | Author | Summary of changes      |
| ---------- | ------ | ----------------------- |
| YYYY-MM-DD |        | Initial version         |
| YYYY-MM-DD |        | Added module spec for X |
