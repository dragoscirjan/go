# Language/Stack Rules for Code Generation

Use this file as the canonical ruleset. Follow Global Rules first, then apply the selected Language Rules. Prefer clarity over cleverness and keep outputs runnable, testable, and secure.

## Global Rules

- Code quality: prioritize readability, small functions, single responsibility; adopt ecosystem-standard formatters/linters (e.g., Prettier, Black, gofmt).
- **Instrumentation (mandatory)**: Even when Stack has its proprietary instrumentation, make use of [Taskfile](https://github.com/go-task/task) to write complex tasks that will permit developer to automate tasks.
- **Project Template Enforcement (mandatory)**: If an official template exists for the selected stack, you MUST scaffold from it. Do not bypass or re-create structure ad hoc.
  - Use the command mentioned for the stack to scaffold the project.
- CI/CD: default to deterministic builds; pin dependencies where practical.
- Docs: include a short README or usage notes when creating new runnable code; document code when necessary, explain complicated code sections
- Errors: return explicit errors; avoid silent failures; include context in messages; make use of error codes.
- IO/Args: (when required) usage block; validate flags; exit non-zero on misuse.
- Licensing: do not include copyrighted snippets; generate original code.
- Modules: accepted licenses are MIT and Apache like; anything restricting to make code public is forbidden
- Ports/paths: make configurable via env vars with safe defaults.
- Process: Follow the 8-step Developer Methodology in `../prompts/implement.md` (Setup → Requirements → Design → Implementation → Testing → Documentation → Validation).
- Style: [Google Style Guide](https://google.github.io/styleguide/) or best applicable rules by programming language.
- Testing: include minimal unit tests for new public behavior when feasible.

---

## Plain English

- Guide: Write an implementation of the task, by describing it in Plain English (use Markdown and `.md` files); split the "code" in as many files as you see fit
- Style: Use Plain Logical English Language combined with PseudoCode
- Testing: Write markdown files (`.test.md`) for each `.md` file that you wrote

## Bash

- Code quality: `shellcheck` and `shfmt`.
- Guide: Shell style (internal) and Google Shell Style where applicable.
- Quoting: quote all variable expansions; avoid word-splitting/globbing surprises.
- Runtime: Bash 4 and Above
- Shebang/strict mode: `#!/usr/bin/env bash` and `set -euo pipefail`.
- Style: [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html).
- Testing: small functions; isolate side effects.

## C

- Code Quality: `clang` tools
- Guide: MISRA C (when applicable), CERT C, or project style; prefer consistency.
- Memory: pair alloc/free; check returns; bounds-check.
- Security: avoid unsafe APIs; use size-aware variants.
- Standard: C11+ (C17/C23 if needed); warnings-as-errors.
- Style: Follow established C conventions.
- Testing: Unity/CUnit; sanitizers (ASan/UBSan) in debug.

## C++

- Scaffold: `uvx --from git+https://github.com/templ-project/cpp.git bootstrap $CODE_FOLDER` (use only for new projects)
  - Run the command above, inspect the scaffolded code and remove unnecessary files.
- Code Quality: `clang` tools
- Concurrency: std::thread/atomic; avoid data races.
- Project Template: [templ-project/cpp](https://github.com/templ-project/cpp)
- Standard: C++20+; RAII; smart pointers; no raw new/delete.
- Style: [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html).
- Testing: GoogleTest/Catch2; DI for testability.
- Tooling: -Wall -Wextra -Werror; clang-tidy.

## Elixir

- Concurrency: processes and message passing.
- Formatting: `mix format`; analysis: Credo.
- OTP: supervision trees; isolate side effects.
- Style: [Elixir Style Guide](https://github.com/christopheradams/elixir_style_guide).
- Testing: ExUnit.

## Go

- Code quality: `gofmt`, `go vet`, `staticcheck`.
- Concurrency: goroutines/channels; context propagation mandatory.
- Errors: return errors, not panics (except unrecoverable).
- Style: [Effective Go](https://go.dev/doc/effective_go).
- Testing: testing/testify; table-driven tests.

## Java

- Build: Gradle/Maven; reproducible builds.
- Concurrency: java.util.concurrent; avoid manual threads.
- Frameworks: Spring; prefer constructor injection.
- Style: [Google Java Style](https://google.github.io/styleguide/javaguide.html).
- Testing: JUnit 5; Testcontainers when applicable.

## JavaScript

- Docs: Use JSHint
- Style: [Google JS Style](https://google.github.io/styleguide/jsguide.html); ESLint + Prettier.
- Testing: Vitest (new) or Jest (existing).

### JavaScript (K6)

- Scaffold: `npx --yes --package=github:templ-project/javascript bootstrap $CODE_FOLDER` (use only for new projects)
  - Run the command above, inspect the scaffolded code and remove unnecessary files.
- Runtime: K6 (ES6 subset); avoid Node APIs.
- Testing: Vitest/Jest; mock K6 as needed.

### JavaScript (Node.js)

- Runtime: Node 22 or above, with ESM by default; const/let only.

### JavaScript (Deno)

- Code quality: `deno fmt`, `deno lint`, `deno check` for type-check with JSR/TypeScript.
- CI/CD: cache Deno and modules; run `deno fmt --check`, `deno lint`, `deno test`.
- Packaging: target web-compatible ESM; avoid Node-only APIs.
- Permissions: run with least privilege (`--allow-read` specific paths, avoid `--allow-all`).
- Runtime: Deno stable; default to ESM. Prefer URL imports or `deno.json` imports map.
- Testing: `deno test` for Deno-native; for cross-runtime libraries use Vitest in a separate Node test matrix.

### JavaScript (Bun)

- Code quality: `bun run lint` with ESLint/Prettier; `bun` for scripts and dev server.
- CI/CD: install Bun via official installer; run `bun test` and lint.
- Compatibility: avoid Bun-only APIs unless the project is Bun-only; document support explicitly.
- Runtime: Bun stable; ESM by default. Target web/Node compat where feasible.
- Testing: `bun test` for Bun-native; for cross-runtime libraries, add Vitest in a separate matrix.

## Objective-C

- ARC: use ARC; understand retain/release.
- Patterns: delegation, categories, protocols.
- Style: [Apple Coding Guidelines](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CodingGuidelines/).
- Testing: XCTest; secrets in Keychain.

## PowerShell

- Analysis: PSScriptAnalyzer; tests with Pester.
- Naming: approved verb-noun; parameter validation.
- Portability: target pwsh cross-platform.
- Runtime: Powershell 7
- Style: Microsoft PowerShell Best Practices.

## Python

- Packaging: pyproject.toml; src/ layout.
- Runtime: Python 3.11 or above
- Style: [PEP 8](https://peps.python.org/pep-0008/).
- Testing: pytest with fixtures.
- Tooling: Black; Ruff/flake8.
- Types: type hints; mypy recommended for libs.

## Rust

- Errors: Result with thiserror/anyhow; avoid panics in libs.
- Ownership: avoid unnecessary clones.
- Style: [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/).
- Testing: cargo test; property tests with proptest as needed.
- Tooling: rustfmt + clippy (deny warnings in CI).

## TypeScript

- Scaffold: `npx --yes --package=github:templ-project/typescript bootstrap $CODE_FOLDER` (use only for new projects)
  - Run the command above, inspect the scaffolded code and remove unnecessary files.
- Style: [Google TypeScript Style](https://google.github.io/styleguide/tsguide.html); ESLint + Prettier.
- Testing: Vitest (new) or Jest (existing).

### TypeScript (K6)

- Runtime: K6 constraints; emit ESM.
- Testing: Vitest/Jest; mock K6 as needed.

### TypeScript (Node.js)

- Runtime: Node 22 or above, with ESM by default; const/let only.

### TypeScript (Deno)

- CI/CD: run `deno fmt --check`, `deno lint`, `deno test`.
- Imports: prefer URL imports or import maps; avoid Node resolution semantics.
- Runtime: Deno stable; ESM; use `deno.json` or `deno.jsonc` for compiler options and import maps.
- Testing: `deno test` for platform code; for universal libraries, keep a Node/Vitest job too.
- Types: Deno provides type checking; use `deno check` or `deno test --allow-none`.

### TypeScript (Bun)

- CI/CD: install Bun; run `bun test` and lint; include Node/Vitest if cross-runtime.
- Runtime: Bun stable; ESM; supports TS out of the box.
- Testing: `bun test` for Bun-native; use Vitest for cross-runtime libraries.
- Tooling: ESLint + Prettier; `bunx` to run CLIs.
- Types: configure `tsconfig.json` with `module`=ESNext, `target`=ES2022+; strict mode.

## Zig

- Formatting: built-in formatter.
- Memory: explicit allocators; no hidden allocations in APIs.
- Style: [Zig Style Guide](https://ziglang.org/documentation/master/#Style-Guide).
- Testing: zig test; document comptime usage/invariants.

---

## Security and Secrets (All Languages)

- Never print secrets; redact by default.
- Load secrets from environment or a secret manager; don’t commit to VCS.
- When logging configs, include keys and metadata only, never secret values.

## Observability (All Languages)

- Emit structured logs; prefer JSON when feasible.
- Include request IDs/correlation IDs; add metrics for critical paths.
- Keep logging levels appropriate: info (normal), warn (unexpected but tolerable), error (actionable).

## Deliverables (When Creating Projects)

- Minimal README with run/test instructions
- Dependency manifest (package.json, pyproject.toml, go.mod, Cargo.toml, etc.)
- Lint/format configs
- Unit tests for public APIs
