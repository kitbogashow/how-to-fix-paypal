from pathlib import Path

# open the example text file and read each line
invoice_lines = (Path(__file__).parent.parent / 'invoices.txt').read_text(encoding="utf-8").splitlines()
