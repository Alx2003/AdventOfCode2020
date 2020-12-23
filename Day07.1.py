"""
Advent of Code 2020 - Day 7 Part 1 - December 7, 2020
"""

# initialized variables
rules = []
rulesArray = []
substring = ""
containSGB = []
search = True

# reads text file of input
data = open('Raw Data\Day07input.txt', 'r')

# stores each line of text file as an integer in a list
for line in data:
    rules.append(line[:-1])

# iterate through each rule in list of rules
for rule in rules:
    count = 0
    ruleParts = []
    # splits the rule up into an array with first index being the key,
    # and remaining indices being the contents
    for char in rule:
        if char == " " and rule[count-4]+rule[count-3]+rule[count-2]+rule[count-1] == "bags":
            ruleParts.append(substring)
            substring = ""
        elif char == ".":
            ruleParts.append(substring)
            substring = ""
        elif char == ",":
            ruleParts.append(substring)
            substring = ""
        elif char == " " and rule[count-4]+rule[count-3]+rule[count-2]+rule[count-1] == "tain":
            substring = ""
        elif char == " " and rule[count-1] == ",":
            substring = ""
        else:
            substring = substring+char
        count += 1
    rulesArray.append(ruleParts)

# iterate through each rule and creates a list (containSGB)
# of the bags, which contain a SGB
for ruleList in rulesArray:
    for rule in ruleList[1:]:
        if "shiny gold bag" in rule:
            containSGB.append(ruleList[0])
oldLength = len(containSGB)

# redo this process until no new bag types are found
# therefore all bag types which contain a SGB are accounted for
while search:
    for key in containSGB:
        for ruleList in rulesArray:
            for rule in ruleList[1:]:
                # checks for single type and multiple bag (ie. bags or bag)
                if (key in rule or key[:-1] in rule) and ruleList[0] not in containSGB:
                    containSGB.append(ruleList[0])
    newLength = len(containSGB)
    if newLength == oldLength:
        search = not search
    else:
        oldLength = newLength

print(len(containSGB), "colour bags will eventually contain a shiny gold bag.")