"""
Advent of Code 2020 - Day 1 Part 2 - December 1, 2020
"""

# define functions
# this function iterates through a list of expenses three times
# to find the product of three numbers that sum to 2020
def productOf2020Sums():
    global num1, num2, num3
    for i in expenses:
        for x in expenses:
            for y in expenses:
                if x + i + y == 2020:
                    num1 = x
                    num2 = i
                    num3 = y
                    product = num1 * num2 * num3
                    return product

# initialized variable
expenses = []
num1 = 0
num2 = 0
num3 = 0
product = 0

# reads text file of input
data = open('Raw Data\Day01input.txt', 'r')

# stores each line of text file as an integer in a list
for line in data:
    expenses.append(int(line[:-1]))

product = productOf2020Sums()

print("The first number is: ", num1)
print("The second number is: ", num2)
print("The third number is: ", num3)
print("The product is: ", product)
