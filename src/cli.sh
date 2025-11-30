#!/usr/bin/env bash
# CLI tool - demonstrates the greeter functionality.
#
# Usage:
#   cli.sh <name>
#
# Example:
#   cli.sh World
#   cli.sh "John Doe"

set -euo pipefail

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Source the greeter library
# shellcheck source=greeter.sh
source "${SCRIPT_DIR}/greeter.sh"

# Main function that demonstrates the template functionality.
# Calls the hello function from the greeter module and displays the result.
main() {
  hello "World"
}

# Run main
main
