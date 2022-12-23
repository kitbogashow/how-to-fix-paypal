#!/bin/bash

count=0
while IFS= read -r line
do
  if echo $line | grep -Piq "([0-9]{3,}|call|contact|\+1)"; then
    echo "sus line found"
    let count++
  fi
done < "../invoices.txt"

echo "sus lines: $count"
