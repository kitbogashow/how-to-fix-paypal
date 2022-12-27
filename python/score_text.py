# open the example text file and read each line
lines = open('invoices.txt', 'r', encoding='utf-8').readlines()
scores = 0

"""
a way to map certain keyword or phrases with a "score" of how "bad" they are
"""
sus_words = {
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

for index, line in enumerate(lines):
    line_total_score = 0
    for word, score in sus_words.items():
        if word.lower() in line.lower():
            line_total_score += score
    scores += line_total_score

print("This is the total score: " + str(scores))

if scores > 3:
    print("AYO WHAT DA H*ll, RED FLAAAAG")
