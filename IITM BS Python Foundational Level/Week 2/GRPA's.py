# GRPA - 1
# Accept three positive integers as input and check if they form the sides of a right triangle. 
# Print YES if they form one, and NO if they do not. 
# The input will have three lines, with one integer on each line. 
# The output should be a single line containing one of these two strings: YES or NO.

a = int(input())
b = int(input())
c = int(input())

if((a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2)):
    print("Yes, They form the right angle triangle")
else:
    print("No, They do not form the right angle triangle")

# GRPA - 2
# EvenOdd is a tech startup. Each employee at the startup is given an employee id which is a unique positive integer. 
# On one warm Sunday evening, five employees of the company come together for a meeting and sit at a circular table:
# The employees follow a strange convention. They will continue the meeting only if the following condition is satisfied.
# The sum of the employee-ids of every pair of adjacent employees at the table must be an even number.
# They are so lazy that they won't move around to satisfy the above condition. If the current seating plan doesn't satisfy the condition, the meeting will be canceled. 
# You are given the employee-id of all five employees. Your task is to decide if the meeting happened or not.
# The input will be five lined, each line containing an integer. 
# The ith line will have the employee-id of Ei. 
# The output will be a single line containing one of these two strings: YES or NO.

e1 = int(input())
e2 = int(input())
e3 = int(input())
e4 = int(input())
e5 = int(input())

if((e1 + e2) % 2 == 0 and (e2 + e3) % 2 == 0 and (e3 + e4) % 2 == 0 and (e4 + e5) % 2 == 0 and (e5 + e1) % 2 == 0):
    print("Yes, The meeting will happen")
else:
    print("No, The meeting is cancelled")

# GRPA - 3
# Accept a string as input and print the vowels present in the string in alphabetical order. 
# If the string doesn't contain any vowels, then print the string none as output. 
# Each vowel that appears in the input string — irrespective of its case — should appear just once in lower case in the output.

string = input()
vowels = ''

if("A" in string or 'a' in string):
    vowels += 'a'
if("E" in string or 'e' in string):
    vowels += 'e'
if("I" in string or "i" in string):
    vowels += 'i'
if("O" in string or "o" in string):
    vowels += 'o'
if("U" in string or "u" in string):
    vowels += 'u'

if vowels == '':
    print("None")
else:
    print(vowels)

# GRPA - 4
# You are given the dates of birth of two persons, not necessarily from the same family. 
# Your task is to find the younger of the two. 
# If both of them share the same date of birth, then the younger of the two is assumed to be that person whose name comes first in alphabetical order (names will follow Python's capitalize case format).
# The input will have four lines. 
# The first two lines correspond to the first person, while the last two lines correspond to the second person. 
# For each person, the first line corresponds to the name and the second line corresponds to the date of birth in DD-MM-YYYY format. 
# Your output should be the name of the younger of the two.

fname = input()
fdob = input()
sname = input()
sdob = input()

d1 = int(fdob[0:2])
d2 = int(sdob[0:2])
m1 = int(fdob[3:5])
m2 = int(sdob[3:5])
y1 = int(fdob[6:])
y2 = int(sdob[6:])

if(fdob == sdob):
    if(fname[0] < sname[0]):
        print(fname)
    else:
        print(sname)

elif(y1 < y2):
    print(sname)

elif(y1 == y2):
    if(m1 < m2):
        print(sname)
    elif(m1 == m2):
        if(d1 < d2):
            print(sname)
        else:
            print(fname)
    else:
        print(fname)

else:
    print(fname)

# GRPA - 5
# Accept a string as input. Your task is to determine if the input string is a valid password or not. 
# For a string to be a valid password, it must satisfy all the conditions given below:
# (1) It should have at least 8 and at most 32 characters
# (2) It should start with an uppercase or lowercase letter
# (3) It should not have any of these characters: / \ = ' "
# (4) It should not have spaces
# It could have any character that is not mentioned in the list of characters to be avoided (points 3 and 4). 
# Output True if the string forms a valid password and False otherwise.

string = input()
valid_password = False

if 8 <= len(string) <= 32:
    if "A" <= string[0] <= "Z" or "a" <= string[0] <= "z":
        if not("/" in string or "\\" in string or "=" in string or "'" in string
                or '"' in string or " " in string):
            valid_password = True
        
if(valid_password == True):
    print(True)
else:
    print(False)

            
            