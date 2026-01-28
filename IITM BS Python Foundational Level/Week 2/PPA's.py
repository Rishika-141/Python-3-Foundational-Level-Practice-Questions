# PPA - 1
# Accept an integer as input. 
# Print positive if it is greater than zero and negative if it is less than zero. 
# You can assume that the input will be non-zero.

integer = int(input())
if integer > 0:
    print("Positive")
else:
    print("Negative")

# PPA - 2
# Consider the piece-wise function given below.
# f(x) = x + 2, if 0 < x < 10
# f(x) = x*2 + 2, if 10 <= x
# 0, otherwise
# Accept the value of x as input and print the value of f(x) as output. Note that both the input and output are real numbers. 
# Your code should reflect this aspect. That is, both x and f(x) should be float values.

x = float(input())
if x > 0 and x < 10:
    print(x + 2)
elif x >= 10:
    print((x**2) + 2)
else:
    print(0)

# PPA - 3
# Accept an integer as input and print the time of the day 

time = int(input())

if time >= 0 and time <= 5:
    print("NIGHT")

elif time >= 6 and time <= 11:
    print("MORNING")

elif time >= 12 and time <= 17:
    print("AFTERNOON")

elif time >= 18 and time <= 23:
    print("EVENING")

else:
    print("INVALID")

# PPA - 4
# Accept a point in 2D space as input and find the region in space that this point belongs to. 
# A point could belong to one of the four quadrants, or it could be on one of the two axes, or it could be the origin. 
# The input is given in 2 lines: the first line is the x-coordinate of the point while the second line is its y-coordinate.
# The possible outputs are first, second, third, fourth, x-axis, y-axis, and origin. 
# Any other output will not be accepted. Note that all outputs should be in lower case.

x = float(input())
y = float(input())

if x > 0 and y > 0:
    print("First Quadrant")
elif x > 0 and y < 0:
    print("Fourth Quadrant")
elif x < 0 and y > 0:
    print("Second Quadrant")
elif x < 0 and y < 0:
    print("Third Quadrant")
elif x > 0 or x < 0 and y == 0:
    print("x-axis")
elif x == 0 and y > 0 or y < 0:
    print("y-axis")
else:
    print("origin")

# PPA - 5
# Write a program to realize the equation of a line given 2 points (x1, y1) and (x2, y2) in 2D space. 
# The input is in 5 lines where, the first, second, third, and fourth lines represents x1, y1, x2 and y2 respectively.
# The fifth line corresponds to x3, Determine y3 using the equation of the straight line as given below:
# (x-x1)/(x2-x1) = (y-y1)/(y2-y1)
# The output should be "Vertical Line" if the line is vertical. 
# In other cases, the output should be 2 lined, where the first line is the value of y3 and the second line indicates whether the slope of the line is positive, negative or zero. 
# Print "Positive Slope", "Negative Slope" or "Horizontal Line" accordingly.
# Note that all inputs are to be processed as real numbers.

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())

if((x2 - x1) != 0):
    m = (y2 - y1)/(x2 - x1)

    # Slope of a line 
    y3 = (m * (x3 - x1)) + y1
    print(y3)
    
    if m > 0:
        print("Positive Slope")
    
    elif m < 0:
        print("Negative Slope")

    else:
        print("Horizontal Line")

else:
    print("Vertical Line")

# PPA - 6
# Accept a string as input. If the input string is of odd length, then continue with it. 
# If the input string is of even length, make the string of odd length by following the two steps mentioned below:
# (1) If the last character is a period (.), then remove it
# (2) If the last character is not a period, then add a period (.) to the end of the string
# Call this string of odd length word. 
# Select a substring made up of three consecutive characters from word such that there are an equal number of characters to the left and right of this substring. 
# Print this substring as output. You can assume that all input strings will be in lower case and will have a length of at least four.

string = input()

if len(string) % 2 == 0:
    
    if string[-1] == ".":
        word = string[0:-1]
    else:
        word = string + "."
    
    n = len(word) // 2
    start = n - 1
    end = (len(word) - n) + 1
    new_word = word[start:end]
    print(new_word)

else:
    n = len(string) // 2
    start = n - 1
    end = (len(string) - n) + 1
    new_word = string[start:end]
    print(new_word)
    
    
# PPA - 7
# A sequence of five words is called "Magical" if the ith word is a substring of the (i+1)th word for every i in the range 1 ≤ i < 5. 
# Accept a sequence of five words as input, one word on each line. Print magical if the sequence is magical and non-magical otherwise.
# Note that str_1 is a substring of str_2 if and only if str_1 is present as a sequence of consecutive characters in str_2.

string1 = input()
string2 = input()
string3 = input()
string4 = input()
string5 = input()

if(string1 in string2 and string2 in string3 and 
   string3 in string4 and string4 in string5):
    print("Magical")
else:
    print("Non-Magical")

# PPA - 8 
# Accept two positions as input: start and end. 
# Print YES if a bishop at start can move to end in exactly one move. 
# Print NO otherwise. Note that a bishop can only move along diagonals.

start = input()
end = input()

word = "ABCDEFGHIJK"
num = "123456789"

start_col, end_col = start[0], end[0]
start_row, end_row = start[-1], end[-1]

col_diff = abs(word.index(start_col) - word.index(end_col))
row_diff = abs(word.index(start_row) - word.index(end_row))

if col_diff == row_diff:
    print("YES")
else:
    print("NO")

# PPA - 9
# You have n gold coins with you. You wish to divide this among three of your friends under the following conditions:
# (1) All three of them should get a non-zero share.
# (2) No two of them should get the same number of coins.
# (3) You should not have any coins with you at the end of this sharing process.
# The input has four lines. The first line contains the number of coins with you. The next three lines will have the share given to your three friends. 
# All inputs shall be non-negative integers. If the division satisfies these conditions, then print the string FAIR. If not, print UNFAIR.

n = int(input())
friend1_share = int(input())
friend2_share = int(input())
friend3_share = int(input())
fair_share = False

if(friend1_share != 0 and friend2_share != 0 and friend3_share != 0):
    if(friend1_share != friend2_share and friend2_share != friend3_share and
       friend3_share != friend1_share):
        if((friend1_share + friend2_share + friend3_share) == n):
            fair_share = True

if(fair_share == True):
    print("FAIR")
else:
    print("UNFAIR")            

# PPA - 10
# Accept a real number x as input and print the greatest integer less than or equal to x on the first line, 
# followed by the smallest integer greater than or equal to x on the second line.

x = float(input())
n = int(x)

if(x == n):
    print(n)
    print(n)

elif(n >= 0):
    print(n)
    print(n + 1)

else:
    print(n - 1)
    print(n)

# PPA - 11
# A class teacher has decided to split her entire class into four groups, namely Sapphire, Peridot, Ruby, and Emerald for sports competitions.
# For dividing the students into these four groups, she has followed the pattern given below:
# Sapphire 1 5 9 13 17 21...
# Peridot 2 6 10 14 18 22...
# Ruby 3 7 11 15 19 23...
# Emerald 4 8 12 16 20 24...
# All the students are represented by their roll numbers. 
# Based on the above pattern, given the roll number as input, print the group the student belongs to as output.

roll_no = int(input())

if(roll_no % 4 == 1):
    print("Sapphire")
elif(roll_no % 4 == 2):
    print("Peridot")
elif(roll_no % 4 == 3):
    print("Ruby")
else:
    print("Emerald")

# PPA - 12
# A data science company wants to hire data scientists from IIT Madras. The company follows a certain criteria for selection: for a student to be selected, 
# the number of backlogs should be at most 5 and the CGPA (Cumulative Grade Point Average) should be greater than 6.
# If the student does not fit the above criteria, then the student is not offered the job. 
# If the student is selected, then the salary offered is equal to 5 times his/her CGPA (in lakhs).
# Accept the number of backlogs (integer) and the CGPA (float) of the student as input. 
# Your task is to determine if the student is selected or not. 
# If the student is selected, then print the package. 
# If not, then print the string Not Selected.

backlog_num = int(input())
cgpa = float(input())

# Selected criteria
if(backlog_num >= 0 and backlog_num <= 5 and cgpa > 6.0):
    salary = 5 * cgpa
    print(salary)
else:
    print("Not Selected")

# PPA - 13
# A test match happened between Team A and Team B. The scores of the teams in both the innings are given as input in eight lines in the format given below. 
# The first two lines represent the scores of Team A in the first innings and the next two lines represent the scores of Team A in the second innings. 
# Likewise, the last four lines represent the scores of Team B in both the innings.
# The numbers in 2nd, 4th, 6th, and 8th lines represent the wickets lost by the teams and the numbers in 1st, 3rd, 5th, and 7th represent the runs scored. 
# For example: 120
#              10
#              210
#              10
#              115
#              10
#              189
#              10
# In the above example, team-A has scored 120 for the loss of 10 wickets in the first innings, 
# and 210 for the loss of 10 wickets in the second innings. Team A plays first and Team B plays second. Your task is to determine the winner of the match.
# Process to decide the outcome
# Team A wins if and only if the sum of its scores in both the innings is greater than sum of the scores of Team B in both the innings AND Team B lost all the ten wickets in the second innings. 
# Team B wins if the sum of its scores in both the innings is greater than sum of the scores of Team A in both the innings.
# A match will end in a draw if the sum of scores in the two innings of both the teams are equal OR if Team B did not lose all the ten wickets in the second innings. 
# If the match ends in a draw, then print DRAW.

# Team A
teamA_score1 = int(input())
wicket1_A = int(input())
teamA_score2 = int(input())
wicket2_A = int(input())

# Team B
teamB_score1 = int(input())
wicket1_B = int(input())
teamB_score2 = int(input())
wicket2_B = int(input())

# Condition for Team A wins
if((teamA_score1 + teamA_score2) > (teamB_score1 + teamB_score2) and wicket2_B == 10):
    print("Team A is the winner")

# Condition for the match to get DRAW
elif((teamA_score1 + teamA_score2) < (teamB_score1 + teamB_score2)):
    print("Team B is the winner")

else:
    print("The match is DRAW")

# PPA - 14
# A word is said to be perfect if it satisfies all the following criteria:
# (1) All the vowels (a,e,i,o,u) should be present in the word.
# (2) Let the vowels be represented as v1 = a, v2 = e, v3 = i, v4 = o, v5 = u in lexical order. 
# If i<j, then the first appearance of vi in the word should come before the first appearance of vj.
# If i<j, then the count of vi should be greater than or equal to the count of vj.
# Accept a word as input and do the following:
# (1) If it is a perfect word, print It is a perfect word
# (2) If the word is not a perfect word, print It is not a perfect word

word = input()
perfect_condition = False

if("a" in word and "e" in word and "i" in word and "o" in word and "u" in word):

    if(word.index("a") < word.index("e") and word.index("e") < word.index("i") and 
       word.index("i") < word.index("o") and word.index("o") < word.index("u")):
        
        if(word.count("a") >= word.count("e") and word.count("e") >= word.count("i") and
           word.count("i") >= word.count("o") and word.count("o") >= word.count("u")):
            perfect_condition = True

if(perfect_condition == True):
    print("It is a perfect word")
else:
    print("It is not a perfect word")        

# PPA - 15
# Accept four integers as input and write a program to print these integers in non-decreasing order.
# The input will be four integers in four lines. The output should be a single line with all the integers separated by a single space in non-decreasing order.
# Note: There is no space after the fourth integer.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# If a is smaller among all four of them
if(a <= b and a <= c and a <= d):
    if(b <= c and b <= d):
        if(c <= d):
            print(a, b, c, d, end=' ')
        else:
            print(a, b, d, c, end=' ')
    elif(c <= b and c <= d):
        if(b <= d):
            print(a, c, b, d, end=" ")
        else:
            print(a, c, d, b, end=' ')
    else:
        if(b <= c):
            print(a, d, b, c, end=' ')
        else:
            print(a, d, c, b, end=' ')
    
#If b is smaller among all four of them
elif(b <= a and b <= c and b <= d):
    if(a <= c and a <= d):
        if(c <= d):
            print(b, a, c, d, end=' ')
        else:
            print(b, a, d, c, end=' ')
    elif(c <= a and c <= d):
        if(a <= d):
            print(b, c, a, d, end=' ')
        else:
            print(b, c, d, a, end=' ')
    else:
        if(a <= c):
            print(b, d, a, c, end=' ')
        else:
            print(b, d, c, a, end=' ')

# If c is smaller among all of them
elif(c <= a and c <= b and c <= d):
    if(a <= b and a <= d):
        if(b <= d):
            print(c, a, b, d, end=' ')
        else:
            print(c, a, d, b, end=' ')
    elif(b <= a and b <= d):
        if(a <= d):
            print(c, b, a, d, end=' ')
        else:
            print(c, b, d, a, end=' ')
    else:
        if(a <= b):
            print(c, d, a, b, end=' ')
        else:
            print(c, d, b, a, end=' ')

# If d is smaller among of them
else:
    if(a <= b and a <= c):
        if(b <= c):
            print(d, a, b, c, end=' ')
        else:
            print(d, a, c, b, end=' ')
    elif(b <= a and b <= c):
        if(a <= c):
            print(d, b, a, c, end=' ')
        else:
            print(d, b, c, a, end=' ')
    else:
        if(a <= b):
            print(d, c, a, b, end=' ')
        else:
            print(d, c, b, a, end=' ')


