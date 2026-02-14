# GRPA - 1
# In the first line of input, accept a sequence of space-separated words. 
# In the second line of input, accept a single word. 
# If this word is not present in the sequence, print NO. 
# If this word is present in the sequence, then print YES and in the next line of the output, print the number of times the word appears in the sequence.

sentence = input().split(' ')
word = input()
count = 0
matched_word = False

for text in sentence:
    if word == text:
        count += 1
        matched_word = True

if matched_word:
    print('YES')
    print(count)
else:
    print('NO')

# GRPA - 2
# You are given a list marks that has the marks scored by a class of students in a Mathematics test. 
# Find the median marks and store it in a float variable named median. 
# You can assume that marks is a list of float values.
# Procedure to find the median
# (1) Sort the marks in ascending order. Do not try to use built-in methods.
# (2) If the number of students is odd, then the median is the middle value in the sorted sequence. 
# If the number of students is even, then the median is the arithmetic mean of the two middle values in the sorted sequence.

number = input().split(',')

# Convert the string into float
number_list = [ ]
for n in number:
    number_list.append(float(n))

# Arrange the number in ascending order
ascending = []
while number_list != [ ]:
    minimum = number_list[0]
    for i in range(len(number_list)):
        if number_list[i] < minimum:
            minimum = number_list[i]
    number_list.remove(minimum)
    ascending.append(minimum)

# Find the median of the list
length = len(ascending)
if length % 2 != 0:
    median = (length + 1) // 2
    print(ascending[median-1])
else:
    first = length // 2
    second = (length // 2) + 1
    median = (ascending[first-1] + ascending[second - 1]) / 2
    print(median)

# GRPA - 3
# Accept two square matrices A and B of dimensions n×n as input and compute their product AB.
# The first line of the input will contain the integer n. This is followed by 2n lines. 
# Out of these, each of the first n lines is a sequence of comma-separated integers that denotes one row of the matrix A. 
# Each of the last n lines is a sequence of comma-separated integers that denotes one row of the matrix B.
# Your output should again be a sequence of n lines, where each line is a sequence of comma-separated integers that denotes a row of the matrix AB.

dimension = int(input())

# Matrix A
A = []
for i in range(dimension):
    row = []
    for elements in input().split(','):
        row.append(int(elements))
    A.append(row)

# Matrix B
B = []
for j in range(dimension):
    row = []
    for elements in input().split(','):
        row.append(int(elements))
    B.append(row)

# Matrix C - creation 
C = []
for k in range(dimension):
    row = []
    for elements in range(dimension):
        row.append(0)
    C.append(row)

# C = Product of AB 
for i in range(dimension):
    for j in range(dimension):
        for k in range(dimension):
            C[i][j] += A[i][k] * B[k][j]
        
        if j != dimension - 1:
            print(C[i][j], end=',')
        else:
            print(C[i][j])

# GRPA - 4
# You are given the names and dates of birth of a group of people. 
# Find all pairs of members who share a common date of birth. 
# Note that this date need not be common across all pairs. 
# It is sufficient if both members in a pair have the same date of birth.
# The first line of input is a sequence of comma-separated names. 
# The second line of input is a sequence of comma-separated positive integers. 
# Each integer in the sequence will be in the range [1,365], endpoints inclusive, and stands for some day in the year.
# Find all pairs of names that share a common date of birth and store them in a list called common. 
# Each element of this list is itself a list, and should be of the form [name1, name2], such that name1 comes before name2 in alphabetical order.
# Notes
# (1) The pairs can be appended to the list common in any order. Only the names within a pair should be in dictionary order.
# (2) You can assume that each test case will have at least one pair of members who share the same date of birth.

name = input().split(',')
bday = input().split(',')

n = len(name)

for i in range(n):
    bday[i] = int(bday[i])

common = []
for i in range(n):
    for j in range(n):
        if((i != j) and bday[i] == bday[j] and name[i] < name[j]):
            pair = [name[i], name[j]]
            common.append(pair)

# Suppose we want an output to be in strings
output = []
for word in common:
    output.append(word[0] + ',' + word[1])
    result = '\n'.join(output)
print(result)

# GRPA - 5
# You are given a sequence of n points, (xi,yi), 1≤i≤n, in the 2-D plane as input. 
# Also, you are given a point P with coordinates (x,y). 
# Print all points in the sequence that are nearest to P. 
# If multiple points have the same least distance from P, print the points in the order of their appearance in the sequence.
# The first line of the input is an integer n, representing the number of points in the sequence. 
# Each of the next n lines contains the co-ordinates of a point separated by comma. 
# The last line contains the x and y co-ordinates of the point P. 
# Assume that all the x and y co-ordinates are integers.
# The distance between two points (x1,y1) and (x2,y2) is ((x1-x2)^2 + (y1-y2)^2)^0.5.
# You can assume that the maximum distance from P to any point will not exceed 1000.

n = int(input())

L = []
for i in range(n):
    L.append(input())

points = input().split(',')
x = int(points[0])
y = int(points[1])

min_list = []
min_dist = 1000

for j in range(n):
    temp = L[j].split(',')

    temp_x = int(temp[0])
    temp_y = int(temp[1])

    dist = ((x - temp_x)**2 + (y - temp_y)**2)**0.5

    if dist < min_dist:
        min_dist = dist
        min_list = [L[j]]
    elif dist == min_dist:
        min_list.append(L[j])

for point in min_list:
    print(point)
