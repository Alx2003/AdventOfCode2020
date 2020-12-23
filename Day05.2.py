"""
Advent of Code 2020 - Day 5 Part 2 - December 5, 2020
"""

# initialized variable
boardingPasses = []
ROW_KEYS = ["F", "B"]
COLUMN_KEYS = ["L", "R"]
NUM_ROWS = 128
NUM_COLS = 8
seatRows = []
seatColumns = []
rows = []
columns = []
seatIDs = []
mySeat = 0

# reads text file of input
data = open('Raw Data\Day05input.txt', 'r')

# stores each line of text file as a string in a list
for line in data:
    boardingPasses.append(line[:-1])

# builds a list of all row numbers
i = 0
while i < NUM_ROWS:
    rows.append(i)
    i += 1

# builds a list of all column numbers
i = 0
while i < NUM_COLS:
    columns.append(i)
    i += 1

# iterates through each boarding pass
for boardingPass in boardingPasses:

    possible_rows = rows
    # iterates through each character in boarding pass
    # sets possible rows to valid row numbers based on character
    for key in boardingPass[:7]:
        if key == ROW_KEYS[0]:
            possible_rows = possible_rows[:int(len(possible_rows)/2)]
        else:
            possible_rows = possible_rows[int(len(possible_rows)/2):]
    # once there is only one possible row, appends value to list of rows
    seatRows.append(int(possible_rows[0]))

    possible_columns = columns
    # iterates through each character in boarding pass
    # sets possible columns to valid column numbers based on character
    for key in boardingPass[-3:]:
        if key == COLUMN_KEYS[0]:
            possible_columns = possible_columns[:int(len(possible_columns)/2)]
        else:
            possible_columns = possible_columns[int(len(possible_columns)/2):]
    # once there is only one possible column, appends value to list of columns
    seatColumns.append(int(possible_columns[0]))

count = 0
# iterates through each boarding pass, and builds
# a list of all seat IDs
for seat in boardingPasses:
    seatID = seatRows[count]*8+seatColumns[count]
    seatIDs.append(seatID)
    count += 1

# iterates through each seat ID, and checks for
# a seat ID with a taken seat ID 2 from it, and
# a vacant seat in between
for i in seatIDs:
    if i+2 in seatIDs and i+1 not in seatIDs:
        mySeat = i+1

print("My seat ID is: ", mySeat)


