"""
Advent of Code 2020 - Day 7 Part 2 - December 10, 2020
"""

# define functions
# this function uses recursion to determine the number of bags within
# a given bag if the rules for their contents are specified (SGBRules)
def recursiveTotalCounter(currBag, multiplier):
    global total
    first = True
    for childBags in currBag[1:]:
        if childBags == "no other bags":
            total += multiplier
        else:
            if childBags not in SGBRules[0][1:] and first:
                first = not first
                total += multiplier
            for rule in SGBRules:
                if childBags[2:] in rule[0]:
                    multiplierPrime = multiplier
                    multiplierPrime *= int(childBags[0])
                    recursiveTotalCounter(rule, multiplierPrime)
                    break

# initialized variables
rules = []
rulesArray = []
substring = ""
search = True
totalBags = 0
total = 0
counter = 0

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

# determines rules that will have an effect on SGB within the main array of rules
SGBRules = []
key = []
for rule in rulesArray:
    if rule[0] == "shiny gold bags":
        SGBRules.append(rule)
        key.append(rule[0])
        break

# create an array of rules that pertain to SGB and its contents
while search:
    for contentRule in SGBRules:
        for contents in contentRule[1:]:
            if contents[2:] in key or contents[2:]+"s" in key:
                search = not search
            else:
                for rule in rulesArray:
                    if contents[2:] in rule[0]:
                        SGBRules.append(rule)
                        key.append(rule[0])
                        break

recursiveTotalCounter(SGBRules[0], 1)
print("The number of bags within my shiny gold bag is:", total)
