# Lists 
# PPA - 1
# Accept a positive integer n as input and print the list of first n positive integers as output.

n = int(input())
positive_list = []
for i in range(1, n+1):
    positive_list.append(i)
print(positive_list)

# PPA - 2
# Accept a sequence of words as input, append all these words to a list in the order in which they are entered, and print this list as output. 
# The first line in the input is a positive integer n that denotes the number of words in the sequence. 
# The next n lines will have one word on each line.

n = int(input())
wordlist = []
for i in range(n):
    word = input()
    wordlist.append(word)
print(wordlist)

# PPA - 3
# Accept a sequence of comma-separated integers as input and print the maximum value in the sequence as output.

num = input()
L = num.split(',')
maxn = int(L[0])
for i in range(len(L)):
    if int(L[i]) > maxn:
        maxn = int(L[i])
print(maxn)
    
# PPA - 4
# A list L of words is already given to you as a part of the prefix code. Print the longest word in the list. 
# If there are multiple words with the same maximum length, print the one which appears at the rightmost end of the list.

word = input().split(',')
length = len(word[0])
output = word[0]
for i in range(len(word)):
    if len(word[i]) >= length:
        length = len(word[i])
        output = word[i]
print(output)

# PPA - 5
# Accept a space-separated sequence of positive real numbers as input. 
# Convert each element of the sequence into the greatest integer less than or equal to it. 
# Print this sequence of integers as output, with a comma between consecutive integers.

L = input().split(' ')

for i in range(len(L)):
    L[i] = float(L[i])
    L[i] = int(L[i])

for i in range(len(L)):
    if i != len(L) - 1:
        print(L[i], end=',')
    else:
        print(L[i], end='')

# PPA - 6
# Accept a sequence of comma-separated words as input. 
# Reverse the sequence and print it as output.

L = input().split(',')
reverse = []
for i in range(len(L)):
    reverse = [L[i]] + reverse # Prepends the list and give a reverse order list

for i in range(len(reverse)):
    if i != len(reverse) - 1:
        print(reverse[i], end=',')
    else:
        print(reverse[i], end='')

# PPA - 7
# Accept a square matrix as input and store it in a variable named matrix. 
# The first line of input will be, n, the number of rows in the matrix. 
# Each of the next n lines will have a sequence of n space-separated integers.

row_no = int(input())
matrix = []
for i in range(row_no):
    L = []
    for num in input().split(' '):
        L.append(int(num))
    matrix.append(L)
print(matrix)

# PPA - 8
# An identity matrix is a square matrix which has ones on the main diagonal and zeros everywhere else. 
# For example, the identity matrix of size 3×3 is: [[1,0,0], [0,1,0], [0,0,1]] 
# Accept a positive integer n as input and print the identity matrix of size n×n. 
# Your output should have n lines, where each line is a sequence of n comma-separated integers that corresponds to one row of the matrix.

row = int(input())

identity_matrix = []

for i in range(row):
    L = []
    for j in range(row):
        if i == j:
            L.append(1)
        else:
            L.append(0)
    identity_matrix.append(L)

print(identity_matrix)

# PPA - 9
# Accept a square matrix A and an integer s as input and print the matrix s⋅A as output. 
# Multiplying a matrix by an integer s is equivalent to multiplying each element of the matrix by s. 
# The first line of input is a positive integer n, that denotes the dimension of the matrix A. 
# Each of the next n lines contains a sequence of space-separated integers. 
# The last line of the input contains the integer s.
# Print the matrix s⋅A as output. Each row of the matrix must be printed as a sequence of space separated integers, one row on each line. 
# There should not be any space after the last number on each line. 
# If the expected output looks exactly like the actual output and still you are getting a wrong answer, it is because of the space at the end.

n = int(input())

m = []
for i in range(n):
    L = []
    for num in input().split(' '):
        L.append(int(num))
    m.append(L)

s = int(input())
for row in range(n):
    for col in range(n):
        m[row][col] *= s

for row in range(n):
    for col in range(n):
        if col != n-1:
            print(m[row][col], end=' ')
        else:
            print(m[row][col])

# PPA - 10
# Accept two square matrices A and B of dimensions n×n as input and compute their sum A+B.
# The first line will contain the integer n. This is followed by 2n lines. 
# Each of the first n lines is a sequence of comma-separated integers that denotes one row of the matrix A. 
# Each of the last n lines is a sequence of comma-separated integers that denotes one row of the matrix B.
# Your output should again be a sequence of n lines, where each line is a sequence of comma-separated integer that denotes a row of the matrix A+B.

dimension = int(input())

# matrix A
A = []
for i in range(dimension):
    L = []
    for num in input().split(','):
        L.append(int(num))
    A.append(L)

# matrix B
B = []
for j in range(dimension):
    M = []
    for number in input().split(','):
        M.append(int(number))
    B.append(M)

# Matrix C = [[0], [0]]
C = []
for i in range(dimension):
    row = []
    for j in range(dimension):
        row.append(0)
    C.append(row)

# C = A + B
for i in range(dimension):
    for j in range(dimension):
        C[i][j] = A[i][j] + B[i][j]
        if j != dimension - 1:
            print(C[i][j], end=',')
        else:
            print(C[i][j])

# PPA - 11
# L is a list of real numbers that is already given to you. 
# You have to sort this list in descending order and store the sorted list in a variable called sorted_L.

L = input().split(',')

flist = []
for x in L:
    flist.append(float(x))
    
sorted_L = [ ]

while flist != [ ]:
    max_num = flist[0]
    for elem in flist:
        if elem > max_num:
            max_num = elem
    flist.remove(max_num)
    sorted_L.append(max_num)

print(sorted_L)
