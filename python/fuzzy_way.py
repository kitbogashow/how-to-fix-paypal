# https://marcobonzanini.com/2015/02/25/fuzzy-string-matching-in-python/
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

invoices = open('../invoices.txt', 'r', encoding='utf-8').readlines()

scam_threshold = 75 # this threshold is usually enough for fuzzy matching, this can be modified though

new_invoice =  input('try a new invoice text: ') # this more of a proof of concept thing, paypal will probably need to do batch inputs or something

is_scam = False

for line in enumerate(invoices):
    fuzzy_ratio = fuzz.partial_ratio(line, new_invoice)
    
    if (fuzzy_ratio > scam_threshold):
        is_scam = True
        break
        
if (is_scam):
    print ('this is a scam! :(')

else:
    print ('this is NOT a scam! :)')

