"""
Advent of Code 2020 - Day 4 Part 2 - December 4, 2020
"""

# define functions
def byrValidity(byr):
    if 1920 <= int(byr[4:]) <= 2002:
        return True
    else:
        return False

def iyrValidity(iyr):
    if 2010 <= int(iyr[4:]) <= 2020:
        return True
    else:
        return False

def eyrValidity(eyr):
    if 2020 <= int(eyr[4:]) <= 2030:
        return True
    else:
        return False

def hgtValidity(hgt):
    if hgt[-2:] == "cm" and 150 <= int(hgt[4:-2]) <= 193:
        return True
    elif hgt[-2:] == "in" and 59 <= int(hgt[4:-2]) <= 76:
        return True
    else:
        return False

def hclValidity(hcl):
    validChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    if hcl[4] == "#" and len(hcl[5:]) == 6:
        for char in hcl[5:]:
            if char not in validChars:
                return False
        return True
    else:
        return False

def eclValidity(ecl):
    eclValid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl[4:] in eclValid:
        return True
    else:
        return False

def pidValidity(pid):
    if len(pid[4:]) == 9 and pid[4:].isnumeric():
        return True
    else:
        return False

def credentialCheck(credentials):
    byrValid = byrValidity(credentials[0])
    eclValid = eclValidity(credentials[1])
    eyrValid = eyrValidity(credentials[2])
    hclValid = hclValidity(credentials[3])
    hgtValid = hgtValidity(credentials[4])
    iyrValid = iyrValidity(credentials[5])
    pidValid = pidValidity(credentials[6])
    if byrValid and eclValid and eyrValid and hclValid and hgtValid and iyrValid and pidValid:
        return True
    else:
        return False

# initialized variables and constants
credentials = []
passportArray = []
validity = True
numValid = 0

# reads text file of input
data = open('Raw Data\Day4input.txt', 'r')

# stores each person's credential as a string in a list
# accounts for a passports data being spread across multiple lines
substring = ""
for line in data:
    if line == "\n":
        credentials.append(substring)
        substring = ""
    elif substring == "":
        substring = line[:-1]
    else:
        substring = substring+" "+line[:-1]

# stores each persons set of credentials in a list
# broken up into different fields (excluding cid)
substring = ""
personPassport = []
for passport in credentials:
    counter = 0
    for char in passport:
        counter += 1
        # if substring (key) starts with cid, clears substring
        if counter != 1 and (passport[counter - 7] + passport[counter - 6] + passport[counter - 5] == "cid"
                             or passport[counter - 6] + passport[counter - 5] + passport[counter - 4] == "cid"):
            substring = ""
        # if another iteration through the passport will
        # result in an out of bounds index, append current substring
        elif counter + 1 > len(passport):
            substring = substring + char
            personPassport.append(substring)
            substring = ""
        # if char is not a space, add char to substring
        elif char != " ":
            substring = substring+char
        # if char is a space and substring is not blank,
        # append substring to passport
        elif char == " " and substring != "":
            personPassport.append(substring)
            substring = ""
    personPassport.sort()
    if len(personPassport) == 7:
        passportArray.append(personPassport)
    personPassport = []

for credential in passportArray:
    valid = credentialCheck(credential)
    if valid:
        numValid += 1

print(numValid, "passports are valid.")
