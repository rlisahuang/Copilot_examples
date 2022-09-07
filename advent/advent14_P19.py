'''
Advent Day 14: Participant 19
Task 1: Takes in a string and a list of rules. 
For every pair of letters in the string, insert a new one based on the list of rules.
Example: 
Given the string "NNCB" and the rules "NC->B", "CB->H", "NN->C", "CC->N", "BC->C", "CN->B"
"NN" -> "NCN"; "NC" -> "NBC"; "CB" -> "CHB" 
The result would be "NNCB" -> "NCNBCHB"
'''
def main():
    input_path1 = "C:/Users/sdtnt/ERSP_vscode-5"
    input_path2 = "/s-copilot_testing/input-day14.txt"
    input_path = input_path1 + input_path2

    #Create an empty dictionary <= Natural language prompt for Copilot by participant 19
    #Written by Copilot:
    template = ""
    insertionRules = {}

    #Read input file   <= Natural language prompt for Copilot
    #Written by Copilot:
    with open(input_path, "r") as f:
        input_data = f.read()

        input = input_data.split("\n")

        #Argument one
        template = input[0]

        #Iterate from 2 to the end of list  <= Natural language prompt for Copilot
        #Written by Copilot: (Copilot answer was better than participant 19's original idea)
        for i in range(2, len(input)):
            rawRule = input[i].split("->")

            #Add to dictionary <= Natural language prompt for Copilot
            #Written by Copilot:
            insertionRules[rawRule[0].strip()] = rawRule[1].strip()

    print("Template: " + template)
    print("Rules: " + str(insertionRules))

    #string to array <= Natural language prompt for Copilot
    #Written by Copilot:
    polymer = list(template)

    newPolymer = []
    #Iterate over the polymer <= Natural language prompt for Copilot
    #Written by Copilot:
    for i in range(0, len(polymer)-1):
        insertionRule = insertionRules[polymer[i] + polymer[i+1]]
        if insertionRule is not None:
            newPolymer.append(polymer[i])
            newPolymer.append(insertionRule)
            #newPolymer.append(polymer[i+1])          <= P19 dbugging Copilot's answer; this line unnecessary

    newPolymer.append(polymer[len(polymer) - 1])

    print(newPolymer)

'''
Task 2:  From the new polymer, 
find the letter that appears the most and the letter that appears the least, and find the difference between them.
'''

    #Count the occurances of each letter in newPolymer      <= Natural language prompt for Copilot
    #Written by Copilot:
    letterCounts = {}
    for i in range(0, len(newPolymer)):
        if newPolymer[i] in letterCounts:
            letterCounts[newPolymer[i]] += 1
        else:
            letterCounts[newPolymer[i]] = 1

    #Get the highest value of the dictionary              <= Natural language prompt for Copilot
    #Written by Copilot:
    highestValue = 0
    lowestValue = len(newPolymer)

    for key in letterCounts:
        if letterCounts[key] > highestValue:
            highestValue = letterCounts[key]
        
        if letterCounts[key] < lowestValue:
            lowestValue = letterCounts[key]

    #Written by participant 19:
    result = highestValue - lowestValue
    print("Results: " + str(result))


main()

"""
For counting occurances and highest and lowest values
particpants just accepted Copilot's suggestion
as it seemed right
later went to double check by printing and
evaluating each line
"""