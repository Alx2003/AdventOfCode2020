"""
Advent of Code 2020 - Day 3 Part 1 - December 3, 2020
"""

# reads text file of input
data = open('Raw Data\Day3input.txt', 'r')

# initialized variable
pathMap = []
spot = 0
numTrees = 0

# stores each line of text file as a string in a list
for line in data:
    pathMap.append(line[:-1])

# iterate through the pathMap
for row in pathMap:
    # increment for each tree hit
    if row[spot] == "#":
        numTrees += 1
    # resets value of spot if index would go out of range
    # else increment spot by 3
    if spot > 30-3:
        spot = (spot+3)%10-1
    else:
        spot += 3

print("The number of trees you will encounter at a slope of 3 right, 1 down is: ", numTrees)
