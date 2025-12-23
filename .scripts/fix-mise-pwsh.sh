#!/usr/bin/env bash
# Fix mise PowerShell installation by re-extracting with proper directory structure
# This script is called by mise postinstall hook

set -euo pipefail

# Get the PowerShell install path from mise
PWSH_PATH=$(mise where github:PowerShell/PowerShell 2>/dev/null || echo "")

if [ -z "$PWSH_PATH" ]; then
  echo "PowerShell not installed via mise, skipping fix"
  exit 0
fi

# Check if Modules folder already exists (already fixed or correct extraction)
if [ -d "$PWSH_PATH/Modules" ]; then
  # Set permissions
  chmod +x "$PWSH_PATH/pwsh"
  echo "PowerShell Modules folder exists, no fix needed"
  exit 0
fi

echo "Fixing PowerShell installation at: $PWSH_PATH"

# Detect OS and architecture
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

# Get version from the path (e.g., /path/to/7.5.4)
VERSION=$(basename "$PWSH_PATH")

# Construct download URL based on OS and architecture
case "$OS-$ARCH" in
linux-x86_64) DOWNLOAD_URL="https://github.com/PowerShell/PowerShell/releases/download/v${VERSION}/powershell-${VERSION}-linux-x64.tar.gz" ;;
linux-aarch64) DOWNLOAD_URL="https://github.com/PowerShell/PowerShell/releases/download/v${VERSION}/powershell-${VERSION}-linux-arm64.tar.gz" ;;
darwin-x86_64) DOWNLOAD_URL="https://github.com/PowerShell/PowerShell/releases/download/v${VERSION}/powershell-${VERSION}-osx-x64.tar.gz" ;;
darwin-arm64) DOWNLOAD_URL="https://github.com/PowerShell/PowerShell/releases/download/v${VERSION}/powershell-${VERSION}-osx-arm64.tar.gz" ;;
*)
  echo "Unsupported OS/architecture: $OS-$ARCH"
  exit 1
  ;;
esac

echo "Re-downloading and extracting: $DOWNLOAD_URL"

# Create temp directory
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

# Download
curl -fsSL "$DOWNLOAD_URL" -o "$TEMP_DIR/pwsh.tar.gz"

# Clear existing installation (keep backup)
if [ -d "$PWSH_PATH.bak" ]; then
  rm -rf "$PWSH_PATH.bak"
fi
mv "$PWSH_PATH" "$PWSH_PATH.bak"
mkdir -p "$PWSH_PATH"

# Extract with proper directory structure
tar -xzf "$TEMP_DIR/pwsh.tar.gz" -C "$PWSH_PATH"

# Verify
if [ -d "$PWSH_PATH/Modules" ]; then
  echo "PowerShell installation fixed successfully"
  rm -rf "$PWSH_PATH.bak"
else
  echo "Fix failed, restoring backup"
  rm -rf "$PWSH_PATH"
  mv "$PWSH_PATH.bak" "$PWSH_PATH"
  exit 1
fi

# Set permissions
chmod +x "$PWSH_PATH/pwsh"
