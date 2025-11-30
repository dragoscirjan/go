# Contributing to Generic Template

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## Pull Requests

Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code passes formatting and linting checks.
6. Issue that pull request!

## Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/generic.git
cd generic

# Install dependencies
npm install

# Install mise for toolchain management (optional but recommended)
curl https://mise.run | sh
mise install

# Run validation to ensure everything works
task validate
```

## Code Style

We use several tools to maintain code quality across multiple languages:

### ESLint (JSON/YAML)

- Configuration: `package.json` devDependencies
- Run: `task lint:eslint` or `npx eslint --fix "./**/*.{json,yaml,yml}"`
- Check: `task lint:check:eslint`

### Prettier (JSON/YAML)

- Configuration: Uses `@templ-project/prettier` preset
- Run: `task format` or `npx prettier --write "./**/*.{json,yaml,yml}"`
- Check: `task format:check`

### ShellCheck (Shell Scripts)

- Run: `task lint:shellcheck` or `./.scripts/lint-shellcheck.sh --fix`
- Check: `./.scripts/lint-shellcheck.sh`
- Configuration: `.shellcheckrc`

### PSScriptAnalyzer (PowerShell Scripts)

- Run: `task lint:powershell` or `./.scripts/lint-powershell.ps1 -Fix`
- Check: `./.scripts/lint-powershell.ps1`
- Configuration: `.PSScriptAnalyzerSettings.psd1`

## Quality Gates

Before submitting a PR, ensure:

```bash
# Run all quality checks
task validate

# This runs:
# - task format        (Format code)
# - task clean         (Clean artifacts)
# - task build         (Build project)
# - task lint          (Lint all code)
# - task run           (Run smoke test)
# - task test          (Run tests)
```

## File Structure

```
.github/
├── actions/          # Custom GitHub Actions
├── ISSUE_TEMPLATE/   # Issue templates
├── prompts/          # AI prompt templates
├── scripts/          # CI/CD helper scripts
└── workflows/        # GitHub Actions workflows (to be added)
.scripts/
├── lint-shellcheck.sh      # Shell linting script
├── lint-powershell.ps1     # PowerShell linting script
├── release-tag.ps1         # Release tagging script
└── dependency-checker.ps1  # Dependency checker
.cwai/
└── templates/
    └── stack.md      # Stack-specific rules and guidelines
```

## Naming Conventions

### Files

- Use kebab-case for most files: `my-file.sh`, `my-config.yml`
- PowerShell scripts: `My-Script.ps1` (PascalCase with `-` separator)
- Configuration files: `.filename` or `filename.config.ext`

### Scripts

- Shell scripts: Use lowercase with hyphens
- PowerShell scripts: Use PascalCase with hyphens
- Make scripts executable: `chmod +x script-name.sh`

## Documentation

### Inline Comments

- Use comments to explain "why", not "what"
- Document complex logic and edge cases
- Include examples for non-obvious usage

### Markdown Documentation

All markdown files should:

- Use proper heading hierarchy
- Include table of contents for long documents
- Use code blocks with language identifiers
- Include examples where applicable

### Shell Scripts

Use the standard header format:

```bash
#!/usr/bin/env bash
# Brief description of what the script does
#
# Usage:
#   script-name.sh [options]
#
# Options:
#   --option   Description
#
# Exit codes:
#   0 - Success
#   1 - Error description
```

### PowerShell Scripts

Use the standard header format:

```powershell
#!/usr/bin/env pwsh
# Brief description of what the script does
#
# Usage:
#   script-name.ps1 [-Option]
#
# Options:
#   -Option   Description
#
# Exit codes:
#   0 - Success
#   1 - Error description
```

## Testing Guidelines

Since this is a template project, testing focuses on:

### Script Testing

1. **Smoke Tests**: Ensure scripts run without errors
2. **Lint Tests**: Verify code passes all linters
3. **Integration Tests**: Test with real repositories

### Validation Process

```bash
# Test linting scripts
./.scripts/lint-shellcheck.sh
./.scripts/lint-powershell.ps1

# Test with --fix flag
./.scripts/lint-shellcheck.sh --fix
./.scripts/lint-powershell.ps1 -Fix

# Test staged files mode
git add some-file.sh
./.scripts/lint-shellcheck.sh --staged
```

## Stack-Specific Contributions

When adding support for a new language/stack:

1. **Update `.cwai/templates/stack.md`**:
   - Add language-specific rules
   - Include style guide references
   - Document required tools
   - Add testing requirements

2. **Add Configuration Files**:
   - Linter configs (e.g., `.eslintrc`, `clippy.toml`)
   - Formatter configs (e.g., `.prettierrc`, `rustfmt.toml`)
   - Test configs (e.g., `vitest.config.js`, `jest.config.js`)

3. **Update Taskfile.yml**:
   - Add language-specific tasks
   - Include build, test, lint, format tasks
   - Document task usage

4. **Add Documentation**:
   - Update main README.md
   - Add examples if needed
   - Document dependencies

## Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new feature
fix: fix bug description
docs: update documentation
style: formatting changes
refactor: code refactoring
test: add or update tests
chore: maintenance tasks
ci: CI/CD changes
```

Examples:

```
feat: add PowerShell linting support
fix: shellcheck script now handles spaces in paths
docs: update CONTRIBUTING.md with testing guidelines
chore: update dependencies to latest versions
ci: add GitHub Actions workflow for validation
```

## Issue Reporting

### Bug Reports

Include:

- Operating system (Windows, Linux, macOS)
- Shell version (bash, zsh, pwsh)
- Tool versions (mise, task, npm, etc.)
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages/logs

### Feature Requests

Include:

- Problem statement (what need does this solve?)
- Proposed solution
- Use case examples
- Impact on existing functionality
- Implementation considerations

## Adding New Languages

When proposing support for a new language:

1. Open an issue describing the language and use case
2. Discuss tooling requirements (compiler, linter, formatter, test runner)
3. Provide example project structure
4. Include quality gates and best practices
5. Reference official style guides

## Continuous Integration

When adding CI/CD workflows:

1. Place in `.github/workflows/`
2. Use descriptive names: `ci-<language>.yml`
3. Include all quality checks
4. Support multiple platforms (Linux, macOS, Windows) where applicable
5. Use caching for dependencies
6. Document required secrets/variables

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Code of Conduct

- Be respectful and constructive
- Welcome newcomers and help them get started
- Focus on what is best for the community
- Show empathy towards other community members

## Questions?

- Open an issue for questions about contributing
- Check existing issues and PRs for similar discussions
- Reach out to maintainers via GitHub discussions

## Additional Resources

- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)

---

Thank you for contributing! 🎉
