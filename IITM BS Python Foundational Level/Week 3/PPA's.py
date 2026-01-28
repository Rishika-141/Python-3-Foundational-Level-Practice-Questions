# Week - 3 - Questions based on for and while loop

# PPA - 1
# Accept a positive integer n as input and print the first n positive integers, 
# one number on each line.

n = int(input())
for i in range(1, n+1):
    print(i)

# PPA - 2
# Accept a positive integer n as input and print all the factors of n, 
# one number on each line.

n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i)
    else:
        pass 

# PPA - 3
# Accept two positive integers a and b as input. 
# Print the sum of all integers in the range [1000,2000], endpoints inclusive, 
# that are divisible by both a and b. 
# If you find no number satisfying this condition in the given range, then print 0.

a = int(input())
b = int(input())
sum = 0
for num in range(1000, 2001):
    if(num % a == 0 and num % b == 0):
        sum += num
print(sum)

# PPA - 4
# Accept a positive integer n as input, where n>1. 
# Print PRIME if n is a prime number and NOTPRIME otherwise

n = int(input())
isprime = True

for i in range(2, n):
    if n % i == 0:
        isprime = False
        break

if(isprime == True):
    print("PRIME")
else:
    print("NOTPRIME")

# PPA - 5
# Accept a sequence of positive integers as input and print the the maximum number in the sequence. 
# The input will have n+1 lines, where n denotes the number of terms in the sequence. 
# The ith line in the input will contain the ith term in the sequence for 1≤i≤n. 
# The last line of the input will always be the number 0. Each test case will have at least one term in the sequence.

n = int(input())
maximum = 0
while(n != 0):
    if n > maximum:
        maximum = n
    n = int(input())
print(maximum)

# PPA - 6
# Accept a sequence of words as input and print the the shortest word in the sequence. 
# The input will have n+1 lines, where n denotes the number of terms in the sequence. 
# The ith line in the input will contain the ith word in the sequence for 1≤i≤n.
# The last line of the input will always be the string abcdefghijklmnopqrstuvwxyz. 
# This string is not a part of the sequence. 
# You can assume that each test case corresponds to a non-empty sequence of words. 
# If there are multiple words that have the same minimum length, print the first such occurrence.

word = input()
minimum_word = word
while(word != 'abcdefghijklmnopqrstuvwxyz'):
    total_len = len(word)
    if total_len == len(minimum_word):
        if word[0] < minimum_word[0]:
            minimum_word = word
        else:
            minimum_word = minimum_word
    else:
        if total_len < len(minimum_word):
            minimum_word = word
        else:
            minimum_word = minimum_word
    word = input()
print(minimum_word)

# PPA - 7
# Accept a positive integer as input and print the sum of the digits in the number.

num = int(input())
sum = 0
while(num != 0):
    rem = num % 10
    sum += rem
    num //= 10
print(sum)

# PPA - 8
# Accept a positive integer n as input and print the first n integers on a line separated by a comma.

n = int(input())
for i in range(1, n+1):
    if i != n:
        print(i, end=',')
    else:
        print(i)

# PPA - 9
# Accept a positive integer n as input and print a triangle of zeros for n lines.
# The ith line should have i zeros. There shouldn't be any spaces between consecutive zeros. 
# Do not print a space at the end of a line.

n = int(input())
for i in range(n):
    for j in range(i+1):
        print(0, end=' ')
    print()

# PPA - 10
# Accept a positive integer n as input and print the sum of all prime numbers in the range [1,n] 
# endpoints inclusive. If there are no prime numbers in the given range, then print 0.

n = int(input())
primesum = 0
for num in range(2, n+1):
    factors = 0
    div = 2
    while(div <= num):
        if num % div == 0:
            factors += 1
        div += 1
    if factors == 1:
        primesum += num

print(primesum)

# PPA - 11
# Accept a positive integer n as input and find all solutions to the equation:
# x*2 + y*2 == z*2
# subject to the following constraints:
# (1) x, y and z are positive integers
# (2) x<y<z<n
# Print each solution triplet on one line — x,y,z — with a comma between consecutive integers. 
# The triplets should be printed in ascending order. 
# If you do not find any solutions satisfying the given constraints, print the string NO SOLUTION as output.

n = int(input())
num = 0
for x in range(1, n):
    for y in range(x+1, n):
        for z in range(y+1, n):
            if x**2 + y**2 == z**2:
                print(f'{x},{y},{z}')
                num += 1
if num == 0:
    print("NO SOLUTIONS")
     

# PPA - 12
# Accept two strings as input and form a new string by removing all characters from the second string which are present in the first string. 
# Print this new string as output. 
# You can assume that all input strings will be in lower case.

string1 = input()
string2 = input()
temp = ''
for i in range(0, len(string1)):
    for j in range(0, len(string2)):

        if(string1[i] == string2[j]):
            continue
        else:
            temp += string2[j]

    string2, temp = temp, ''

print(string2)

# PPA - 13
# Accept a string as input and print PALINDROME if it is a palindrome, and NOT PALINDROME otherwise.

word = input()
new_word = ''
for char in range(len(word)-1, -1, -1):
    new_word += word[char]

if word[0:] == new_word[0:]:
    print("PALINDROME")
else:
    print("NOT PALINDROME")

# PPA - 14
# Two integers are co-prime if the only common divisor between the two integers is one.
# Accept two positive integers as input in two different lines. 
# Print Coprime if the two integers are co-prime, else print Not Coprime. 
# Assume that both the integers are greater than two.

num1 = int(input())
num2 = int(input())
coprime = True

for i in range(2, num1):
    if num1 % i == 0:
        if num2 % i == 0:
            coprime = False
            break

if coprime:
    print("COPRIME NUMBERS")
else:
    print("NOT COPRIME")

# PPA - 15
# Accept a string as input, print Integer if the string is an integer, print Float if it a float, else print None.

n = input()

chars = '0123456789.'

isstring = False

for i in n:
    if i not in chars:
        isstring = True

if not isstring:
    if '.' in n and n.count('.') == 1:
        print("FLOAT")
    elif n.count(".") == 0:
        print("INTEGER")
    else:
        print("NONE")
else:
    print("NONE")

# PPA - 16
# Multiple Select Questions (MSQ) could have more than one correct answers. The marks scored by a student in a MSQ will be determined by the following conditions:
# (1) If the question has c correct options, each individual correct option carries n/c marks.
# (2)  If a student selects any of the wrong options, the marks awarded for the question will be 0.
# Calculate the marks obtained by the student and print this as float value.
# The input contains four lines.
# (1) First line is the number of marks for the question.
# (2) Second line contains the number of options for the question.
# (3) Third line is a comma-separated sequence of correct options for this question.
# (4) Fourth line is a comma-separated sequence of options given by the student.
# Write a program to print the number of marks scored by a student.

n = int(input())
total_opt = int(input())
correct = input()
c = (len(correct) + 1) // 2
selected = input()
marks = 0.0

for i in range(0, len(selected), 2):
    if selected[i] in correct:
        marks += n/c
    else:
        marks = 0.0

print(marks)

# PPA - 17
# Consider two non-empty strings a and b of lengths n1 and n2  respectively, which contain only numbers as their characters. 
# Both the strings are in ascending order, that is a[i] ≤ a[j] for 0≤i<j<n1 
# The same holds true for b. 
# You need to merge both the strings into one string of length n1 + n2 such that all the characters of this combined string are also in ascending order.
# Accept a and b as input and print this merged string as output.

a = input()
b = input()
n1 = len(a)
n2 = len(b)
n = n1 + n2
word = ''

while(n > 0):
    if len(a) == 0:
        word += b
        break
    elif len(b) == 0:
        word += a
        break
    else:
        if a[0] == b[0]:
            word += a[0] * 2
            a = a[1:]
            b = b[1:]
            n -= 2
        elif a[0] > b[0]:
            word += b[0]
            b = b[1:]
            n -= 1
        else:
            word += a[0]
            a = a[1:]
            n -= 1

print(word)
