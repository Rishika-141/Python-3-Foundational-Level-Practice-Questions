# GRPA - 1
# The range of a list of numbers is the difference between the maximum and minimum values in the list.
# Write a function named get_range that accepts a list of real numbers as argument. It should return the range of the list.

num = input().split(',')
L = [ ]
for element in num:
    L.append(float(element))

def get_range(L):
    max_no = L[0]
    min_no = L[0]
    for i in range(len(L)):
        if L[i] > max_no:
            max_no = L[i]
        if L[i] < min_no:
            min_no = L[i]
    range_val = max_no - min_no
    return range_val

# GRPA - 2
# A perfect number is a positive integer that is equal to the sum of all its divisors excluding itself. For example, 6 is a perfect number as 6 = 1 + 2 + 3.
# Write a function named is_perfect that accepts a positive integer n as argument and returns True if it is perfect, and False otherwise.

num = int(input())

def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    
    if total == n:
        return True
    else:
        return False

# GRPA - 3
# The distance between two letters in the English alphabet is one more than the number of letters between them. 
# Alternatively, it can be defined as the number of steps needed to move from the alphabetically smaller letter to the larger letter. 
# This is always a non-negative integer. For example:
# Letter-1	Letter-2	Letter-Distance
#   a	        a	        0
#   a	        c	        2
#   a	        z	        25
#   z	        a	        25
#   e	        a	        4
# The distance between two words is defined as follows:
# It is -1, if the words are of unequal lengths.
# If the word-lengths are equal, it is the sum of the distances between letters at corresponding positions in the words. For example:
# dword(dog,cat)= dletter(d,c) + dletter(o,a)+ dletter(g,t) = 1+14+13=28
# Write a function named distance that accepts two words as arguments and returns the distance between them.

word1 = input()
word2 = input()

def distance(word1, word2):

    sentence = 'abcdefghijklmnopqrstuvwxyz'
    total_dist = 0

    if len(word1) != len(word2):
        return -1
    else:
        size = len(word1)
        for i in range(size):
            letter, word = word1[i], word2[i]
            diff = abs(sentence.index(letter) - sentence.index(word))
            total_dist += diff
        return total_dist
print(distance(word1, word2))

# GRPA - 4
# A n×n square matrix of positive integers is called a magic square if the following sums are equal:
# (1) row-sum: sum of numbers in every row; there are n such values, one for each row
# (2) column-sum: sum of numbers in every column; there are n such values, one for each column
# (3) diagonal-sum: sum of numbers in both the diagonals; there are two values
# There are n+n+2=2n+2 values involved. All these values must be the same for the matrix to be a magic-square.
# Write a function named is_magic that accepts a square matrix as argument and returns YES if it is a magic-square and NO if it isn't one.

# How can we take an input for such questions from user

n = int(input())  # dimension of matrix
mat = [ ]
while n != 0:
    rows = [ ]
    for i in input().split(' '):
        rows.append(int(i))
    mat.append(rows)
    n -= 1

# Now we will write function is_magic

def is_magic(mat):
    m = len(mat)
    # diagonal sum 
    d1sum , d2sum = 0, 0
    for i in range(m):
        d1sum += mat[i][i]
        d2sum += mat[i][(m-i-1)]
    
    if not(d1sum == d2sum):
        return 'NO'
    
    # row and column sum
    for i in range(m):
        rsum, csum = 0, 0
        for j in range(m):
            rsum += mat[i][j]
            csum += mat[j][i]
    
        if not(rsum == csum == d1sum):
            return 'NO'
    
    return 'YES'

# GRPA - 5
# Write a function named transpose that accepts a matrix mat as input and returns its transpose.

# How you will take input from an user
dim = input()
row = int(dim[0])
column = int(dim[-1])

n = row
mat = [ ]
while n != 0:
    rows = [ ]
    for i in input().split(','):
        rows.append(int(i))
    mat.append(rows)
    n -= 1

# Define functions transpose 
def transpose(mat):
    transpose_mat = [ ]
    for i in range(column):
        t = [ ]
        for j in range(row):
            t.append(mat[j][i])
        transpose_mat.append(t)
    return transpose_mat




