"""
Advent of Code 2020 - Day 9 Part 2 - December 16, 2020
"""

# initialized variables
nums = []
previousNums = []
difference = 0
counter = 0
sum = 0
total = 0
elementsList = []
answer = 0
count = 0
search = True

# reads text file of input
data = open('Raw Data\Day09input.txt', 'r')

# stores each line of text file in a list
for line in data:
    nums.append(line[:-1])

# iterate through each number in the data list
for number in nums[25:]:
    previousNums = nums[0+counter:25+counter]
    check = False
    # iterate through each of the previous 25 number
    # if the difference between the number and one of the previous numbers
    # is within the list of the previous 25, then break and move on to next
    for previousNum in previousNums:
        difference = int(number)-int(previousNum)
        if str(difference) in previousNums:
            check = True
            break
    # if the number was not a sum of two of the previous 25,
    # break out of loop and set invalid = number
    if not check:
        sum = number
        break
    counter += 1

# iterate through each number and grow a total,
# when total > sum, break and go to next number starting value
# if total == sum, break

while search:
    for number in nums[count:]:
        total += int(number)
        elementsList.append(number)
        if total == int(sum):
            break
        elif total > int(sum):
            total = 0
            elementsList = []
            break
    if elementsList != []:
        search = not search
    count += 1

# sort list of nums numerically and add smallest and largest numbers
elementsList.sort()
answer = int(elementsList[0])+int(elementsList[-1])

print(answer)
