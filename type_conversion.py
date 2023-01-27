'''
convert a string representation of a number to a number. The number could be negative. No built-in functions like `int` or `float` should be used.
'''

def string_to_number(string):
    if string[0] == '-':
        # convert the rest of the string to a number
                                                    
        number = string_to_number(string[1:])
        # negate the number
        number = -number
    else:
        # convert the string to a number
        number = 0
        for digit in string:
            # subtract the ascii value of the digit by the ascii value of '0' to get the actual number
            number = number * 10 + ord(digit) - ord('0')
    return number


string_to_number('1234')
string_to_number('-7')
string_to_number('0')
string_to_number('-9395')


'''
First shot prompt: convert a string to a number without using built-in functions
First shot solution: incorrect (failed at negative numbers)

    string = string[::-1]
    number = 0
    for i in range(len(string)):
        number += int(string[i]) * 10 ** i
    return number

'''

'''
Second attempt was correct by getting the correct queries. 

Line 6 `if string[0] == '-'` was manually provided.

All the other comments were queries, except for `#negate the number`, which was part of the synth'd code.

However, the synth'd snippet is incomplete; it stopped at the for loop header, prompting me to add another query `# subtract ...`.
'''