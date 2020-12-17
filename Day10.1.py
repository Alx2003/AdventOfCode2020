"""
Advent of Code 2020 - Day 10 Part 1 - December 16, 2020
"""

# reads text file of input
data = open('Raw Data\Day10input.txt', 'r')

# initialized variables
adapters = []
counter = 0
diff1 = 0
diff2 = 0
diff3 = 0
answer = 0

# stores each line of text file in a list
for line in data:
    adapters.append(int(line[:-1]))

# append a value of 0 to represent the charging outlet
adapters.append(0)
adapters.sort()
# append a value of 3+ the highest rated adapter to represent your device
adapters.append(adapters[-1]+3)

# iterate through a sorted list of adapter values
# accumulate for each adapter difference type
for adapter in adapters:
    if adapter+1 == adapters[counter+1]:
        diff1 += 1
    elif adapter+2 == adapters[counter+1]:
        diff2 += 1
    elif adapter+3 == adapters[counter+1]:
        diff3 += 1
    counter += 1
    if counter+1 == len(adapters):
        break

answer = diff1*diff3
print(answer)
