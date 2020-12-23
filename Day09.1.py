"""
Advent of Code 2020 - Day 9 Part 1 - December 16, 2020
"""

# initialized variables
nums = []
previousNums = []
difference = 0
counter = 0
invalid = 0

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
        invalid = number
        break
    counter += 1

print("The number that does not follow the pattern is:", invalid)
