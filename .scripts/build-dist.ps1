<#
.SYNOPSIS
    Creates distribution archives from built binaries (Windows only).

.DESCRIPTION
    This script creates .zip archives for Windows binaries in the build/ directory.
    For Unix binaries, use build-dist.sh instead.

.PARAMETER ProjectName
    The project name prefix for binaries (default: go-template)

.PARAMETER BuildDir
    The directory containing built binaries (default: build)

.PARAMETER DistDir
    The output directory for archives (default: dist)

.EXAMPLE
    .\build-dist.ps1
    .\build-dist.ps1 -ProjectName "myapp" -BuildDir "build" -DistDir "dist"
#>

param(
    [string]$ProjectName = "go-template",
    [string]$BuildDir = "build",
    [string]$DistDir = "dist"
)

$ErrorActionPreference = "Stop"

# Create dist directory if it doesn't exist
if (-not (Test-Path $DistDir)) {
    New-Item -ItemType Directory -Force -Path $DistDir | Out-Null
}

# Find all Windows binaries matching the project name pattern
$binaries = Get-ChildItem -Path $BuildDir -Filter "${ProjectName}_windows_*" -File -ErrorAction SilentlyContinue

if (-not $binaries -or $binaries.Count -eq 0) {
    Write-Host "No Windows binaries found matching pattern '${ProjectName}_windows_*' in $BuildDir"
    exit 0
}

foreach ($binary in $binaries) {
    $binaryPath = $binary.FullName
    $binaryName = $binary.Name
    
    # Remove .exe extension for archive name
    $archiveName = $binaryName -replace '\.exe$', ''
    $archivePath = Join-Path $DistDir "${archiveName}.zip"
    
    # Remove existing archive if present
    if (Test-Path $archivePath) {
        Remove-Item $archivePath -Force
    }
    
    Compress-Archive -Path $binaryPath -DestinationPath $archivePath -Force
    Write-Host "Created: $archivePath"
}

Write-Host "Distribution archives created in $DistDir"
