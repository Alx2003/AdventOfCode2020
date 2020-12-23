"""
Advent of Code 2020 - Day 10 Part 2 - December 17, 2020
"""

# define functions
# this function uses recursion to map the possibilities
# and increment when the end value is reached
def possibilityMapper(currentSpot):
    global answer
    if currentSpot == adapters[-1]:
        answer += 1
    else:
        for options in adapterOptions:
            if currentSpot == options[0]:
                for validConnections in options [1:]:
                    possibilityMapper(validConnections)
                break

# initialized variables
adapters = []
answer = 0
adapterOptions = []

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

# build an array of the adapter and what can connect to it
for adapter in adapters:
    possibilities = [adapter]
    if adapter+1 in adapters:
        possibilities.append(adapter+1)
    if adapter+2 in adapters:
        possibilities.append(adapter+2)
    if adapter+3 in adapters:
        possibilities.append(adapter+3)
    adapterOptions.append(possibilities)

possibilityMapper(adapters[0])

print(answer)
