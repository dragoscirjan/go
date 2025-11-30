// Package main demonstrates basic usage of the greeter package.
//
// This example shows how to use both Hello and Goodbye functions
// with proper error handling.
package main

import (
	"fmt"
	"log"
	"os"

	"github.com/templ-project/go/pkg/greeter"
)

func main() {
	// Get name from command line or use default
	name := "World"
	if len(os.Args) > 1 {
		name = os.Args[1]
	}

	// Call Hello function
	helloMsg, err := greeter.Hello(name)
	if err != nil {
		log.Fatalf("Error creating greeting: %v", err)
	}
	fmt.Println(helloMsg)

	// Call Goodbye function
	goodbyeMsg, err := greeter.Goodbye(name)
	if err != nil {
		log.Fatalf("Error creating farewell: %v", err)
	}
	fmt.Println(goodbyeMsg)
}
