"""
Advent of Code 2020 - Day 10 Part 2 - December 17, 2020
"""

# define functions
# this function uses recursion to build a sum of the number
# of possible combinations of adapters
def possibilityMapper(currentSpot):
    global answer
    possibilities = []
    if currentSpot == adapters[-1]:
        answer += 1
    else:
        if currentSpot+1 in adapters:
            possibilities.append(currentSpot+1)
        if currentSpot+2 in adapters:
            possibilities.append(currentSpot+2)
        if currentSpot+3 in adapters:
            possibilities.append(currentSpot+3)
        for path in possibilities:
            possibilityMapper(path)

# initialized variables
adapters = []
answer = 0

# reads text file of input
data = open('Raw Data\Day10input.txt', 'r')

# stores each line of text file in a list
for line in data:
    adapters.append(int(line[:-1]))

# append a value of 0 to represent the charging outlet
adapters.append(0)
adapters.sort()
# append a value of 3+ the highest rated adapter to represent your device
adapters.append(adapters[-1]+3)

possibilityMapper(adapters[0])

print(answer)
