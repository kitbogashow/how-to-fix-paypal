# Something like this should be used on PayPal's end to prevent users from sending invoices with naughty words

naughtyWords = ['fraud', 'refund', 'illegal', 'if you did not', 'toll']
sellerNote = input("Enter your note to the customer: ")
any_word_in_string = any(word in sellerNote for word in naughtyWords)
if any_word_in_string:
    print('Your customer note contains naughty words please try again')
else:
    print('Invoice sent')
