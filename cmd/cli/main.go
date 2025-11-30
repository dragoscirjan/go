// Package main provides a CLI tool that demonstrates the greeter functionality.
//
// This is a simple command-line application that uses the greeter package
// to display greeting messages.
//
// Usage:
//
//	go run cmd/cli/main.go
//	# or after building:
//	./cli
package main

import (
	"fmt"
	"log"
	"os"

	"github.com/templ-project/go/pkg/greeter"
)

func main() {
	// Get name from command line arguments or use default
	name := "World"
	if len(os.Args) > 1 {
		name = os.Args[1]
	}

	// Call the hello function from the greeter package
	message, err := greeter.Hello(name)
	if err != nil {
		log.Fatalf("Error: %v\n", err)
	}

	// Display the greeting
	fmt.Println(message)
}
