import re

def readDemEmail(fn):
    demEmails=[]
    emails=[]
    with open(fn, "r") as file:
        emails=file.readlines()
    for email in emails:
        demEmails.append({"emailText":email})
    return demEmails


demEmails=readDemEmail("invoices.txt")

obviLies = [ "if you did not", "suspisous activites", "please call (us|at|our)", "illegally access"]
     



for email in demEmails:
    lie=email['emailText']
    email['intent'] = "innocent"
    for obvi in obviLies:
        if re.search(obvi, lie.lower()):
            email['intent'] = "scam"
            break

print(len([email for email in demEmails if email['intent'] == "scam"]))
    
    








