# Functions
# PPA - 1
# The factorial of a positive integer n is the product of the first n positive integers.
# Write a function named factorial that accepts an integer n as argument. It should return the factorial of n if n is a positive integer. It should return −1 if n is a negative integer, and it should return 1 if n is zero.

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return -1
    else:
        fact = 1
        for i in range(n, 1, -1):
            fact = fact * i
        return fact

num = int(input())
print(factorial(num))

# PPA - 2
# In the Gregorian calendar, a leap year has a total of 366 days instead of the usual 365 as a result of adding an extra day (February 29) to the year. 
# This calendar was introduced in 1582 to replace the flawed Julian Calendar. 
# The criteria given below are used to determine if a year is a leap year or not.
# If a year is divisible by 100 then it will be a leap year if it is also divisible by 400.
# If a year is not divisible by 100, then it will be a leap year if it is divisible by 4.
# Write a function named check_leap_year that accepts a year between 1600 and 9999 as argument. 
# It should return True if the year is a leap year and False otherwise.

def check_leap_year(year):
    
    if year % 100 == 0 and year % 400 == 0:
        return True
    
    elif year % 100 != 0 and year % 4 == 0:
        return True
    
    else:
        return False

leap_year = int(input("Enter the year: "))
print(check_leap_year(leap_year))

# PPA - 3
# Write a function maxval that accepts three integers a, b and c as arguments. It should return the maximum among the three numbers.

def maxval(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

x = int(input())
y = int(input())
z = int(input())

print(maxval(x, y, z))

# PPA - 4
# Write a function named dim_equal that accepts two matrices A and B as arguments. 
# It should return True if the the dimensions of both matrices are the same, and False otherwise.
# You do not have to accept input from the user or print output to the console. You just have to write the function definition.

def dim_equal(A, B):
    dimA = len(A)
    dimB = len(B)
    innerdimA = len(A[0])
    innerdimB = len(B[0])

    if dimA == dimB and innerdimA == innerdimB:
        return True
    else:
        return False

# PPA - 5
# Write a function named first_three that accepts a list L of distinct integers as argument. 
# It should return the first maximum, second maximum and third maximum in the list, in this order. 
# You can assume that the input list will have a size of at least three.
# You do not have to accept input from the user or print output to the console. You just have to write the function definition.

def first_three(L):
    fmax = max(L)
    L.remove(fmax)
    smax = max(L)
    L.remove(smax)
    tmax = max(L)
    return fmax, smax, tmax

# PPA - 6 - how to take call another function inside the another function
# A class of English words is called mysterious if it satisfies certain conditions. These conditions are hidden from you. Instead, you are given a function named mysterious that accepts a word as argument and returns True if the word is mysterious and False otherwise.
# Write a function named type_of_sequence that accepts a list of words as an argument. 
# Its return value is a string that depends on the number of mysterious words in the sequence. 
# The exact conditions are given in the following table. 
# If k denotes the number of mysterious words in the sequence, then:
# k < 2 -> mildly mysterious
# k >= 2 and k < 5 -> moderately mysterious
# k >= 5 -> most mysterious
# You do not have to accept input from the user or print output to the console. You just have to write the function definition.

def type_of_sequence(words):
    count = 0
    # for string in words:
    #     if mysterious:
    #         count += 1
    
    if count < 2:
        return "mildly mysterious"
    elif count >= 2 and count < 5:
        return "moderately mysterious"
    else:
        return "most mysterious"

# PPA - 7 - how to create multiple functions 
# In a throwback to CT days, write the definition of the following five functions, all of which accept a list L as argument.
# (1) is_empty: return True if the list is empty, and False otherwise.

# (2) first: return the first element if the list is non-empty, return None otherwise.

# (3) last: return the last element if the list is non-empty, return None otherwise.

# (4) init: return the first n−1 elements if the list is non-empty and has size n, return None otherwise. 
# Note that if L has just one element, init(L) should return the empty list.

# (5) rest: return the last n−1 elements if the list is non-empty and has size n, return None otherwise. 
# Note that if L has just one element, rest(L) should return the empty list.

def is_empty(L):
    if L == []:
        return True
    else:
        return False
    
def first(L):
    if L != []:
        return L[0]
    else:
        return "None"

def last(L):
    if L != []:
        return L[-1]
    else:
        return "None"

def init(L):
    if L != []:
        n = len(L)
        if n > 1:
            return L[0:n-1]
        else:
            return []
    else:
        return "None"
    
def rest(L):
    if L != []:
        n = len(L)
        if n > 1:
            return L[1:n]
        else:
            return []
    else:
        return "None"

print(first([1, 2, 3]))
print(last([1, 2, 3, 4]))
print(is_empty([ ]))
print(is_empty([1, 2]))
print(first([ ]))
print(first([-1, 10, 2]))
print(last([ ]))
print(last([10, 0, -100]))
print(init([ ]))
print(init([1, 2, 3, 4, 5]))
print(rest([ ]))
print(rest([1, 2, 3, 4, 5, 6]))

# PPA - 8
# Write a recursive function named fibo that accepts a positive integer n as argument and returns the nth Fibonacci number. 
# For this problem, F1=F2=1 are the first two Fibonacci numbers.
# You do not have to accept input from the user or print output to the console. You just have to write the function definition.

def fibo(n):
    if n <= 2:
        return 1
    return (fibo(n-1) + fibo(n-2))

# PPA - 9
# Implement the following functions.
# (1) Write a function named get_column that accepts a matrix named mat and a non-negative integer named col as arguments. 
# It should return the column that is at index col in the matrix mat as a list. 
# Zero-based indexing is used here.
# (2) Write a function named get_row that accepts a matrix named mat and a non-negative integer named row as arguments. 
# It should return the row that is at index row in the matrix mat as a list. 
# Zero-based indexing is used here.
# You do not have to accept input from the user or print output to the console. 
# You just have to write the definition of both the functions. 
# Each test case will correspond to one function call.

def get_column(mat, col):
    col_mat = [ ]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j == col:
                col_mat.append(mat[i][j])
    return col_mat

def get_row(mat, row):
    row_mat = [ ]
    for i in range(len(mat)):
        if i == row:
            for j in range(len(mat[i])):
                row_mat.append(mat[i][j])
    return row_mat

# PPA - 10
# Write a function insert that accepts a sorted list L of integers and an integer x as input. 
# The function should return a sorted list with the element x inserted at the right place in the input list. 
# The original list should not be disturbed in the process.
# (1) The only built-in methods you are allowed to use are append and remove. 
# You should not use any other method provided for lists
# (2) You do not have to accept input from the user or print output to the console. 
# You just have to write the function definition.

def insert(L, x):

    sortedl = [ ]
    inserted = False

    for number in L:
        if (not inserted) and (number > x):
            sortedl.append(x)
            inserted = True
        sortedl.append(number)
    
    if (not inserted):
        sortedl.append(x)
    
    return sortedl
    

