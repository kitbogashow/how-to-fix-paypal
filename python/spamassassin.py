import os

from spamassassin_client import SpamAssassin

FILES = [dict(type='spam', name='invoices/1.txt'),dict(type='spam', name='invoices/2.txt'),dict(type='spam', name='invoices/3.txt'),dict(type='spam', name='invoices/4.txt'),dict(type='spam', name='invoices/5.txt'),dict(type='spam', name='invoices/6.txt'),dict(type='spam', name='invoices/7.txt'),dict(type='spam', name='invoices/8.txt'),dict(type='spam', name='invoices/9.txt'),dict(type='spam', name='invoices/10.txt'),dict(type='spam', name='invoices/11.txt'),]

def main():
    for test in FILES:
        filename = test['name']
        with open(filename,"rb") as f:            
            print("\nProcessing file: {}".format(filename))
            assassin = SpamAssassin(f.read())
            print("Spamassassin score of {0}".format(assassin.get_score()))

if __name__ == "__main__":
    main()

