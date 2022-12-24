#! /usr/bin/env swift

// Usually we compile Swift, but for fun this is written as a script.

import Foundation
import RegexBuilder

let examples = URL(fileURLWithPath: "../invoices.txt").lines
let suspicionThreshold = 1.0 // Score needed to be sufficiently suspicious.

// Using regex, but readable. See https://developer.apple.com/documentation/RegexBuilder

let phoneNumberSeparator = Optionally(.anyOf("- "))

let countryCode = Optionally {
	Optionally("+")
	OneOrMore(.digit)
}

let phoneNumber = Regex {
	countryCode
	phoneNumberSeparator
	Optionally("(")
	Repeat(.digit, 1...3)
	Optionally(")")
	phoneNumberSeparator
	Repeat(.digit, 1...3)
	phoneNumberSeparator
	Repeat(.digit, 1...4)
}

let suspiciousWordsRankings = [
	"cancel": 1,
	"refund": 1,
	"help desk": 0.5,
	"authorized": 0.5,
	"24 hours": 0.25,
	"usd": 0.1
]

for try await example in examples {
	let lowercased = example.lowercased()
	var score = suspiciousWordsRankings.reduce(0.0) { current, pair in
		guard lowercased.contains(pair.key) else { return current }
		return current + pair.value
	}

	// Phone numbers are suspicious
	if lowercased.contains(phoneNumber) {
		score += 0.5
	}

	if score > suspicionThreshold {
		print("Suspicious activity. Likely a scam ")
	}
}
