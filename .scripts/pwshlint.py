#!/usr/bin/env python3
"""PSScriptAnalyzer linter wrapper for PowerShell scripts.

This script provides a Python interface to PSScriptAnalyzer with consistent
output formatting and optional auto-fix support.
"""

import os
import shutil
import subprocess
import sys

# Add the current directory to sys.path to allow importing pylib
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from pylib.linter import Colors, Linter  # noqa: E402  # pylint: disable=wrong-import-position


class PwshLinter(Linter):
    """Linter for PowerShell scripts using PSScriptAnalyzer."""

    def __init__(self):
        """Initialize the PSScriptAnalyzer linter."""
        super().__init__("PSScriptAnalyzer", "**/*.ps1")

    def check_installed(self) -> None:
        """Verify that PowerShell and PSScriptAnalyzer are installed."""
        if not shutil.which("pwsh"):
            print(
                f"{Colors.RED}[FAIL] PowerShell (pwsh) is not installed{Colors.RESET}"
            )
            sys.exit(2)

        self._ensure_psscriptanalyzer()

    def _ensure_psscriptanalyzer(self) -> None:
        """Ensure PSScriptAnalyzer module is installed."""
        check_cmd = "Get-Module -ListAvailable -Name PSScriptAnalyzer"
        result = subprocess.run(
            ["pwsh", "-Command", check_cmd],
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode != 0 or not result.stdout.strip():
            print(f"{Colors.YELLOW}Installing PSScriptAnalyzer...{Colors.RESET}")
            install_cmd = (
                "Install-Module -Name PSScriptAnalyzer -Force "
                "-Scope CurrentUser -SkipPublisherCheck -ErrorAction Stop"
            )
            install_res = subprocess.run(
                ["pwsh", "-Command", install_cmd],
                capture_output=True,
                text=True,
                check=False,
            )
            if install_res.returncode != 0:
                print(
                    f"{Colors.RED}[FAIL] Failed to install PSScriptAnalyzer: "
                    f"{install_res.stderr}{Colors.RESET}"
                )
                sys.exit(2)
            print(
                f"{Colors.GREEN}[OK] PSScriptAnalyzer installed successfully{Colors.RESET}"
            )

    def _get_settings_arg(self) -> str:
        """Get the settings file argument if it exists.

        Returns:
            Settings argument string or empty string.
        """
        root_dir = os.path.dirname(SCRIPT_DIR)
        settings_file = os.path.join(root_dir, ".PSScriptAnalyzerSettings.psd1")
        if os.path.exists(settings_file):
            return f"-Settings '{settings_file}'"
        return ""

    def lint_file(self, file_path: str, fix: bool) -> bool:
        """Lint a PowerShell script using PSScriptAnalyzer.

        Args:
            file_path: Path to the PowerShell script to lint.
            fix: Whether to attempt automatic fixes.

        Returns:
            True if issues were found, False otherwise.
        """
        settings_arg = self._get_settings_arg()

        if fix:
            self._try_fix(file_path, settings_arg)

        # Check for issues
        cmd = (
            f"Invoke-ScriptAnalyzer -Path '{file_path}' {settings_arg} "
            "-ErrorAction SilentlyContinue | "
            "Format-Table -Property Line, Severity, RuleName, Message -AutoSize | "
            "Out-String -Width 4096"
        )

        result = subprocess.run(
            ["pwsh", "-Command", cmd],
            capture_output=True,
            text=True,
            check=False,
        )

        output = result.stdout.strip()
        if result.returncode == 0 and output:
            print(f"{Colors.WHITE}{file_path}{Colors.RESET}")
            print(output)
            return True

        print(f"{Colors.GRAY}  OK: {file_path}{Colors.RESET}")
        return False

    def _try_fix(self, file_path: str, settings_arg: str) -> None:
        """Attempt to apply PSScriptAnalyzer fixes.

        Args:
            file_path: Path to the file to fix.
            settings_arg: Settings file argument string.
        """
        cmd = (
            f"Invoke-ScriptAnalyzer -Path '{file_path}' -Fix {settings_arg} "
            "-ErrorAction SilentlyContinue"
        )

        try:
            subprocess.run(
                ["pwsh", "-Command", cmd],
                capture_output=True,
                text=True,
                check=False,
            )
        except OSError as exc:
            print(
                f"{Colors.YELLOW}  Warning: Error during fix for {file_path}: "
                f"{exc}{Colors.RESET}"
            )


if __name__ == "__main__":
    PwshLinter().run()
