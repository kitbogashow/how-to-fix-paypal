import re

# Do not include spaces or uppercase characters for easier matching.
KEYWORDS = { 
    re.compile(r"\+([\d\(\)-]+)"): 2, # This is a phone number regex.
    'cancel': 1,
    'illegal': 1,
    'refund': 1,
    'helpdesk': 1,
    'bitcoin': 0.5,
    'authorized': 0.5,
    '24hours': 0.25,
    'usd': 0.1, 
    "btc": 0.1
}

def analyze_text(text: str) -> None:
    text = re.sub(r'\s+', '', text).lower() # Remove all spaces, tabs, newlines and make the text lower-case for better easier matching.

    sus = []
    sus_score = 0
    for pattern, score in KEYWORDS.items():
        if isinstance(pattern, str):
            pattern = re.compile(re.escape(pattern)) #If it is a string convert it to a regex pattern.

        for match in re.findall(pattern, text):
            sus.append(match)
            sus_score += score



    if len(sus) > 0:
        print(f"Suspicious score: {sus_score}")
        print(f"Suspicious matches: {', '.join(list(set(sus)))}")
        return
    print("No suspicious keywords found.")

if __name__ == "__main__":  
    for index, text in enumerate(open('invoices.txt', 'r', encoding='utf-8').readlines()):
        print(f"Analyzing email #{index}:")
        analyze_text(text)
        print()
    
    print("Don't reply, open links, download attachments, or call any listed phone numbers.")
    print("PayPal will never ask for your password or financial details by email or message, or over the phone.")
    print("Forward suspicious messages to phishing@paypal.com and then delete them.")