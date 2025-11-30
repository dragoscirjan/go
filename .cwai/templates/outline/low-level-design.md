## Execution Flow (main)

```
1. If no HLD mentioned, load features spec from Input path; else
   → Parse HLD and requirements; if HLD contains [NEEDS CLARIFICATION] tags fail and instruct to use /clarify prompt.
2. If `${FEATURE_FOLDER}/low-level-design.md` exists already,
   → if file contains [NEEDS CLARIFICATION] tags, fail and instruct to use `/clarify` prompt; else
   → continue formulating based on existing content.
3. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Research best implementation for the required feature (produce summary under `${FEATURE_FOLDER}/research.md`)
4. Break system into modules/components.
5. For each module: specify classes, methods, data, interfaces.
6. Add diagrams (class, sequence, state, activity) → WARN if omitted.
7. Define data structures & flows.
8. Specify external/internal interfaces (contracts, formats).
9. Capture algorithms, complexity, error handling, logging.
10. Security, performance, testing details.
11. Validate against assumptions, dependencies, constraints.
12. Run Review Checklist → FAIL if mandatory sections missing or contain only `[NEEDS CLARIFICATION]`.
```

---

## ⚡ Guidelines

- ✅ Focus on **HOW the system is built internally** (classes, methods, data, flows).
- ❌ Do not drift into requirements/business value (belongs to HLD).
- 📐 Use diagrams where possible. Use Mermaid.js
- 🧩 Every interface & module must have unambiguous contracts.
- 🏷 Mark uncertainties with `[NEEDS CLARIFICATION: …]`.

---

# Low-Level Design (LLD): [SYSTEM / MODULE NAME]

**Design ID**: [LLD-###]  
**Service / Domain**: [Service Name]  
**Owner**: [Name / Role]  
**Contributors**: [Names / Roles]  
**Version**: [vX.Y] • **Date**: [YYYY-MM-DD] • **Status**: Draft  
**Input**: Reference HLD: [link or "[NEEDS CLARIFICATION]"]

## Introduction [MANDATORY]

### Purpose

Explain why this LLD exists (ref HLD).

### Scope

What part of the system this LLD covers.

### Audience

Who should read this (devs, testers, ops).

### References

Link to HLD, requirements, standards, documentation.

### Technical Context

- **Language/Version**: [e.g., Python 3.11, Swift 5.9, Rust 1.75 or NEEDS CLARIFICATION]
- **Coding Style Guides**: [e.g. Google Style Guides, PEP8 or NEEDS CLARIFICATION (unless there's smth more language oriented like PEP8, use Google's)] (add link)
- **Primary Dependencies**: [e.g., FastAPI, UIKit, LLVM or NEEDS CLARIFICATION]
- \***\*Storage**: [if applicable, e.g., PostgreSQL, CoreData, files or N/A]
- \***\*Testing**: [e.g., pytest, XCTest, cargo test or NEEDS CLARIFICATION]
- **Target Platform**: [e.g., Linux server, iOS 15+, WASM or NEEDS CLARIFICATION] Project Type: [single/web/mobile - determines source structure]
- **Performance Goals**: [domain-specific, e.g., 1000 req/s, 10k lines/sec, 60 fps or NEEDS CLARIFICATION]
- **Constraints**: [domain-specific, e.g., <200ms p95, <100MB memory, offline-capable or NEEDS CLARIFICATION]
- **Scale/Scope**: [domain-specific, e.g., 10k users, 1M LOC, 50 screens or NEEDS CLARIFICATION]

## 2. System Overview [MANDATORY]

### 2.1 System Description

Brief description.

### 2.2 System Context

Where this component/module fits (with diagram if useful).

## 3. Detailed Design [MANDATORY]

### 3.1 Module Descriptions

- **Module Name**
  - Purpose
  - Responsibilities
  - Dependencies

### 3.2 Class Diagrams

[Include UML diagrams + explanation]

### 3.3 Sequence Diagrams

[Show interactions between classes/modules]

### 3.4 State Diagrams [OPTIONAL]

### 3.5 Activity Diagrams [OPTIONAL]

## 4. Data Design [MANDATORY]

### 4.1 Data Structures

Tables, collections, objects, types.

### 4.2 Database Schema

Tables, keys, constraints.

### 4.3 Data Flow

Detailed flow of information between modules.

## 5. Interface Design [MANDATORY]

### 5.1 User Interfaces

Layouts, inputs, behaviors.

### 5.2 External Interfaces (APIs)

Request/response formats, contracts.

### 5.3 Interface Contracts

Inputs, outputs, pre/post conditions.

## 6. Algorithm Design [MANDATORY]

### 6.1 Algorithms

Pseudocode / flowcharts.

### 6.2 Complexity

Time & space complexity.

## 7. Security Design [MANDATORY]

### 7.1 Measures

Encryption, validation, secure defaults.

### 7.2 Authentication & Authorization

### 7.3 Data Protection

## 8. Error Handling & Logging [MANDATORY]

### 8.1 Error Handling

Strategy, recovery.

### 8.2 Logging

Format, levels, retention.

## 9. Performance Considerations [MANDATORY]

### 9.1 Optimization Techniques

### 9.2 Load Handling & Scaling

## 10. Testing & Validation [MANDATORY]

### 10.1 Unit Testing

### 10.2 Integration Testing

### 10.3 Mapping to HLD Requirements

## 11. Deployment Considerations [OPTIONAL]

### 11.1 Deployment Architecture

### 11.2 Deployment Process

## 12. Assumptions & Dependencies [MANDATORY]

### 12.1 Assumptions

### 12.2 Dependencies

## 13. Appendix [OPTIONAL]

- Glossary
- Acronyms
- Document History

---

## Acceptance Criteria

- ✅ All **mandatory sections** completed.
- ❌ Missing or `[NEEDS CLARIFICATION]` in mandatory sections = **fail review**.
- ⚠ Optional sections may be omitted if not relevant.

---

## Review Checklist

- [ ] LLD aligns with HLD & requirements
- [ ] All modules, data, interfaces detailed
- [ ] Diagrams included where required
- [ ] No implementation-specific configs (LLD ≠ code)
- [ ] Security, error handling, performance covered
- [ ] All mandatory sections filled, no open clarifications

---
