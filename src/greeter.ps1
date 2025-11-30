#!/usr/bin/env pwsh
# Greeter module - demonstrates functional design following PowerShell best practices.
#
# Provides greeting and farewell functionality using pure functions.
# Follows Microsoft PowerShell Best Practices.
#
# This is a library module meant to be dot-sourced, not executed directly.

<#
.SYNOPSIS
Creates a greeting message for the specified name.

.DESCRIPTION
Validates input and returns a formatted greeting message.
Throws an error if the name is empty or null.

.PARAMETER Name
The name to greet (required, non-empty string)

.OUTPUTS
System.String - The greeting message

.EXAMPLE
Hello -Name "World"
# Output: Hello, World!

.EXAMPLE
Hello "World"
# Output: Hello, World!
#>
function Hello {
  [CmdletBinding()]
  [OutputType([string])]
  param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateNotNullOrEmpty()]
    [string]$Name
  )

  # Trim whitespace and create greeting
  $trimmedName = $Name.Trim()
  return "Hello, ${trimmedName}!"
}

<#
.SYNOPSIS
Creates a farewell message for the specified name.

.DESCRIPTION
Validates input and returns a formatted farewell message.
Throws an error if the name is empty or null.

.PARAMETER Name
The name to bid farewell (required, non-empty string)

.OUTPUTS
System.String - The farewell message

.EXAMPLE
Goodbye -Name "World"
# Output: Goodbye, World!

.EXAMPLE
Goodbye "World"
# Output: Goodbye, World!
#>
function Goodbye {
  [CmdletBinding()]
  [OutputType([string])]
  param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateNotNullOrEmpty()]
    [string]$Name
  )

  # Trim whitespace and create farewell
  $trimmedName = $Name.Trim()
  return "Goodbye, ${trimmedName}!"
}
