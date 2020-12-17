"""
Advent of Code 2020 - Day 2 Part 2 - December 2, 2020
"""

# reads text file of input
data = open('Raw Data\Day02input.txt', 'r')

# initialized variable
passwords = []
valid = 0

# stores each line of text file as a string in a list
for line in data:
    passwords.append(line[:-1])

# iterate through all passwords and requirements
for i in passwords:
    # stores the matching position
    if i[1] != "-":
        pos1 = int(i[0]+i[1])
        placeHolder = 2
    else:
        pos1 = int(i[0])
        placeHolder = 1
    # stores the differing position
    if i[placeHolder + 2] != " ":
        pos2 = int(i[placeHolder + 1] + i[placeHolder + 2])
        placeHolder += 4
    else:
        pos2 = int(i[placeHolder + 1])
        placeHolder += 3
    # stores the character with the parameter
    char = i[placeHolder]
    # stores the actual password
    password = i[placeHolder+3:]
    # checks to see if password matches parameters
    # and increments number of valid passwords if it does
    if (password[pos1-1] == char and password[pos2-1] != char)\
            or (password[pos1-1] != char and password[pos2-1] == char):
        valid += 1

print("The number of valid passwords is: ", valid)
