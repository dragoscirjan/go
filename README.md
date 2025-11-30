# Go Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/templ-project/go/issues)
[![Go Report Card](https://goreportcard.com/badge/github.com/templ-project/go)](https://goreportcard.com/report/github.com/templ-project/go)

> A modern, cross-platform Go project template with comprehensive tooling, linting, and quality checks built-in.

- [Go Template](#go-template)
  - [Quick Start](#quick-start)
  - [What's Included](#whats-included)
  - [Common Commands](#common-commands)
  - [Requirements](#requirements)
  - [Setup Development Environment](#setup-development-environment)
  - [Project Structure](#project-structure)
  - [Pre-commit Hooks](#pre-commit-hooks)
  - [Configuration](#configuration)
  - [License](#license)
  - [Support](#support)

## Quick Start

**Clone and setup:**

```bash
# Clone the repository
git clone https://github.com/templ-project/go.git my-go-project
cd my-go-project

# Install development tools
mise install

# Install dependencies
task deps:sync

# Build the project
task build

# Run the application
task run
```

That's it! You now have a fully configured Go project with linting, formatting, testing, and quality tools.

## What's Included

- ✅ **Go 1.23** - Modern Go toolchain
- ✅ **Task Runner** - Modern [Taskfile](https://taskfile.dev/) for build automation
- ✅ **Tool Management** - [mise](https://mise.jdx.dev/) for development environment
- ✅ **Go Linting** - golangci-lint with comprehensive checks
- ✅ **Code Formatting** - gofmt + Prettier for Go and config files
- ✅ **Testing** - Built-in test framework with coverage reports
- ✅ **Benchmarking** - Performance testing support
- ✅ **Pre-commit Hooks** - Husky + lint-staged for automatic validation
- ✅ **Duplicate Detection** - jscpd with badge generation
- ✅ **Documentation** - MkDocs with Material theme + godoc
- ✅ **Cross-Platform** - Works on Linux, macOS, and Windows

## Common Commands

```bash
# Building
task build               # Build the project
task build:all           # Build for all platforms (Linux, macOS, Windows)
task clean               # Clean build artifacts

# Code formatting
task format              # Format all code (gofmt, prettier)
task format:check        # Check formatting without fixing

# Linting
task lint                # Lint all code (golangci-lint, eslint)
task lint:check          # Check all without fixing

# Testing
task test                # Run tests with race detection and coverage
task test:gen-coverage   # Generate HTML coverage report
task test:bench          # Run benchmark tests

# Development
task run                 # Build and run the application
task debug               # Run with delve debugger

# Code quality
task duplicate-check     # Check for duplicate code

# Documentation
task docs                # Build documentation
task docs:serve          # Serve documentation locally
task docs:godoc          # Start godoc server

# Full validation
task validate            # Run complete CI pipeline
```

## Requirements

- [mise](https://mise.jdx.dev/) - For tool version management
- [Task](https://taskfile.dev/) - Task runner (installed via mise)
- [Go 1.23+](https://go.dev/) - Go toolchain (installed via mise)
- [golangci-lint](https://golangci-lint.run/) - Go linter (installed via mise)
- [Node.js](https://nodejs.org/) - For config file linting (installed via mise)

## Setup Development Environment

```bash
# Install mise (if not already installed)
curl https://mise.run | sh

# Install all required tools
mise install

# Install Node.js dependencies
mise exec -- npm install

# Install Python dependencies (for docs)
mise exec -- task uv:sync

# Install pre-commit hooks
mise exec -- npx husky install
```

## Project Structure

```text
.github/                 # GitHub templates and workflows
.husky/                  # Git hooks
cmd/                     # Application entry points
  └── cli/               # CLI application
      └── main.go
pkg/                     # Public packages
  └── greeter/           # Example greeter package
      ├── greeter.go
      └── greeter_test.go
docs/                    # Documentation source
build/                   # Build artifacts (gitignored)
Taskfile.yml             # Task definitions
go.mod                   # Go module definition
.mise.toml               # Tool versions
.golangci.yml            # golangci-lint configuration
.lintstagedrc.yml        # Staged file linting config
```

## Pre-commit Hooks

The template includes automatic pre-commit validation via Husky:

- Go code formatting (gofmt)
- Go linting (golangci-lint)
- Config file formatting (Prettier)
- Linting (ESLint)
- Duplicate code detection

Configure what runs in [.lintstagedrc.yml](.lintstagedrc.yml) and [.husky/pre-commit](.husky/pre-commit).

## Configuration

All configuration uses shared packages and standard tools:

- **Go**: Standard toolchain (gofmt, go test, go build)
- **golangci-lint**: `.golangci.yml`
- **ESLint**: `@templ-project/eslint`
- **Prettier**: `@templ-project/prettier`

## License

MIT © [Templ Project](https://github.com/templ-project)

## Support

- 🐛 [Report Issues](https://github.com/templ-project/go/issues)
- 📖 [Read the Docs](https://github.com/templ-project/go#readme)
- ⭐ [Star on GitHub](https://github.com/templ-project/go)
