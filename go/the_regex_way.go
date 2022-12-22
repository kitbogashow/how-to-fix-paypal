package main

import (
	"bufio"
	"os"
	"regexp"
)

func main() {

	matches := 0

	// open invoices.txt
	invoices, err := os.Open("../invoices.txt")
	if err != nil {
		panic(err)
	}
	defer invoices.Close()

	// read the file line by line
	var messages []string
	scanner := bufio.NewScanner(invoices)
	for scanner.Scan() {
		messages = append(messages, scanner.Text())
	}

	// compile the regex and check each message for a match
	regex := regexp.MustCompile(`([0-9]{3,}|call|contact|\+1)`)
	for _, message := range messages {
		if regex.MatchString(message) {
			matches++
		}
	}

	// print the number of matches
	println(matches)

}
