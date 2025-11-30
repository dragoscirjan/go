## Execution Flow (main) (remove at cleanup)

```
1. Parse inputs (business brief, drivers, requirements, current state)
   → If missing: ERROR "Insufficient inputs for HLD"
2. If `${FEATURE_FOLDER}/high-level-design.md` exists already,
   → if file contains [NEEDS CLARIFICATION] tags, fail and instruct to use `/clarify` prompt; else
   → continue formulating based on existing content.
3. Summarize Context & Drivers
   → Validate objectives are SMART; else WARN and mark [NEEDS CLARIFICATION]
4. Capture Assumptions, Constraints, Dependencies
5. Document Current State (logical, physical, interfaces)
   → If unknown: WARN and mark discovery tasks
6. Propose Target Architecture (logical first, then physical)
   → Include interface impacts; avoid vendor lock-in specifics unless required
7. Define NFRs & Service Continuity (RTO/RPO, failure modes, SPOF, symmetry)
8. Asses Security & Compliance (threats, controls, data flows)
9. Estimate Cost Model (CapEx / OpEx) & Support Model
10. Define Risks & Mitigations; Decommissioning; Roadmap
11. Run Review Checklist
    → If any [NEEDS CLARIFICATION]: WARN "HLD has uncertainties"
    → If low-level build details present: ERROR "Remove implementation detail"
12. Cleanup document of unnecessary sections.
13. Return: SUCCESS (HLD ready for governance / planning)
```

---

## ⚡ Quick Guidelines (remove at cleanup)

- ✅ HLD = **WHAT the solution looks like** and **WHY these choices**, not step-by-step build.
- ❌ No low-level config, code, or vendor SKUs (leave for LLD/implementation).
- 🧩 Separate **logical** (concepts & flows) from **physical** (tech components).
- 📐 Use diagrams where possible. Use Mermaid.js
- 🧪 Every decision should map to drivers, requirements, or constraints.
- 🏷 Use `[NEEDS CLARIFICATION: …]` instead of guessing.

---

# High-Level Design (HLD): [SYSTEM / FEATURE NAME] [MANDATORY]

**Design ID**: [HLD-###]
**Service / Domain**: [Service Name]
**Owner**: [Name / Role]
**Contributors**: [Names / Roles]
**Version**: [vX.Y] • **Date**: [YYYY-MM-DD] • **Status**: Draft
**Input**: Business brief / proposal link: [URL or "[NEEDS CLARIFICATION: missing]"]

## Document History [MANDATORY]

| Version | Date       | Summary of Change | Reference ID |
| ------: | ---------- | ----------------- | ------------ |
|     1.0 | 2014-07-15 | Initial draft     | -            |

## Design Ownership (RACI-lite) [MANDATORY]

| Role                                   | Responsibility                        | Named Individual |
| -------------------------------------- | ------------------------------------- | ---------------- |
| Design Owner (Essential)               | Owns HLD content/versioning; handover |                  |
| Project Manager                        | Delivery governance                   |                  |
| Service Owner (Essential)              | Service lifecycle accountability      |                  |
| Service Operations Manager (Essential) | Operational readiness                 |                  |
| Design Mentor (Essential)              | Architecture review                   |                  |
| Business                               | Requirements integrity                |                  |
| Applications & Data                    | App/data architecture                 |                  |
| Technology                             | Platform standards alignment          |                  |

## 1 Context [MANDATORY]

### 1.1 Summary (for non-technical stakeholders) [MANDATORY]

- Service/system name: [ ]
- Change type: [New / Change / Upgrade]
- Business areas affected: [ ]
- Why now (driver): [ ]
- Expected outcomes: [ ]
- Very high-level “how”: [ ]
- Criticality / categorisation: [Low/Med/High or [NEEDS CLARIFICATION]]

### 1.2 Links to Documentation [MANDATORY]

- Business case / PID: [ ]
- Prior designs / related docs: [ ]
- Requirements doc: [ ]

## 2 Drivers, Requirements, Objectives [MANDATORY]

### 2.1 Drivers [MANDATORY]

- [ ]

### 2.2 Requirements (Functional & Non-Functional) [MANDATORY]

- Reference / link: [ ]
- Gaps: [NEEDS CLARIFICATION: …]

### 2.3 Objectives (SMART) [MANDATORY]

| ID     | Objective | Success Criteria |
| ------ | --------- | ---------------- |
| OBJ-01 |           |                  |

### 2.4 Impact of No Action [MANDATORY]

- [Business/operational risk if unchanged]

## 3 Assumptions, Constraints, Dependencies [MANDATORY]

### 3.1 Assumptions [MANDATORY]

| Assumption                | Impact on Design |
| ------------------------- | ---------------- |
| Org growth 10% YoY        |                  |
| ISD shrinks 1% real terms |                  |
| Split DC model (~30km)    |                  |
| Additional                |                  |

### 3.2 Constraints [MANDATORY]

- Funding: [ ]
- Skills / resources: [ ]
- Existing tech lock-in: [ ]
- Timescales: [ ]
- Customer process rigidity: [ ]
- Pre-purchased items: [ ]

### 3.3 Dependencies [MANDATORY]

- Other departments: [ ]
- Suppliers: [ ]
- Internal groups / other projects: [ ]
- Those dependent on this design: [ ]

## 4 Current State [MANDATORY]

### 4.1 Logical / Architectural Summary [MANDATORY]

- Key components, actors, data, flows.

### 4.2 Logical Diagrams [OPTIONAL]

- DFD / ERD / Use cases.
- Internal interfaces: [ ]

### 4.3 Physical Technology Summary [MANDATORY]

- Hardware / software / platforms in scope.

### 4.4 Physical Diagrams [OPTIONAL]

- Network / compute / storage / app topology.

### 4.5 External Interfaces [MANDATORY]

- Systems: [AD, DNS, Email, Monitoring, myFinance, myView, ETLs, Storage]
- Known change impacts: [ ]

### 4.6 Current Limitations [MANDATORY]

| ID     | Limitation | Impact |
| ------ | ---------- | ------ |
| LIM-01 |            |        |

## 5 Target Architecture [MANDATORY]

### 5.1 Options Considered (Brief) [MANDATORY]

- Alternatives & rationale for selection.

### 5.2 Logical Target Design [MANDATORY]

- Changes from current: [ ]
- Known logical limitations (1-year / 5-year): [ ]
- Residual risks/limitations: [ ]

### 5.3 Physical Solution Summary [MANDATORY]

- Platforms, hosting model, data stores, major products (generic—no SKUs).
- Reference designs cited: [Suppliers/SMEs]

### 5.4 Physical Diagrams [OPTIONAL]

- Network / server / storage / app / data.

### 5.5 Interfaces (Target) [MANDATORY]

| Interface | Change Summary | Effort | Owner |
| --------- | -------------- | ------ | ----- |
|           |                |        |       |

## 6 Service Continuity & NFRs [MANDATORY]

### 6.1 Criticality & SLOs [MANDATORY]

- Criticality: [ ]
- Availability target: [ ]
- RTO: [ ] • RPO: [ ]
- Performance / scale targets: [NEEDS CLARIFICATION if missing]

### 6.2 Backup & Recovery [MANDATORY]

- Scope, frequency, retention, recovery procedures, BCP link.

### 6.3 Failure Modes & Response [MANDATORY]

| Failure Mode                    | Required Function | High-Level Process |
| ------------------------------- | ----------------- | ------------------ |
| Loss of single site (planned)   |                   |                    |
| Loss of single site (unplanned) |                   |                    |
| Data loss (partial/complete)    |                   |                    |
| During component updates        |                   |                    |

### 6.4 Single Points of Failure [MANDATORY]

- [ ]

### 6.5 Symmetry (Primary vs Secondary) [OPTIONAL]

- [ ]

## 7 Security & Compliance [MANDATORY]

- Data classification, flows, and boundaries
- Threats & controls (authn/z, logging, monitoring)
- Regulatory/standards: [ ]
- Open issues: [NEEDS CLARIFICATION]

## 8 Update Methodology [MANDATORY]

For major elements: frequency, type, responsibility, expected cost.

## 9 Benefits (High Level) [MANDATORY]

- [Business, operational, risk reduction]

## 10 Risks & Mitigations (Residual) [MANDATORY]

| Risk | Type | Summary | Mitigation |
| ---- | ---- | ------- | ---------- |
|      |      |         |            |

## 11 Cost Model (High Level, excl. project costs) [MANDATORY]

### 11.1 CapEx [MANDATORY]

- Servers, upfront licenses, network, facilities.

### 11.2 CapEx-Generated OpEx [OPTIONAL]

- Support, maintenance, per-seat/size uplifts, HW maintenance, annual health checks.

### 11.3 OpEx [MANDATORY]

- Hosting, backup, comms & networks.

## 12 Support & Operations [MANDATORY]

### 12.1 Service Governance [MANDATORY]

- Service Owner, Service Operations Manager, Business Owner.

### 12.2 Operational Support [MANDATORY]

| Element | Capabilities Required | Anticipated Load | Current Capacity | Training/Resourcing Needed |
| ------- | --------------------- | ---------------- | ---------------- | -------------------------- |
|         |                       |                  |                  |                            |

## 13 Decommissioning Targets [MANDATORY]

- Services / Infrastructure to retire; timing from delivery.
  | Element | Replaced By | Decommission Type | Timescale |
  |---------|-------------|-------------------|----------|
  | | | | |

## 14 Block Scheduling & Lifecycle [OPTIONAL]

- Major blocks, lifecycle stages, decision gates; where outputs go (CAB, etc.).

## 15 Potential Future Improvements [OPTIONAL]

- Near-term and strategic enhancements.

---

## Review & Acceptance Checklist (Gate) (remove at cleanup)

### Content Quality]

- [ ] No low-level implementation details
- [ ] Logical and physical separated & justified
- [ ] Stakeholder-readable; links provided
- [ ] Objectives SMART and mapped to drivers

### Completeness]

- [ ] Assumptions/constraints/dependencies explicit
- [ ] Current state and target defined with diagrams
- [ ] NFRs & continuity (RTO/RPO) set
- [ ] Interfaces and impacts captured
- [ ] Security & compliance addressed
- [ ] Costs & support model outlined
- [ ] Decommissioning and risks listed
- [ ] No [NEEDS CLARIFICATION] remain

---

## Execution Status (auto-updated by main())

- [ ] Inputs parsed
- [ ] Context & drivers summarized
- [ ] Assumptions/constraints/dependencies captured
- [ ] Current state documented
- [ ] Target architecture defined (logical/physical)
- [ ] NFRs & continuity set
- [ ] Security & compliance covered
- [ ] Costs & support defined
- [ ] Risks & decommissioning set
- [ ] Review checklist passed
