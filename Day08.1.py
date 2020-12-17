"""
Advent of Code 2020 - Day 8 Part 1 - December 12, 2020
"""

# define variables
# increments accumulator by appropriate value when given acc command
def accumulator(line):
    global counter, acc
    if line[4] == "+":
        acc += int(line[5:])
    else:
        acc -= int(line[5:])
    counter += 1

# jumps to line of code specified in jmp command
def jmp(line):
    global counter
    if line[4] == "+":
        counter += int(line[5:])
    else:
        counter -= int(line[5:])

# reads text file of input
data = open('Raw Data\Day08input.txt', 'r')

# initialized variables
code = []
acc = 0
codeIterations = []
notBreak = True

# stores each line of text file as an integer in a list
for line in data:
    code.append(line[:-1])

# iterate through the list of commands
counter = 0
while notBreak:
    line = code[counter]
    # if a command is already in list of read commands end loop
    if counter in codeIterations:
        notBreak = not notBreak
        codeIterations.append(counter)
    else:
        codeIterations.append(counter)
        # accumulates acc by correct number
        if line[:3] == "acc":
            accumulator(line)
        # jumps to specified line of code
        elif line[:3] == "jmp":
            jmp(line)
        else:
            counter += 1

# prints out results of accumulator
print("Accumulator is at:", acc)

