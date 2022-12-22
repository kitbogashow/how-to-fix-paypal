import re
from data import invoice_lines

matches = sum(
    1
    for line in invoice_lines
    if re.search(r'([0-9]{3,}|call|contact|\+1)', line)
)

if __name__ == '__main__':
    print(f'Matched {str(matches)} / {str(len(invoice_lines))}')
