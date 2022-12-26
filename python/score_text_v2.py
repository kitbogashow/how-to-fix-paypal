import re

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
    r'24\W?hours ': 0.25,  # Prevents special char to evade regex like 24-hours
    r'usd': 0.1,
    r'btc': 0.1
}

# Compile all regex just once
KEYWORDS = {re.compile(k): v for k, v in KEYWORDS.items()}


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


if __name__ == "__main__":
    for index, text in enumerate(open('invoices.txt', 'r', encoding='utf-8').readlines()):
        print(f"Analyzing email #{index}:")
        matches, score = analyze_text(text)
        if score > 0:
            print(f"Suspicious score: {score}")
            print(f"Suspicious matches: {', '.join(list(set(matches)))}")
        else:
            print("No suspicious keywords found.")
        print()

    print("Don't reply, open links, download attachments, or call any listed phone numbers.")
    print("PayPal will never ask for your password or financial details by email or message, or over the phone.")
    print("Forward suspicious messages to phishing@paypal.com and then delete them.")
