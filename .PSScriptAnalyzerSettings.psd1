# PSScriptAnalyzer settings for PowerShell linting
# See: https://github.com/PowerShell/PSScriptAnalyzer

@{
    # Enable all default rules
    IncludeDefaultRules = $true

    # Severity levels to include: Error, Warning, Information
    Severity = @('Error', 'Warning', 'Information')

    # Rules to exclude (adjust as needed)
    ExcludeRules = @(
        # Allow Write-Host for user-facing scripts (install scripts, build tools, etc.)
        'PSAvoidUsingWriteHost',
        # Disable alignment rule - too opinionated and causes conflicts
        'PSAlignAssignmentStatement'
    )

    # Custom rule configuration
    Rules = @{
        PSPlaceOpenBrace = @{
            Enable = $true
            OnSameLine = $true
            NewLineAfter = $true
            IgnoreOneLineBlock = $true
        }

        PSPlaceCloseBrace = @{
            Enable = $true
            NewLineAfter = $true
            IgnoreOneLineBlock = $true
            NoEmptyLineBefore = $false
        }

        PSUseConsistentIndentation = @{
            Enable = $true
            IndentationSize = 2
            PipelineIndentation = 'IncreaseIndentationForFirstPipeline'
            Kind = 'space'
        }

        PSUseConsistentWhitespace = @{
            Enable = $true
            CheckInnerBrace = $true
            CheckOpenBrace = $true
            CheckOpenParen = $true
            CheckOperator = $true
            CheckPipe = $true
            CheckPipeForRedundantWhitespace = $false
            CheckSeparator = $true
            CheckParameter = $false
        }

        PSAlignAssignmentStatement = @{
            Enable = $true
            CheckHashtable = $true
        }

        PSUseCorrectCasing = @{
            Enable = $true
        }
    }
}
