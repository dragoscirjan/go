#!/usr/bin/env bash
# Greeter module - demonstrates functional design following Bash best practices.
#
# Provides greeting and farewell functionality using pure functions.
# Follows Google Shell Style Guide.
#
# This is a library module meant to be sourced, not executed directly.

# Creates a greeting message for the specified name.
#
# Arguments:
#   $1 - The name to greet (required, non-empty string)
#
# Outputs:
#   Writes greeting message to stdout
#
# Returns:
#   0 on success
#   1 on error (empty/missing name)
#
# Example:
#   hello "World"
#   # Output: Hello, World!
hello() {
  local name="${1:-}"

  # Validate input
  if [[ -z "${name}" ]]; then
    echo "Error: Name must be a non-empty string" >&2
    return 1
  fi

  # Trim whitespace and create greeting
  name="$(echo "${name}" | xargs)"
  echo "Hello, ${name}!"
}

# Creates a farewell message for the specified name.
#
# Arguments:
#   $1 - The name to bid farewell (required, non-empty string)
#
# Outputs:
#   Writes farewell message to stdout
#
# Returns:
#   0 on success
#   1 on error (empty/missing name)
#
# Example:
#   goodbye "World"
#   # Output: Goodbye, World!
goodbye() {
  local name="${1:-}"

  # Validate input
  if [[ -z "${name}" ]]; then
    echo "Error: Name must be a non-empty string" >&2
    return 1
  fi

  # Trim whitespace and create farewell
  name="$(echo "${name}" | xargs)"
  echo "Goodbye, ${name}!"
}

# Main execution (only when sourced or run directly)
# Demonstrates usage of the functions
main() {
  if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Script is being executed directly
    if [[ $# -eq 0 ]]; then
      echo "Usage: ${0} <name>" >&2
      echo "" >&2
      echo "Examples:" >&2
      echo "  ${0} World" >&2
      echo "  ${0} 'John Doe'" >&2
      exit 1
    fi

    # Demonstrate both functions
    hello "${1}"
    goodbye "${1}"
  fi
}

# Run main if executed directly (not sourced)
main "$@"
