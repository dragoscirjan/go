#!/usr/bin/env pwsh
<#
.SYNOPSIS
Fix mise PowerShell installation by re-extracting with proper directory structure.

.DESCRIPTION
Mise's GitHub release extraction loses the Modules/ folder structure.
This script re-downloads and extracts PowerShell properly.
#>

$ErrorActionPreference = 'Stop'

# Get the PowerShell install path from mise
try {
  $PwshPath = (mise where github:PowerShell/PowerShell 2>$null)
  if (-not $PwshPath) {
    [Console]::WriteLine("PowerShell not installed via mise, skipping fix")
    exit 0
  }
}
catch {
  [Console]::WriteLine("PowerShell not installed via mise, skipping fix")
  exit 0
}

# Check if Modules folder already exists
$ModulesPath = Join-Path $PwshPath "Modules"
if (Test-Path $ModulesPath) {
  [Console]::WriteLine("PowerShell Modules folder exists, no fix needed")
  exit 0
}

[Console]::WriteLine("Fixing PowerShell installation at: $PwshPath")

# Get version from path
$Version = Split-Path $PwshPath -Leaf

# Detect architecture
$Arch = if ([Environment]::Is64BitOperatingSystem) { "x64" } else { "x86" }

# Build download URL for Windows
$DownloadUrl = "https://github.com/PowerShell/PowerShell/releases/download/v${Version}/PowerShell-${Version}-win-${Arch}.zip"

[Console]::WriteLine("Re-downloading: $DownloadUrl")

# Create temp directory
$TempDir = Join-Path $env:TEMP "pwsh-fix-$(Get-Random)"
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

try {
  $ZipPath = Join-Path $TempDir "pwsh.zip"

  # Download (disable progress bar for speed)
  [Console]::WriteLine("Downloading...")
  $ProgressPreference = 'SilentlyContinue'
  Invoke-WebRequest -Uri $DownloadUrl -OutFile $ZipPath -UseBasicParsing

  # Backup existing installation
  $BackupPath = "${PwshPath}.bak"
  if (Test-Path $BackupPath) {
    Remove-Item -Recurse -Force $BackupPath
  }
  Rename-Item $PwshPath $BackupPath
  New-Item -ItemType Directory -Path $PwshPath -Force | Out-Null

  # Extract with proper directory structure
  [Console]::WriteLine("Extracting...")
  Add-Type -AssemblyName System.IO.Compression.FileSystem
  [System.IO.Compression.ZipFile]::ExtractToDirectory($ZipPath, $PwshPath)

  # Verify
  $NewModulesPath = Join-Path $PwshPath "Modules"
  if (Test-Path $NewModulesPath) {
    [Console]::WriteLine("PowerShell installation fixed successfully")
    Remove-Item -Recurse -Force $BackupPath
  }
  else {
    [Console]::WriteLine("Fix failed, restoring backup")
    Remove-Item -Recurse -Force $PwshPath
    Rename-Item $BackupPath $PwshPath
    exit 1
  }
}
finally {
  # Cleanup temp
  if (Test-Path $TempDir) {
    Remove-Item -Recurse -Force $TempDir
  }
}
