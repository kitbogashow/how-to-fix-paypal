import re

lines = open('invoices.txt', 'r').readlines()
matches = 0

for line in lines:
    if re.search('([0-9]{3,}|call|contact|\\+1)', line):
        matches += 1

print('Matched ' + str(matches) + ' / ' + str(len(lines)))
