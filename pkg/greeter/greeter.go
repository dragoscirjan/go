// Package greeter provides greeting and farewell functionality.
//
// This package demonstrates functional design following Go best practices.
// It provides simple, pure functions for creating greeting messages.
package greeter

import (
	"errors"
	"strings"
)

var (
	// ErrEmptyName is returned when an empty or whitespace-only name is provided.
	ErrEmptyName = errors.New("name must be a non-empty string")
)

// Hello creates a greeting message for the specified name.
//
// The name is trimmed of leading and trailing whitespace before
// generating the greeting. If the name is empty or contains only
// whitespace, an error is returned.
//
// Example:
//
//	msg, err := Hello("World")
//	if err != nil {
//	    log.Fatal(err)
//	}
//	fmt.Println(msg) // Output: Hello, World!
func Hello(name string) (string, error) {
	// Trim whitespace
	trimmedName := strings.TrimSpace(name)

	// Validate input
	if trimmedName == "" {
		return "", ErrEmptyName
	}

	// Create greeting
	return "Hello, " + trimmedName + "!", nil
}

// Goodbye creates a farewell message for the specified name.
//
// The name is trimmed of leading and trailing whitespace before
// generating the farewell. If the name is empty or contains only
// whitespace, an error is returned.
//
// Example:
//
//	msg, err := Goodbye("World")
//	if err != nil {
//	    log.Fatal(err)
//	}
//	fmt.Println(msg) // Output: Goodbye, World!
func Goodbye(name string) (string, error) {
	// Trim whitespace
	trimmedName := strings.TrimSpace(name)

	// Validate input
	if trimmedName == "" {
		return "", ErrEmptyName
	}

	// Create farewell
	return "Goodbye, " + trimmedName + "!", nil
}
