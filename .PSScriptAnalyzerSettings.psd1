# PSScriptAnalyzer settings for PowerShell linting
# See: https://github.com/PowerShell/PSScriptAnalyzer

@{
    # Enable all default rules
    IncludeDefaultRules = $true

    # Severity levels to include (alphabetically sorted)
    Severity = @('Error', 'Information', 'Warning')

    # Rules to exclude (alphabetically sorted)
    ExcludeRules = @(
        # Disable alignment rule - too opinionated and causes conflicts
        'PSAlignAssignmentStatement',
        # Allow Write-Host for user-facing scripts (install scripts, build tools, etc.)
        'PSAvoidUsingWriteHost'
    )

    # Custom rule configuration (alphabetically sorted)
    Rules = @{
        PSAlignAssignmentStatement = @{
            CheckHashtable = $true
            Enable         = $true
        }

        PSPlaceCloseBrace = @{
            Enable            = $true
            IgnoreOneLineBlock = $true
            NewLineAfter      = $true
            NoEmptyLineBefore = $false
        }

        PSPlaceOpenBrace = @{
            Enable            = $true
            IgnoreOneLineBlock = $true
            NewLineAfter      = $true
            OnSameLine        = $true
        }

        PSUseConsistentIndentation = @{
            Enable              = $true
            IndentationSize     = 2
            Kind                = 'space'
            PipelineIndentation = 'IncreaseIndentationForFirstPipeline'
        }

        PSUseConsistentWhitespace = @{
            CheckInnerBrace                 = $true
            CheckOpenBrace                  = $true
            CheckOpenParen                  = $true
            CheckOperator                   = $true
            CheckParameter                  = $false
            CheckPipe                       = $true
            CheckPipeForRedundantWhitespace = $false
            CheckSeparator                  = $true
            Enable                          = $true
        }

        PSUseCorrectCasing = @{
            Enable = $true
        }
    }
}
