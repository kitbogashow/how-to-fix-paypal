from data import invoice_lines

"""
a way to map certain keyword or phrases with a "score" of how "bad" they are
"""
suspicious_words = {
    'suspicious': 1,
    'cancel': 1,
    'illegal': 1,
    'refund': 1,
    'help desk': 0.5,
    'bitcoin': 0.5,
    'authorized': 0.5,
    '24 hours': 0.25,
    'USD': 0.1,
    'BTC': 0.1
}

if __name__ == '__main__':
    for index, line in enumerate(invoice_lines):
        line_total_score = sum(
            score
            for word, score in suspicious_words.items()
            if word in line.lower()
        )

        print(f"Line {index + 1}: {line_total_score}")
