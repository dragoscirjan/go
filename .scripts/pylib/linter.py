"""Abstract base class for linter implementations.

This module provides a common interface and utilities for building
file linters with consistent behavior and output formatting.
"""

import argparse
import sys
from abc import ABC, abstractmethod

from .file_finder import find_files


class Colors:
    """ANSI color codes for terminal output."""

    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    GRAY = "\033[90m"
    WHITE = "\033[37m"


class Linter(ABC):
    """Abstract base class for file linters.

    Provides common argument parsing, file discovery, and result reporting.
    Subclasses must implement check_installed() and lint_file().
    """

    def __init__(self, name: str, default_pattern: str):
        """Initialize the linter.

        Args:
            name: The name of the linter (for display purposes).
            default_pattern: Default glob pattern for finding files.
        """
        self.name = name
        self.default_pattern = default_pattern
        self.parser = argparse.ArgumentParser(description=f"Lint {name} files")
        self.parser.add_argument(
            "--fix", action="store_true", help="Apply fixes automatically"
        )
        self.parser.add_argument(
            "files", nargs="*", help="Files or glob patterns to lint"
        )
        self.parser.add_argument("--ignore", action="append", help="Patterns to ignore")

    @abstractmethod
    def check_installed(self) -> None:
        """Verify that the linter tool is installed.

        Should exit with code 2 if the tool is not available.
        """

    @abstractmethod
    def lint_file(self, file_path: str, fix: bool) -> bool:
        """Lint a single file.

        Args:
            file_path: Path to the file to lint.
            fix: Whether to apply automatic fixes.

        Returns:
            True if issues were found (and not fixed), False otherwise.
        """

    def run(self) -> None:
        """Run the linter on files matching the configured patterns.

        Parses command-line arguments, discovers files, runs the linter on each,
        and exits with appropriate status code.
        """
        args = self.parser.parse_args()
        self.check_installed()

        patterns = args.files
        if not patterns:
            patterns = [self.default_pattern]

        files = find_files(patterns, args.ignore)

        if not files:
            print(f"{Colors.YELLOW}No {self.name} files found to lint{Colors.RESET}")
            sys.exit(0)

        print(f"{self.name}: Linting files...")
        print("")

        has_issues = False
        file_count = 0

        for file_path in files:
            file_count += 1
            if self.lint_file(file_path, args.fix):
                has_issues = True

        print("")
        print(f"Checked {file_count} file(s)")

        if has_issues:
            if args.fix:
                print("")
                print(
                    f"{Colors.YELLOW}[WARN] Some issues could not be auto-fixed{Colors.RESET}"
                )
                print("Please review and fix them manually")
                sys.exit(1)
            else:
                print(f"{Colors.RED}[FAIL] {self.name} found issues{Colors.RESET}")
                print("Run with --fix to apply automatic fixes")
                sys.exit(1)
        else:
            print(f"{Colors.GREEN}[OK] All files are clean{Colors.RESET}")
            sys.exit(0)
