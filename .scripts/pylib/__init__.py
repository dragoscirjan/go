"""Shared Python utilities for linting scripts.

This package provides common abstractions and utilities for building
consistent file linters.
"""

from .file_finder import find_files
from .linter import Colors, Linter

__all__ = ["Colors", "Linter", "find_files"]
