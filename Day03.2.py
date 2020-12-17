"""
Advent of Code 2020 - Day 3 Part 2 - December 3, 2020
"""

# reads text file of input
data = open('Raw Data\Day03input.txt', 'r')

# initialized variable and constants
pathMap = []
spot = 0
numTrees = 0
SLOPES = [1, 3, 5, 7]
counter = 0
product = 1

# stores each line of text file as a string in a list
for line in data:
    pathMap.append(line[:-1])

# iterate through the SLOPES with 1 down
for slope in SLOPES:
    numTrees = 0
    spot = 0
    # iterate through the pathMap
    for row in pathMap:
        # increment for the number of trees encountered
        if row[spot] == "#":
            numTrees += 1
        # reset the spot position (index) if index will go out of bounds
        if spot+slope > 30:
            spot = (spot+slope) % 10 - 1
        # increment the spot position by the slope
        else:
            spot += slope
    product *= numTrees

# reset values of spot and numTrees
spot = 0
numTrees = 0
# iterate through the pathMap
for row in pathMap:
    # increment for each tree encountered if row number is even
    if row[spot] == "#" and counter % 2 == 0:
        numTrees += 1
    # reset spot position if index would go out of bound and
    # row number is not even (this accounts for the right 1, down 2 slope)
    if spot+1 > 30 and counter % 2 != 0:
        spot = 0
    # increment the spot if the row is not even
    elif counter % 2 != 0:
        spot += 1
    counter += 1
product *= numTrees

print("The product of the total number of trees encountered is: ", product)
