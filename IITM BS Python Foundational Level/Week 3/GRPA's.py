# GRPA - 1
# Accept a positive integer n as input and print the sum of the first n terms of the series given below:

n = int(input())
sumofnterms = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        sumofnterms += j
        
print(sumofnterms)

# GRPA - 2
# Accept a positive integer n, with n>1, as input from the user and print all the prime factors of n in ascending order.

n = int(input())
for d in range(2, n+1):
    if n % d == 0:
        isprime = True
        for f in range(2, d):
            if d % f == 0:
                isprime = False
                break
        if isprime:
            print(d)

# GRPA - 3
# A bot starts at the origin — (0,0) — and can make the following moves:
# (1) UP
# (2) DOWN
# (3) LEFT
# (4) RIGHT
# Each move has a magnitude of 1 unit. 
# Accept the sequence of moves made by the bot as input. 
# The first entry in the sequence is always START while the last entry in the sequence is always STOP. 
# A sample sequence is given below:
# START
# UP
# RIGHT
# LEFT
# LEFT
# DOWN
# UP
# STOP
# Print the Manhattan distance of the bot from the origin. 
# If the bot is at the position (x,y), then its Manhattan distance from the origin is given by the equation:
# D=∣x∣+∣y∣

entry = input()

while(entry != 'STOP'):

    if entry == 'UP':
        y += 1
    elif entry == 'RIGHT':
        x += 1
    elif entry == 'LEFT':
        x -= 1
    elif entry == 'DOWN':
        y -= 1
    else:
        x, y = 0, 0
    
    entry = input()

Manhattan_distance = abs(x) + abs(y)
print(Manhattan_distance)

# GRPA - 4
# Accept a string as input, convert it to lower case, sort the string in alphabetical order, and print the sorted string to the console. You can assume that the string will only contain letters.

string = input().lower()
length = len(string)
word = ''

text = 'abcdefghijklmnopqrstuvwxyz'

for char in text:
    for i in range(0, length):
        if char == string[i]:
            word += char 

print(word)

# GRPA - 5
# Accept a phone number as input. A valid phone number should satisfy the following constraints.
# (1) The number should start with one of these digits: 6, 7, 8, 9
# (2) The number should be exactly 10 digits long.
# (3) No digit should appear more than 7 times in the number.
# (4) No digit should appear more than 5 times in a row in the number.
# If the fourth condition is not very clear, then consider this example: the number 9888888765 is invalid because the digit 8 appears more than 5 times in a row.
# Print the string valid if the phone number is valid. If not, print the string invalid.

number = input()
isvalid = True

if len(number) == 10 and number[0] in '6789':
    for i in range(0, len(number)):
        if number.count(number[i]) > 7:
            isvalid = False
            break
        if 6 * number[i] in number:
            isvalid = False
            break
    else:
        isvalid = True

if isvalid:
    print("VALID")
else:
    print("INVALID")

# GRPA - 6
# Accept a positive integer n as input and print a "number arrow" of size n. 
# For example, n=5 should produce the following output:
# 1
# 12
# 123
# 1234
# 12345
# 1234
# 123
# 12
# 1
# You can assume that n≥2 for all test cases.

n = int(input())

# First half lines that is from 0 to n-1 lines
for i in range(n):
    for j in range(i+1):
        if i == j:
            print(j+1, end='')
        else:
            print(j+1, end=',')
    print()

# Second half that is from n upto (n*2)-1 lines
for k in range(n, n*2):
    for m in range(1, n):
        if (n-1) == m:
            print(m, end='')
        else:
            print(m, end=',')
    print()
    


    