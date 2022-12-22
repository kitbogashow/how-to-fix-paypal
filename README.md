# How to fix PayPal's invoice emails
### or more simply: how to search text for suspicious things

For months now, scammers have been able to exploit the PayPal invoice system to "request money" or invoice potential victims via email. 
These emails come from `service@paypal.com` and therefore look legitimate at first glance. If the particular email user has a PayPal account, they will also see the money deducted in their account and a button to view said request or invoice. 

For more information regarding these types of scams follow [kitboga](https://youtube.com/kitbogashow) on youtube or twitter.

## The regular expressions way:
Credit: @codecat
```regex
([0-9]{3,}|call|contact|\+1)
```
Run test: `$ python3 python/the_regex_way.py`


## The "how suspicious is this text" way:
```
# various phrases to match against, and their "weight" of how bad they are.
sus_words = {
    'cancel': 1,
    'refund': 1,
    'help desk': 0.5,
    'authorized': 0.5,
    '24 hours': 0.25,
    'USD': 0.1
}

for index, line in enumerate(lines):
    line_total_score = 0
    for word, score in sus_words.items():
        if word in line.lower():
            line_total_score += score
    
    # decide what to do if the score is too high 
```
Run test: `$ python python/score_text.py`

## The obfuscated way:
```c
char l[512];int c(char f[]){int i=0,m=0,c;while(c=tolower(l[i++])){char
e=tolower(f[m]);if(!e)return 1;else if(c==e){if(f[m+++1]=='\0')return 1
;}else m=0;}return 0;}int main(){int s=0,t=0;FILE*fh=fopen("../invoice"
"s.txt","rb");while(fgets(l,512,fh))++t&&(c("suspicious")||c("unauthor"
"ized")||c("+1")||c("geek squad")||c(" call"))&&s++;printf("%d / %d\n",
s,t);}
```

### Want to help? 

There are currently (12/22/22) 12 sample invoices in text form in `invoices.txt`.
If you have some code that could solve this task, please let me know and I will try to keep this up to date. 
