"""
Advent of Code 2020 - Day 2 Part 1 - December 2, 2020
"""

# reads text file of input
data = open('Raw Data\Day2input.txt', 'r')

# initialized variable
passwords = []
valid = 0

# stores each line of text file as a string in a list
for line in data:
    passwords.append(line[:-1])

# iterate through all passwords and requirements
for i in passwords:
    # stores min value if min is double digit
    if i[1] != "-":
        min = int(i[0]+i[1])
        placeHolder = 2
    # stores min value if min is single digit
    else:
        min = int(i[0])
        placeHolder = 1
    # stores max value if max is double digit
    if i[placeHolder+2] != " ":
        max = int(i[placeHolder+1]+i[placeHolder+2])
        placeHolder += 4
    # stores max value if max is single digit
    else:
        max = int(i[placeHolder+1])
        placeHolder += 3
    # stores the character with the parameter
    char = i[placeHolder]
    # stores the actual password
    password = i[placeHolder+3:]
    # set/rest numChars = 0
    numChars = 0
    # check num of instances of char in password
    for x in password:
        if x == char:
            numChars += 1
    if numChars<=max and numChars>=min:
        valid += 1

print("The number of valid passwords is: ", valid, end="\n\n")
