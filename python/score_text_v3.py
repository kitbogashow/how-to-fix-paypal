import re

from spellchecker import SpellChecker

# Note to Paypal:
# When an user submits an invoice, before sending the email to the receipent, check what the user has inputed.
# If the text is flagged as suspicious just add a notice at the top of the email.
#
# "Don't reply, open links, download attachments, or call any listed phone numbers.")
# "PayPal will never ask for your password or financial details by email or message, or over the phone.")
# "Forward suspicious messages to phishing@paypal.com and then delete them.")
#
# You won't loose customers doing this and your customers will be safe.

# Do not include spaces or uppercase characters for easier matching.
KEYWORDS = {
    r"\+([\d\(\)-]+)": 2,  # This is a phone number regex.
    r'cancel': 1,
    r'illegal': 1,
    r'refund': 1,
    r'help\W?desk': 1,  # Prevents special char to evade regex like help-desk
    r'bitcoin': 0.5,
    r'authorized': 0.5,
    r'24\W?hours': 0.25,  # Prevents special char to evade regex like 24-hours
    r'usd': 0.1,
    r'btc': 0.1
}

# Compile all regex just once
KEYWORDS = {re.compile(k): v for k, v in KEYWORDS.items()}

SPELLCHECK_MIN_WORD_LEN = 3
SPELLCHECKER = SpellChecker()

KNOWN_VALID_WORDS = {"paypal", "coinbase"}

SPELLCHECK_VALUE_COEFICIENT = 0.8  # Adjust te value of the keyword that was corrected automate
SPELLCHECK_INVALID_VALUE = 0.1  # Adjust te value of the keyword that was corrected automate


# Returns list of matches and the suspicious score.
def analyze_text(text: str) -> tuple[list[str], float]:
    # Remove all spaces, tabs, newlines and make the text lower-case for better easier matching.
    text = re.sub(r'\s+', '', text).lower()

    sus = []
    sus_score = 0
    for pattern, score in KEYWORDS.items():

        for match in re.findall(pattern, text):
            sus.append(match)
            sus_score += score

    return sus, sus_score


def analyze_misspell_in_text(text: str) -> tuple[list[str], list[str], float]:
    # Splits text by whitespaces and remove shorter words
    words = [re.sub(r'\W', '', word)  # Removes special chars from word to prevent false positives
             for word in text.lower().split()  # Splits texts and makes it lowercase
             if len(word) > SPELLCHECK_MIN_WORD_LEN]  # Filters too short words

    misspelled = SPELLCHECKER.unknown(words)  # Find all (probably) misspelled words

    invalid_words = []
    alternatives_text = []

    for word in misspelled:
        if word in KNOWN_VALID_WORDS:  # Valid words not recognized by the spellchecker
            continue

        if len(word) <= SPELLCHECK_MIN_WORD_LEN:
            continue

        invalid_words.append(word)

        alternatives = SPELLCHECKER.candidates(word)
        if not alternatives:
            continue

        alternatives_text += list(alternatives)

    alternatives_text = " ".join(alternatives_text)

    suspect_words, score = analyze_text(alternatives_text)

    # Calculates the score adding the corrected suspect score plus number of invalid words in text
    score = score * SPELLCHECK_VALUE_COEFICIENT + len(invalid_words) * SPELLCHECK_INVALID_VALUE

    return invalid_words, suspect_words, score


if __name__ == "__main__":
    for index, text in enumerate(open('invoices.txt', 'r', encoding='utf-8').readlines()):
        print(f"Analyzing email #{index}:")
        matches, score = analyze_text(text)
        invalid_words, suspect_words, misspell_score = analyze_misspell_in_text(text)

        suspect_words = suspect_words + matches
        score = score + misspell_score

        if score > 0:
            print(f"Suspicious score: {score}\n",
                  f"\tSuspicious matches: {', '.join(list(set(matches)))} \n" if matches else "",
                  f"\tInvalid words: {', '.join(list(set(invalid_words)))} \n" if invalid_words else "",
                  f"\n\n")
            continue

        print("No suspicious keywords found.\n\n")

    print("Don't reply, open links, download attachments, or call any listed phone numbers.\n",
          "PayPal will never ask for your password or financial details by email or message, or over the phone.\n",
          "Forward suspicious messages to phishing@paypal.com and then delete them.\n")
