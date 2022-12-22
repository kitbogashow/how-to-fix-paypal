# Twitch name: Advistane

import re

# Source: https://www.paypal.com/us/smarthelp/contact-us
official_paypal_numbers = [
    "8882211161",
    "4029352050",
    "8889148072"
]


# Doesn't need to scan whole text to find phone numbers,
# but could potentially break due to different phone number formats
def check_performant(line_to_check):
    scam = False  # Assume an email isn't a scam initially
    line_stripped = re.sub(r'[^a-zA-Z0-9_+ ]', '',
                           line_to_check)  # Remove all non-alphanumeric characters (except for _, +, and spaces)
    line_stripped = line_stripped.replace("+1", "")  # Remove country code indicator

    for match in re.finditer(r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b",
                             line_stripped):  # Find phone numbers in the stripped text
        if match not in official_paypal_numbers:  # If the number is not in the official PayPal numbers, it's a scam
            return True

    return False


# Checks all numbers to see if an official PayPal number is included
def check(line_to_check):
    line_stripped = re.sub(r'[^0-9]', '', line_to_check)  # Extract only numbers
    for number in official_paypal_numbers:
        if number not in line_stripped:
            return True


lines = open('./invoices.txt', encoding='utf-8')

for index, line in enumerate(lines):  # Iterate through each line

    print(line)
    print("Scam (performant)?", str(check_performant(line)))
    print("Scam?", str(check(line)))
    print("----------")
