# Generic Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/templ-project/generic/issues)

> A modern, cross-platform project template with comprehensive tooling, linting, and quality checks built-in.

- [Generic Template](#generic-template)
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

**Bootstrap a new project:**

Bootstrap in current directory

```bash
uvx --from git+https://github.com/templ-project/generic.git bootstrap .
```

Bootstrap in specific directory

```bash
uvx --from git+https://github.com/templ-project/generic.git bootstrap ./my-project
```

Bootstrap with custom project name

```bash
uvx --from git+https://github.com/templ-project/generic.git bootstrap --project-name my-awesome-project ./target-dir
```

**After bootstrapping:**

```bash
cd my-project
git init
git add .
git commit -m "Initial commit"
mise install
npm install
```

That's it! You now have a fully configured project with linting, formatting, and quality tools.

## What's Included

- ✅ **Task Runner** - Modern [Taskfile](https://taskfile.dev/) for build automation
- ✅ **Tool Management** - [mise](https://mise.jdx.dev/) for development environment
- ✅ **Shell Linting** - ShellCheck with auto-fix support
- ✅ **PowerShell Linting** - PSScriptAnalyzer with cross-platform support
- ✅ **Code Formatting** - Prettier + ESLint for JSON/YAML/Markdown
- ✅ **Pre-commit Hooks** - Husky + lint-staged for automatic validation
- ✅ **Duplicate Detection** - jscpd with badge generation
- ✅ **Documentation** - MkDocs with Material theme
- ✅ **Cross-Platform** - Works on Linux, macOS, and Windows/WSL

## Common Commands

```bash
# Code formatting
task format              # Format all code (prettier)
task format:check        # Check formatting without fixing

# Linting
task lint                # Lint all code (md, json, yaml, shellcheck, powershell)
task lint:check          # Check all without fixing

# Code quality
task duplicate-check     # Check for duplicate code

# Documentation
task docs                # Build documentation
task docs:serve          # Serve documentation locally
task docs:deploy         # Deploy to GitHub Pages

# Full validation
task validate            # Run complete CI pipeline
```

## Requirements

- [mise](https://mise.jdx.dev/) - For tool version management
- [Task](https://taskfile.dev/) - Task runner (installed via mise)
- [Node.js](https://nodejs.org/) - For linting tools (installed via mise)
- [PowerShell Core](https://github.com/PowerShell/PowerShell) - For cross-platform scripting (installed via mise)

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
.scripts/                # Linting scripts
  ├── lint-shellcheck.sh
  └── lint-powershell.ps1
_uvx_install/            # Bootstrap script (auto-removed after install)
docs/                    # Documentation source
Taskfile.yml             # Task definitions
.mise.toml               # Tool versions
.lintstagedrc.yml        # Staged file linting config
```

## Pre-commit Hooks

The template includes automatic pre-commit validation via Husky:

- Code formatting (Prettier)
- Linting (ESLint, ShellCheck, PowerShell)
- Duplicate code detection

Configure what runs in [.lintstagedrc.yml](.lintstagedrc.yml) and [.husky/pre-commit](.husky/pre-commit).

## Configuration

All configuration uses shared packages for consistency:

- **ESLint**: `@templ-project/eslint`
- **Prettier**: `@templ-project/prettier`
- **ShellCheck**: `.shellcheckrc`
- **PSScriptAnalyzer**: `.PSScriptAnalyzerSettings.psd1`

## License

MIT © [Templ Project](https://github.com/templ-project)

## Support

- 🐛 [Report Issues](https://github.com/templ-project/generic/issues)
- 📖 [Read the Docs](https://github.com/templ-project/generic#readme)
- ⭐ [Star on GitHub](https://github.com/templ-project/generic)
