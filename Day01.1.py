"""
Advent of Code 2020 - Day 1 Part 1 - December 1, 2020
"""

# reads text file of input
data = open('Raw Data\Day01input.txt', 'r')

# initialized variable
expenses = []
num1 = 0
num2 = 0
product = 0

# stores each line of text file as an integer in a list
for line in data:
    expenses.append(int(line[:-1]))

# creates a list of the complements (2020 minus each expense)
# checks for a a match in the remaining expenses
difference = []
for i in expenses:
    difference.append(2020 - i)
    if i in difference:
        num1 = i
        num2 = 2020 - i
        break

product = num1 * num2
print("The first number is: ", num1)
print("The second number is: ", num2)
print("The product is: ", product)
