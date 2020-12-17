"""
Advent of Code 2020 - Day 6 Part 2 - December 6, 2020
"""

# reads text file of input
data = open('Raw Data\Day06input.txt', 'r')

# initialized variables
groups = []
group = []
total = 0

# stores each line of the text file as a string in a list for each group.
# when a new line character is hit, append the current list to groups array,
# and clear memory for group
i = 0
for line in data:
    if i == 2282:
        group.append(line[:-1])
        groups.append(group)
        group = []
    elif line != "\n":
        group.append(line[:-1])
    else:
        groups.append(group)
        group = []
    i += 1

# iterates through each group of passengers
for group in groups:
    # if group length is 1, set valid chars to that person's answers
    if len(group) == 1:
        valid = group[0]
    # else set reference to first person in the group
    # and clear valid value
    else:
        ref = group[0]
        potentialValid = []
        valid = ""
        # iterate through the rest of the members of each group
        for person in group[1:]:
            # iterates through each letter in those members
            for letter in person:
                if letter in ref:
                    potentialValid.append(letter)
        # determine how many occurrences of letter in potential valid
        # if occurrences == len(group-1),  then add letter to valid
        for letter in potentialValid:
            count = potentialValid.count(letter)
            if count == len(group)-1 and letter not in valid:
                valid = valid+letter
    total += len(valid)

print("The sum of the counts is: ", total)
