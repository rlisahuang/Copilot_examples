
import re
'''
StackOverFlow
https://stackoverflow.com/questions/466684/how-can-i-return-system-information-in-python
Use regular expression to extract numbers before specific words
'''
def extract_Num(string):
    #Use regular expressions to extract numbers before the
    #words 'hours' ,'hour', 'day', 'days'
    #example: '1 hour ago' returns 1
    #example: '2 days and 3 seconds ago' returns 2
    #example: '2 Approximately 5.1 hours 100 ays 1 s' returns 5.1
    num = re.findall(r'(\d*\.?\d+)\s*(?:hour|hours|day|days)', string)
    #print(num)
    if num:
        #convert array to string
        num = ''.join(num)
        return float(num[0])
    else:
        return 0

extract_Num('2 Approximately 5.1 hours 100 ays 1 s')

'''
Example from Youtube
https://www.youtube.com/watch?v=rhzKDrUiJVk
Create a regular expression that matches different types of phone numbers templates
'''
def isPhoneNumber(string):
    #Use regular expressions to check if string is a phone number
    #example: '415-555-4242' returns True
    #example: '1234567890' is True
    #example: '(415) 555-4242' is True
    #example: '+1 415-555-4242' is True
    #example: '415-555-4242-1234' is False
    #example: '555-4242' is False
    #example: '+1 (415)-555-4242' is True      <= Natural language prompt for Copilot

    #Written by Copilot: Failed
    regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    mo = regex.search(string)
    if mo:
        return True
    else:
        return False

isPhoneNumber('415-555-4242')
isPhoneNumber('1234567890')
isPhoneNumber('(415) 555-4242')   #Return False, Expected True
isPhoneNumber('+1 415-555-4242')
isPhoneNumber('415-555-4242-1234')
isPhoneNumber('555-4242')
isPhoneNumber('+1 (415)-555-4242')

def isPhoneNumber2(string):
    #Written by Copilot: Failed
    reg = re.search(r'^\+1\s?\(?\d{3}\)?\s?\d{3}-\d{4}$', string)
    if reg:
        return True
    else:
        return False

#Everything returned False
isPhoneNumber2('415-555-4242')
isPhoneNumber2('1234567890')
isPhoneNumber2('(415) 555-4242')
isPhoneNumber2('+1 415-555-4242')
isPhoneNumber2('415-555-4242-1234')
isPhoneNumber2('555-4242')
isPhoneNumber2('+1 (415)-555-4242')


def isPhoneNumber3(string):
    #Written by Copilot: Success
    reg = re.match(r'\+?1?\s*\(?(\d{3})\)?\s*-?\s*(\d{3})\s*-?\s*(\d{4})\s*$', string)
    if reg:
        print(reg)
        return True
    else:
        print(reg)
        return False

isPhoneNumber3('415-555-4242')
isPhoneNumber3('1234567890')
isPhoneNumber3('(415) 555-4242')
isPhoneNumber3('+1 415-555-4242')
isPhoneNumber3('415-555-4242-1234')
isPhoneNumber3('555-4242')
isPhoneNumber3('+1 (415)-555-4242')
isPhoneNumber3('abcdefghij')

'''
Example to test how sub() looks in PB
'''
def editParagraph(string):
    #given a string, return a string with the following edits:
    #1. remove all filler words ('very', 'um', 'uh', 'like', 'so', 'basically')
    #2. replace all instances of 'good' with 'great'
    #3. replace all instances of 'bad' with 'terrible'              <= Natural language prompt for Copilot
    
    #remove filler words ignore case
    string = re.sub(r'\b(?:very|um|uh|like|so|basically)\b', '', string, flags=re.IGNORECASE)
    string = re.sub(r'\b(?:very|um|uh|like|so|basically)\b', '', string)
    print("Removing filleter words: " + string)
    #replace good with great
    string = re.sub(r'\b(?:good)\b', 'great', string)
    print("Replacing good with great: " + string)
    #replace bad with terrible
    string = re.sub(r'\b(?:bad)\b', 'terrible', string)
    print("Replacing bad with terrible: " + string)
    print(string)
    return string

string = "Um so basically I am very bad at math. But um I am like good at english."
editParagraph(string)


'''
StackOverFlow:
https://stackoverflow.com/questions/466684/how-can-i-return-system-information-in-python
How Replace a dot (.) in sentence except when it appears in an abbreviation using regular Expression

Depiste Mulitple Tries, Copilot Failed to generate a correct regular expression
Copilot got close, but usually would remove the dot in non abbreviation words
Some light editing was required to get the correct result
'''
def abbrev(string):
    '''
    I want to replace every dot with a space in a sentence except when it is used with an abbreviation.
     When it is used with an abbreviation, I want to replace it with '' NULL.

    Abbreviation means a dot surrounded at least two Capital letters.
    example: 'U.S.A is abbr  x.y  is not. But I.I.T. is also valid ABBVR and so is M.Tech' should
    return 'USA is abbr  x y  is not But IIT is also valid ABBVR and so is MTech'
    '''
    #Written by Copilot: Failed
    #replace all dots with spaces
    string = re.sub(r'\.', ' ', string)
    #replace all abbreviations with ''
    string = re.sub(r'\s[A-Z]\s', '', string)
    print(string)
    return string
abbrev('U.S.A is abbr  x.y  is not. But I.I.T. is also valid ABBVR and so is M.Tech')

def abbrev2(string):
    #Written by Copilot: Failed
    string = re.sub(r'\b\w\.\w\.', '', string)
    string = re.sub(r'\.', ' ', string)
    print(string)
    return string
abbrev2('U.S.A is abbr  x.y  is not. But I.I.T. is also valid ABBVR and so is M.Tech')

def abbrev3(string):
    #Written by Copilot: Failed
    #string = re.sub(r'\.(?=[A-Z]{2})', '', string)
    #string = re.sub(r'\.', ' ', string)
    #string = re.sub(r'\b([A-Z]{2,})\b', r'\1', string)
    string = re.sub(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', '', string)
    print(string)
    return string
abbrev3('U.S.A is abbr  x.y  is not. But I.I.T. is also valid ABBVR and so is M.Tech')

def abbrev4(string):
    #Written by Copilot: Failed
    #First replace all dots with spaces
    string = re.sub(r'\.', ' ', string)
    print(string)
    #Now replace all dots with space except when it is used with an abbreviation.
    string = re.sub(r'(?<!\b[A-Z])\.(?![A-Z])', '', string)
    print(string)
    return string

abbrev4('U.S.A is abbr  x.y  is not. But I.I.T. is also valid ABBVR and so is M.Tech')


def abbrev5(string):
    #Written by Copilot: Failed
    string = re.sub(r'(?<!\b[A-Z])\.(?![A-Z])', '', string)
    string = re.sub(r'\.', ' ', string)
    print(string)
    return string

abbrev5('U.S.A is abbr  x.y  is not. But I.I.T. is also valid ABBVR and so is M.Tech')

#Modified Copilot Code
def abbrevSol(string):
    string = re.sub(r'\.', ' ', string)
    string = re.sub(r'(?<=[A-Z])([ ])(?=[A-Z])', '', string)
    print(string)
    return string
abbrevSol('U.S.A is abbr  x.y  is not. But I.I.T. is also valid ABBVR and so is M.Tech')




