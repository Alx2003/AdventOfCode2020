"""
Advent of Code 2020 - Day 6 Part 1 - December 6, 2020
"""

# initialized variables
groups = []
group = []
total = 0

# reads text file of input
data = open('Raw Data\Day06input.txt', 'r')

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

for group in groups:
    letters = []
    for person in group:
        for letter in person:
            if letter not in letters:
                letters.append(letter)
    total += len(letters)

print("The sum of the counts is: ", total)