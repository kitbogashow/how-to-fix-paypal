# Twitch name: Advistane

import os.path
import re

# Source: https://www.paypal.com/us/smarthelp/contact-us
official_paypal_numbers = [
    "8882211161",
    "4029352050",
    "8889148072"
]
lines = open(os.path.join(os.getcwd(), '..', 'invoices.txt'), encoding='utf-8')

for index, line in enumerate(lines):  # Iterate through each line
    scam = False  # Assume an email isn't a scam initially
    line_stripped = re.sub(r'[^a-zA-Z0-9_+ ]', '',
                           line)  # Remove all non-alphanumeric characters (except for _, +, and spaces)
    line_stripped = line_stripped.replace("+1", "")  # Remove country code indicator

    for match in re.finditer(r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b",
                             line_stripped):  # Find phone numbers in the stripped text
        if match not in official_paypal_numbers:  # If the number is not in the official PayPal numbers, it's a scam
            scam = True
            break

    print(line)
    print("Scam?", str(scam))
    print("----------")
