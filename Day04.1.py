"""
Advent of Code 2020 - Day 4 Part 1 - December 4, 2020
"""

# initialized variables and constants
FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
credentials = []
validity = True
validPass = 0

# reads text file of input
data = open('Raw Data\Day04input.txt', 'r')

# stores each line of text file as a string in a list
# accounts for a passports data being spread across multiple lines
substring = ""
for line in data:
    if line == "\n":
        credentials.append(substring)
        substring = ""
    elif substring == "":
        substring = line[:-1]
    else:
        substring = substring+" "+line[:-1]

# iterates through list of passports and required fields
# if passport has all required fields, increment to accumulator
for passport in credentials:
    for field in FIELDS[:-1]:
        if field not in passport:
            validity = False
            break
    if validity:
        validPass += 1
    validity = True

print(validPass, "passports are valid.")
