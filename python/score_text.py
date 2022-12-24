import csv

# open the example text file and read each line
lines = open('invoices.txt', 'r', encoding='utf-8').readlines()

# open a csv-file that contains ඞsussyඞ words
sus_words_csv = csv.reader(open('words.csv'), delimiter=',')

# csv -> python dictionary
sus_words = {}
for row in sus_words_csv:
    try:
        sus_words[row[0]] = float(row[1])
    except ValueError:
        print ("Not a float")
    except IndexError:
        print ("Missing Value")

# give every line a score
for index, line in enumerate(lines):
    line_total_score = 0
    for word, score in sus_words.items():
        if word.lower() in line.lower():
            line_total_score += score

    print(f"Line {index+1}: {line_total_score}")
