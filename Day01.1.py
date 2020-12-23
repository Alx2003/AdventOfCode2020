"""
Advent of Code 2020 - Day 1 Part 1 - December 1, 2020
"""

# define functions
# this function finds the pair of numbers, which
# have their complement (2020 minus the expense)
# within the list of numbers
def productOf2020Sums():
    global num1, num2
    difference = []
    for i in expenses:
        difference.append(2020 - i)
        if i in difference:
            num1 = i
            num2 = 2020 - i
            product = num1 * num2
            return product

# initialized variable
expenses = []
num1 = 0
num2 = 0
product = 0

# reads text file of input
data = open('Raw Data\Day01input.txt', 'r')

# stores each line of text file as an integer in a list
for line in data:
    expenses.append(int(line[:-1]))

product = productOf2020Sums()

print("The first number is:", num1)
print("The second number is:", num2)
print("The product is:", product)
