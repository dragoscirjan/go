"""File discovery utilities for linting scripts.

This module provides functions to find files matching glob patterns
while respecting common ignore directories.
"""

import glob
import os
from typing import List, Optional, Set

DEFAULT_IGNORES = [
    "__pycache__",
    ".git",
    ".husky",
    ".venv",
    "build",
    "dist",
    "node_modules",
    "target",
    "vendor",
    "venv",
]


def is_ignored(path: str, ignore_patterns: Set[str]) -> bool:
    """Check if a path should be ignored based on directory patterns.

    Args:
        path: The file path to check.
        ignore_patterns: Set of directory names to ignore.

    Returns:
        True if any path component matches an ignore pattern.
    """
    parts = path.split(os.sep)
    for part in parts:
        if part in ignore_patterns:
            return True
    return False


def find_files(
    patterns: List[str], ignore_patterns: Optional[List[str]] = None
) -> List[str]:
    """Find files matching glob patterns while ignoring specified directories.

    Args:
        patterns: List of file paths or glob patterns to match.
        ignore_patterns: Additional directory names to ignore.

    Returns:
        Sorted list of matching file paths.
    """
    if ignore_patterns is None:
        ignore_patterns = []

    all_ignores = set(DEFAULT_IGNORES + ignore_patterns)
    found_files = set()

    if not patterns:
        return []

    for pattern in patterns:
        # If the pattern is a direct file path that exists, add it (unless ignored)
        if os.path.isfile(pattern):
            if not is_ignored(pattern, all_ignores):
                found_files.add(os.path.normpath(pattern))
            continue

        # Otherwise treat as glob
        # recursive=True allows ** to match subdirectories
        matches = glob.glob(pattern, recursive=True)

        for match in matches:
            if os.path.isfile(match) and not is_ignored(match, all_ignores):
                found_files.add(os.path.normpath(match))

    return sorted(found_files)
