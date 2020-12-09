"""
Advent of Code 2020 - Day 1 Part 2 - December 1, 2020
"""

# reads text file of input
data = open('Raw Data\Day1input.txt', 'r')

# initialized variable
expenses = []
num1 = 0
num2 = 0
num3 =0
product = 0

# stores each line of text file as an integer in a list
for line in data:
    expenses.append(int(line[:-1]))

# iterates through all the expenses and finds the
# 3 numbers that sum to 2020
for i in expenses:
    for x in expenses:
        for y in expenses:
            if x + i + y == 2020:
                num1 = x
                num2 = i
                num3 = y
                break

product = num1 * num2 * num3
print("The first number is: ", num1)
print("The second number is: ", num2)
print("The third number is: ", num3)
print("The product is: ", product)
