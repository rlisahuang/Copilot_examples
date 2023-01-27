'''
Advent Day 14: Participant 15
Task 1: Takes in a string and a list of rules. 
For every pair of letters in the string, insert a new one based on the list of rules.
Example: 
Given the string "NNCB" and the rules "NC->B", "CB->H", "NN->C", "CC->N", "BC->C", "CN->B"
"NN" -> "NCN"; "NC" -> "NBC"; "CB" -> "CHB" 
The result would be "NNCB" -> "NCNBCHB"
'''

#Written by P15 with help from Copilot: P15 forgot how to strip in Python
#Copilot helped by automatically suggesting the correct syntax
#P15 immediately printed out the result to check if it was correct
def create_dict_from_split_string(string):
    key = string.split("->")[0].strip()
    value = string.split("->")[1].strip()
    return {key:value}

    
#Written by Copilot:
#P15 checked if was correct by printing out the result
def convert_string_to_list(string):
    return list(string)

#Written mostly by P15 with help from Copilot autocomplete suggestions
def main():
    input_path1 = "C:/Users/sdtnt/ERSP_vscode-5"
    input_path2 = "/s-copilot_testing/input-day14.txt"
    input = input_path1 + input_path2
    with open(input) as file:
        data = file.read().splitlines()
    print(data)
    reaction_list = []
    compound = convert_string_to_list(data[0])
    print(compound)
    for line in data:
        if "->" in line:
            reaction_list.append(
                create_dict_from_split_string(line)
            )
    print(reaction_list)


main()

#Note: particapant already had a very clear method of how they wanted
#To write their code. They were just using Copilot to test its 
#capabilites and handle tedious tasks
#It seems like it saved them a few Google searches though