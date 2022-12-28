
import pprint;
import language_tool_python
tool = language_tool_python.LanguageTool('en-US')  # use a local server (automatically set up), language English
lines = open('invoices.txt', 'r', encoding='utf-8').readlines()
matches = 0

for line in lines:
    error = tool.check(line)
    length = len(error)
    if length  >= 4:
        print("lots of spelling mistakes might wanna check "+ str(length))
    else:
        print("this is fine " + str(length))
