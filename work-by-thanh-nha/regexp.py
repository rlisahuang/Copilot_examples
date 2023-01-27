'''
StackOverFlow
https://stackoverflow.com/questions/7548692/how-to-grab-number-after-word-in-python
How to grab number after word in Python?
'''
#find the number that follows the pattern x in the line
#where x is the pattern
#so given uniprotkb:P09123
# want to find num = 09123                              <= Natural language prompt for Copilot
#Written by Copilot:
import re
x = 'uniprotkb:P'
f = open('m.txt')
for line in open('m.txt'):
    match = re.search('uniprotkb:P(\d+)', line)
    if match:
        print (match.group(1))

    

    
