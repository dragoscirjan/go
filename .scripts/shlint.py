#!/usr/bin/env python3
"""ShellCheck linter wrapper for shell scripts.

This script provides a Python interface to shellcheck with consistent
output formatting and optional auto-fix support via git apply.
"""

import os
import shutil
import subprocess
import sys

# Add the current directory to sys.path to allow importing pylib
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from pylib.linter import Colors, Linter  # noqa: E402  # pylint: disable=wrong-import-position


class ShellLinter(Linter):
    """Linter for shell scripts using ShellCheck."""

    def __init__(self):
        """Initialize the ShellCheck linter."""
        super().__init__("ShellCheck", "**/*.sh")

    def check_installed(self) -> None:
        """Verify that ShellCheck is installed."""
        if not shutil.which("shellcheck"):
            print(f"{Colors.RED}[FAIL] ShellCheck is not installed{Colors.RESET}")
            print("Install it: https://github.com/koalaman/shellcheck#installing")
            sys.exit(2)

    def lint_file(self, file_path: str, fix: bool) -> bool:
        """Lint a shell script using ShellCheck.

        Args:
            file_path: Path to the shell script to lint.
            fix: Whether to attempt automatic fixes via git apply.

        Returns:
            True if issues were found, False otherwise.
        """
        if fix:
            self._try_fix(file_path)

        result = subprocess.run(
            ["shellcheck", "-x", "--severity=style", "--format=tty", file_path],
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode != 0 and result.stdout.strip():
            print(f"{Colors.WHITE}{file_path}{Colors.RESET}")
            print(result.stdout)
            return True

        print(f"{Colors.GRAY}  OK: {file_path}{Colors.RESET}")
        return False

    def _try_fix(self, file_path: str) -> None:
        """Attempt to apply ShellCheck fixes via git apply.

        Args:
            file_path: Path to the file to fix.
        """
        try:
            result = subprocess.run(
                [
                    "shellcheck",
                    "-x",
                    "--severity=style",
                    "--format=diff",
                    file_path,
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            if result.stdout:
                apply_process = subprocess.run(
                    ["git", "apply", "--allow-empty"],
                    input=result.stdout,
                    text=True,
                    capture_output=True,
                    check=False,
                )

                if apply_process.returncode == 0:
                    print(f"{Colors.WHITE}  Fixed: {file_path}{Colors.RESET}")
                else:
                    print(
                        f"{Colors.YELLOW}  Warning: Could not apply fixes "
                        f"to {file_path}{Colors.RESET}"
                    )
                    print(apply_process.stderr)

        except OSError as exc:
            print(
                f"{Colors.YELLOW}  Warning: Error during fix for {file_path}: "
                f"{exc}{Colors.RESET}"
            )


if __name__ == "__main__":
    ShellLinter().run()
