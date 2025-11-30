#!/usr/bin/env pwsh
# CLI tool - demonstrates the greeter functionality.
#
# Usage:
#   cli.ps1
#
# Example:
#   pwsh -File cli.ps1

$ErrorActionPreference = 'Stop'

# Get the directory where this script is located
$ScriptDir = Split-Path -Path $MyInvocation.MyCommand.Path -Parent

# Dot-source the greeter library
. "$ScriptDir/greeter.ps1"

# Main function that demonstrates the template functionality.
# Calls the Hello function from the greeter module and displays the result.
function Main {
  $message = Hello -Name "World"
  Write-Output $message
}

# Run main
Main
