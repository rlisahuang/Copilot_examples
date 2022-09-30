"""
Use regular expressions to check if string is a phone number
example: '415-555-4242' returns True
example: '1234567890' is True
example: '(415) 555-4242' is True
example: '+1 415-555-4242' is True
example: '415-555-4242-1234' is False
example: '555-4242' is False
example: '+1 (415)-555-4242' is True  
"""
import re
def isPhoneNumber(text):
    #regex for zero or one +1, zero or one (, 3 digits zero or one ), 0 or 1 space, 3 digits, 0 or 1 space, 4 digits
    if re.search(r'^(\+1)?(\(\d{3}\))?(\s)?\d{3}(\s)?\d{4}$', text):

isPhoneNumber('415-555-4242')
isPhoneNumber('1234567890')
isPhoneNumber('(415) 555-4242')
isPhoneNumber('+1 415-555-4242')
isPhoneNumber('415-555-4242-1234')
isPhoneNumber('555-4242')
isPhoneNumber('+1 (415)-555-4242')
