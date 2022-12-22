# How to fix PayPal's invoice emails
### or more simply: how to search text for suspicious things

For months now, scammers have been able to exploit the PayPal invoice system to "request money" or invoice potential victims via email. 
These emails come from `service@paypal.com` and therefore look legitimate at first glance. If the particular email user has a PayPal account, they will also see the money deducted in their account and a button to view said request or invoice. 

For more information regarding these types of scams follow [kitboga](https://youtube.com/kitbogashow) on youtube or twitter.

## The simple way:


## Using Natural Language Processing:


## The regular expressions way:
```regex
([0-9]{3,}|call|contact|\+1)
```
Run test: `$ python3 python/the_regex_way.py`

### Want to help? 

There are currently (12/22/22) 12 sample invoices in text form in `invoices.txt`.
If you have some code that could solve this task, please let me know and I will try to keep this up to date. 
