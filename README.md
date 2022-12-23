# How to fix PayPal's invoice emails

### or more simply: how to search text for suspicious things

For months now, scammers have been able to exploit the PayPal invoice system to "request money" or invoice potential victims via email.
These emails come from `service@paypal.com` and therefore look legitimate at first glance. If the particular email user has a PayPal account, they will also see the money deducted in their account and a button to view said request or invoice.

For more information regarding these types of scams follow [kitboga](https://youtube.com/kitbogashow) on youtube or twitter.

An example invoice email looks like this:
![](/assets/email.png)

## Table of contents:

-   [Context links](#context-links)
-   [The "easy" way](#the-simple-way)
-   [The regular expressions way](#the-regular-expressions-way)
-   [The "how suspicious is this text" way](#the-how-suspicious-is-this-text-way)
-   [The obfuscated way](#the-obfuscated-way)
-   [The Java Way](#the-java-way)
-   [The RUSTy way](#the-rusty-way)
-   [Want to help?](#want-to-help)

## Context links:

-   [PayPal's information on fake messages](https://www.paypal.com/us/security/learn-about-fake-messages)


## The "simple" way:
Don't allow your users to include phone numbers in the "message" of an invoice. 

But if that somehow causes irreputable harm to your business, explore the other options below:

## The regular expressions way:

Credit: @codecat

```regex
([0-9]{3,}|call|contact|\+1)
```
Run test: `$ python3 python/the_regex_way.py`

## The "how suspicious is this text" way:
Credit @kitbogashow
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
        if word.lower() in line.lower():
            line_total_score += score

    # decide what to do if the score is too high
```
Run test: `$ python python/score_text.py`

## The obfuscated way:
Credit: @codecat
```c
char l[512];int c(char f[]){int i=0,m=0,c;while(c=tolower(l[i++])){char
e=tolower(f[m]);if(!e)return 1;else if(c==e){if(f[m+++1]=='\0')return 1
;}else m=0;}return 0;}int main(){int s=0,t=0;FILE*fh=fopen("../invoice"
"s.txt","rb");while(fgets(l,512,fh))++t&&(c("suspicious")||c("unauthor"
"ized")||c("+1")||c("geek squad")||c(" call"))&&s++;printf("%d / %d\n",
s,t);}
```

## The one line node.js way:
Credit: @Nomnivore
```
import("fs").then((fs) => fs.readFileSync("./invoices.txt").toString().trim().split("\n").forEach((l, n) => l.search(/([0-9]{3,}|call|contact|\\+1)/) >= 0 ? console.log(`line ${n} is likely a scam`) : console.log(`line ${n} is likely not a scam`)))
```
see `javascript/scamGoBye.js`

## The Java Way:
Credit: @Gamer1120 / @datatags
```
private static final Pattern PATTERN = Pattern.compile("[0-9]{3,}|call|contact|\\\\+1");
public static void main(String[] args) {
    try (BufferedReader reader = new BufferedReader(new FileReader("invoices.txt"))) {
        reader.lines().forEach(line -> {
            if (PATTERN.matcher(line).find()){
                System.out.println("ඞ sus thing found: " + line);
            }
        });
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```
see `java/src/main/java/FixPaypalRegex.java`

## The RUSTy way: 
Credit: @jasonverbeek
```
fn rate_lines() -> Result<()> {
    let file = File::open("../../invoices.txt")
        .or_else(|_| ErrorType::IOError.as_error("Could not open invoices.txt"))?;
    let lines = std::io::BufReader::new(file).lines();

    for (i, line) in lines.enumerate() {
        let mut score = 0;
        if let Ok(line_str) = line {
            for sussy in SUSSY_WUSSY {
                if line_str.to_lowercase().contains(sussy) {
                    score += 1;
                }
            }
        }
        println!("line {} has a sussy wussy score of {}", i, score);
    }
    Ok(())
}
```
see `rust/sussy-wussy-meter`

## The GO way:
Credit: @McChronicle
```
regex := regexp.MustCompile(`([0-9]{3,}|call|contact|\+1)`)
for _, message := range messages {
    if regex.MatchString(message) {
        matches++
    }
}
```
see `go/the_regex_way.go`

## The Lua way:
Credit: @not-optikk
```
for word in text:gmatch('%w+') do
    if flagged_words[word] then
        sus_score = sus_score + flagged_words[word]
    elseif word:match('%d+') == word and not whitelisted_numbers[word] then
        table.insert(numbers, word)
    end
end
```
see `lua/main.lua`


## The Bash way:
Credit: @emp500
```
#!/bin/bash

count=0
while IFS= read -r line
do
  if echo $line | grep -Piq "([0-9]{3,}|call|contact|\+1)"; then
    echo "sus line found"
    let count++
  fi
done < "../invoices.txt"

echo "sus lines: $count"
```
see `bash/run.sh`

### Want to help? 

There are currently (12/22/22) 12 sample invoices in text form in `invoices.txt`.
If you have some code that could solve this task, please let me know and I will try to keep this up to date.
