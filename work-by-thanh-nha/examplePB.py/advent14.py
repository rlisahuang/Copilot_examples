'''
Advent Day 14: Participant 15
Task 1: Takes in a string and a list of rules. 
For every pair of letters in the string, insert a new one based on the list of rules.
Example: 
Given the string "NNCB" and the rules "NC->B", "CB->H", "NN->C", "CC->N", "BC->C", "CN->B"
"NN" -> "NCN"; "NC" -> "NBC"; "CB" -> "CHB" 
The result would be "NNCB" -> "NCNBCHB"
Task 2:  From the new polymer, 
find the letter that appears the most and the letter that appears the least, 
and find the difference between them.
'''

def main():
    #Read in list of rules from file
    filename = "C:\Users\tumit\OneDrive\Documents\copilot\advent\input-day14.txt"
    rules = []
    #extract first line from file
    string = open(filename).readline().strip()
    with open(filename) as f:
        for line in f:
            #if line is not the first line, add to list of rules
            if line != string:
                #if line is not empty, add to list of rules
                if line != "
                    rules.append(line.strip())

    #Create a dictionary of rules from the list of rules split by "->"
    rules_dict = {}
    for rule in rules:
        key, value = rule.split("->")
        rules_dict[key] = value

    #Read the string, for each pair, insert with value from dictionary
    result = ""
    for i in range(len(string)):
        pair = string[i:i+2]
        if pair in rules_dict:
            result += string[i] + rules_dict[pair]
    result += string[len(string)-1]


    #Find the letter that appears the most and the letter that appears the least in result
    #Find the difference between them
    most = 0
    least = len(result)

    for letter in result:
        if result.count(letter) > most:
            most = result.count(letter)
        if result.count(letter) < least:
            least = result.count(letter)

    return most - least 

main()





    
    

