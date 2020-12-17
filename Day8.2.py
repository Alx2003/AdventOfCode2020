"""
Advent of Code 2020 - Day 8 Part 2 - December 12, 2020
"""

# define variables
# increments accumulator by appropriate value when given acc command
def accumulator(line, acc):
    if line[4] == "+":
        acc += int(line[5:])
    else:
        acc -= int(line[5:])
    return acc

# jumps to line of code specified in jmp command
def jmp(line, counter):
    if line[4] == "+":
        counter += int(line[5:])
    else:
        counter -= int(line[5:])
    return counter

# changes code to reflect one jmp or nop command switching
# returns value of acc after running through whole code
# if code is about to complete command for a second time, break
def testCode(command, code, counter):
    codePrime = list.copy(code)
    if command[:3] == "jmp":
        codePrime[counter] = "nop " + command[4:]
    elif command[:3] == "nop":
        codePrime[counter] = "jmp " + command[4:]
    count = 0
    acc = 0
    codeIterations = []
    search = True
    while search:
        line = codePrime[count]
        if count in codeIterations:
            acc = 0
            search = not search
        else:
            codeIterations.append(count)
            # accumulates acc by correct number
            if line[:3] == "acc":
                acc = accumulator(line, acc)
                count += 1
            # jumps to specified line of code
            elif line[:3] == "jmp":
                count = jmp(line, count)
            else:
                count += 1
        if count >= len(codePrime):
            search = not search
    return acc

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

# loop while acc value is 0
# set command equal to each line in code
# if code is a jmp or nop command enter test code
counter = 0
while acc == 0:
    command = code[counter]
    if command[:3] != "acc":
        acc = testCode(command, code, counter)
    counter += 1

# prints out results of accumulator
print("Accumulator is at:", acc)
