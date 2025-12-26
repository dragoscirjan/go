#!/usr/bin/env bash
#
# Creates distribution archives from built binaries.
#
# Usage:
#   ./build-dist.sh [project_name] [build_dir] [dist_dir]
#
# Arguments:
#   project_name - The project name prefix for binaries (default: go-template)
#   build_dir    - The directory containing built binaries (default: build)
#   dist_dir     - The output directory for archives (default: dist)
#

set -euo pipefail

PROJECT_NAME="${1:-go-template}"
BUILD_DIR="${2:-build}"
DIST_DIR="${3:-dist}"

# Create dist directory if it doesn't exist
mkdir -p "$DIST_DIR"

# Find all binaries matching the project name pattern
shopt -s nullglob
binaries=("$BUILD_DIR/${PROJECT_NAME}_"*)
shopt -u nullglob

if [ ${#binaries[@]} -eq 0 ]; then
    echo "No binaries found matching pattern '${PROJECT_NAME}_*' in $BUILD_DIR"
    exit 0
fi

for binary in "${binaries[@]}"; do
    [ -f "$binary" ] || continue
    
    filename=$(basename "$binary")
    # Remove .exe extension for archive name if present
    name="${filename%.exe}"
    
    if [[ "$binary" == *"windows"* ]]; then
        # Create .zip for Windows binaries
        archive_path="$DIST_DIR/${name}.zip"
        zip -j "$archive_path" "$binary"
        echo "Created: $archive_path"
    else
        # Create .tar.gz for Unix binaries
        archive_path="$DIST_DIR/${name}.tar.gz"
        tar -czf "$archive_path" -C "$BUILD_DIR" "$filename"
        echo "Created: $archive_path"
    fi
done

echo "Distribution archives created in $DIST_DIR"
