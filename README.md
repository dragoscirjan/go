# Go Bootstrap Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go CI](https://github.com/templ-project/go/actions/workflows/ci.yml/badge.svg)](https://github.com/templ-project/go/actions/workflows/ci.yml)
[![Go Report Card](https://goreportcard.com/badge/github.com/templ-project/go)](https://goreportcard.com/report/github.com/templ-project/go)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/templ-project/go/issues)

> A modern, cross-platform Go project template with comprehensive tooling, linting, and quality checks built-in.

- [Go Bootstrap Template](#go-bootstrap-template)
  - [Quick Start](#quick-start)
  - [What's Included](#whats-included)
  - [Common Commands](#common-commands)
  - [Requirements](#requirements)
  - [Setup Development Environment](#setup-development-environment)
  - [Project Structure](#project-structure)
  - [Building](#building)
  - [Testing](#testing)
  - [Code Quality](#code-quality)
    - [Pre-commit Hooks](#pre-commit-hooks)
    - [golangci-lint Configuration](#golangci-lint-configuration)
  - [Configuration](#configuration)
  - [Using as a Library](#using-as-a-library)
  - [CI/CD Pipeline](#cicd-pipeline)
  - [License](#license)
  - [Support](#support)

## Quick Start

**Bootstrap a new project:**

Using uvx (recommended):

```bash
uvx --from git+https://github.com/templ-project/go.git bootstrap my-project
cd my-project
task deps:sync
task test
```

Or clone manually:

```bash
git clone https://github.com/templ-project/go.git my-project
cd my-project
rm -rf .git
task deps:sync
task build
```

That's it! You now have a fully configured Go project with linting, formatting, testing, and quality tools.

## What's Included

| Feature                 | Tool                                                                                              | Description                        |
| ----------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **Language**            | [Go 1.23](https://go.dev/)                                                                        | Modern Go toolchain                |
| **Task Runner**         | [Taskfile](https://taskfile.dev/)                                                                 | Modern build automation            |
| **Tool Management**     | [mise](https://mise.jdx.dev/)                                                                     | Isolated development environment   |
| **Go Linting**          | [golangci-lint](https://golangci-lint.run/)                                                       | 18+ linters (gosec, errcheck, etc) |
| **Code Formatting**     | gofmt + [Prettier](https://prettier.io/)                                                          | Go and config file formatting      |
| **Testing**             | [gotestsum](https://github.com/gotestyourself/gotestsum)                                          | Enhanced test output with coverage |
| **Benchmarking**        | `go test -bench`                                                                                  | Performance testing support        |
| **Pre-commit Hooks**    | [Husky](https://typicode.github.io/husky/) + [lint-staged](https://github.com/okonet/lint-staged) | Automatic validation               |
| **Duplicate Detection** | [jscpd](https://github.com/kucherenko/jscpd)                                                      | Copy-paste detector                |
| **Documentation**       | [MkDocs](https://www.mkdocs.org/) + godoc                                                         | Material theme docs + Go docs      |
| **CI/CD**               | GitHub Actions                                                                                    | Multi-platform testing & releases  |

## Common Commands

```bash
# === Development ===
task run                 # Build and run the application
task build               # Build the project
task build:all           # Build for all platforms (Linux, macOS, Windows)
task clean               # Clean build artifacts

# === Code Formatting ===
task format              # Format all code (gofmt, Prettier)
task format:check        # Check formatting without fixing

# === Linting ===
task lint                # Lint all code (golangci-lint, ESLint)
task lint:check          # Check all without fixing

# === Testing ===
task test                # Run tests with race detection and coverage
task test:coverage       # Run tests with coverage report
task test:gen-coverage   # Generate HTML coverage report
task test:bench          # Run benchmark tests

# === Code Quality ===
task duplicate-check     # Check for duplicate code

# === Documentation ===
task docs                # Build documentation
task docs:serve          # Serve documentation locally
task docs:godoc          # Start godoc server

# === Debugging ===
task debug               # Run with delve debugger

# === Full Validation ===
task validate            # Run complete CI pipeline locally

# === Dependencies ===
task deps:sync           # Install all dependencies (mise, npm, go mod)
task deps:refresh        # Update all dependencies
task deps:clean          # Remove all dependencies
```

## Requirements

- [mise](https://mise.jdx.dev/) - Tool version management (installs everything else)
- [Task](https://taskfile.dev/) - Task runner (can be installed via mise or standalone)

**Automatically installed via mise:**

- Go 1.23
- golangci-lint (latest)
- Node.js (for ESLint, Prettier, jscpd)
- Python 3.11+ (for MkDocs documentation)

## Setup Development Environment

```bash
# Install mise (if not already installed)
# Linux/macOS:
curl https://mise.run | sh

# Windows (PowerShell):
winget install jdx.mise
# or: choco install mise

# Install Task runner
# https://taskfile.dev/installation/

# Clone and setup
git clone https://github.com/templ-project/go.git my-project
cd my-project

# Install all dependencies
task deps:sync

# Verify setup
task validate
```

## Project Structure

```text
├── .github/
│   └── workflows/        # CI/CD pipelines
├── .husky/               # Git hooks
├── .scripts/             # Build/lint helper scripts
├── .taskfiles/           # Shared Taskfile modules
├── cmd/
│   └── cli/
│       └── main.go       # CLI application entry point
├── pkg/
│   └── greeter/
│       ├── greeter.go    # Example package
│       └── greeter_test.go # Unit tests
├── build/                # Build artifacts (gitignored)
├── docs/                 # Documentation source
├── Taskfile.yml          # Task definitions
├── .mise.toml            # Tool versions & hooks
├── go.mod                # Go module definition
├── go.sum                # Go dependency checksums
├── .golangci.yml         # golangci-lint configuration
├── package.json          # Node.js dev dependencies
└── .lintstagedrc.yml     # Staged file linting config
```

## Building

Build the project for different platforms:

```bash
# Build for current platform
task build

# Build for all platforms (Linux, macOS, Windows)
task build:all

# Build with debug symbols
task build:debug
```

Outputs to `build/`:

- `build/{os}-{arch}/` - Platform-specific binaries

## Testing

Tests use the standard Go testing framework with gotestsum for better output:

```go
// pkg/greeter/greeter_test.go
package greeter

import "testing"

func TestHello(t *testing.T) {
    got := Hello("World")
    want := "Hello, World!"
    if got != want {
        t.Errorf("Hello() = %q, want %q", got, want)
    }
}
```

Run tests:

```bash
task test                # Run with race detection
task test:coverage       # Run with coverage
task test:bench          # Run benchmarks
```

## Code Quality

### Pre-commit Hooks

The template includes automatic pre-commit validation via Husky:

- Go code formatting (gofmt)
- Go linting (golangci-lint)
- Config file formatting (Prettier)
- Config file linting (ESLint)
- Duplicate code detection

Configure in:

- `.husky/pre-commit` - Hook script
- `.lintstagedrc.yml` - File patterns and commands

### golangci-lint Configuration

The template uses a comprehensive golangci-lint configuration with 18+ linters:

| Linter        | Purpose                       |
| ------------- | ----------------------------- |
| `errcheck`    | Unchecked errors              |
| `gosimple`    | Code simplification           |
| `govet`       | Suspicious constructs         |
| `ineffassign` | Ineffectual assignments       |
| `staticcheck` | Static analysis               |
| `gosec`       | Security issues               |
| `bodyclose`   | Unclosed HTTP response bodies |
| `dupl`        | Code duplication              |
| `gocyclo`     | Cyclomatic complexity         |
| `gofmt`       | Formatting                    |
| `misspell`    | Spelling mistakes             |
| `unconvert`   | Unnecessary type conversions  |
| ...           | And more                      |

Configure in `.golangci.yml`.

## Configuration

| File                  | Purpose                                          |
| --------------------- | ------------------------------------------------ |
| `.mise.toml`          | Tool versions (Go, golangci-lint, Node, Python)  |
| `Taskfile.yml`        | Task definitions                                 |
| `go.mod`              | Go module and dependencies                       |
| `.golangci.yml`       | golangci-lint configuration                      |
| `eslint.config.mjs`   | ESLint config (uses `@templ-project/eslint`)     |
| `prettier.config.mjs` | Prettier config (uses `@templ-project/prettier`) |
| `.jscpd.json`         | Duplicate detection settings                     |

## Using as a Library

```go
package main

import (
    "fmt"
    "github.com/templ-project/go/pkg/greeter"
)

func main() {
    message := greeter.Hello("World")
    fmt.Println(message) // "Hello, World!"

    // Or use the Greeter struct
    g := greeter.New()
    fmt.Println(g.Hello("Go")) // "Hello, Go!"
}
```

## CI/CD Pipeline

The GitHub Actions pipeline runs on **Linux, macOS, and Windows**:

| Workflow         | Trigger                 | Jobs                                |
| ---------------- | ----------------------- | ----------------------------------- |
| `ci.yml`         | Push/PR to main/develop | Matrix orchestrator                 |
| `ci.quality.yml` | Called by ci.yml        | lint, test, build, duplicate-check  |
| `ci.version.yml` | Push to main            | Semantic version bump               |
| `ci.release.yml` | After version bump      | Create GitHub release with binaries |

**Release artifacts:**

- Linux binaries (amd64, arm64)
- macOS binaries (amd64, arm64)
- Windows binaries (amd64)

## License

MIT © [Templ Project](https://github.com/templ-project)

## Support

- [Report Issues](https://github.com/templ-project/go/issues)
- [Read the Docs](https://github.com/templ-project/go#readme)
- [Star on GitHub](https://github.com/templ-project/go)
