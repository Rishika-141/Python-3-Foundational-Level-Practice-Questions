#PPA-3 - 2024 
#Accept an integer as input and print its square as output.
num = int(input())
square = num ** 2
print(square)

#PPA-4
#Accept two integers as input and print their sum as output.
num1 = int(input())
num2 = int(input())
print(num1 + num2)

#PPA-5
#Accept two words as input and print the two words after adding a space between them.
word1 = input()
word2 = input()
print(word1 + " " + word2)

#PPA-6
#Accept the registration number of a vehicle as input and print its state-code as output.
reg_no = input()
print(reg_no[:2])

#PPA-7
#Accept a five digit number as input and print the sum of its digits as output.
number = input()
n1 = int(number[0])
n2 = int(number[1])
n3 = int(number[2])
n4 = int(number[3])
n5 = int(number[4])
print(n1+n2+n3+n4+n5)

#PPA-9
# A simple algorithm has to be designed to find out whether a student belongs to the Data Science branch or not. 
# The input will be a student's roll number, which is of the form BR18B0000.
# Here, BR represents the branch code, 18 represents the year of joining, B represents the education level and 
# 0000 represents the specific identification given to the student of that batch. 
# The branch code for Data Science is DS Print True if the student belongs to Data Science branch and False otherwise.
roll_no = input()
branch_code = roll_no[:2]
if branch_code == 'DS':
    print(True)
else:
    print(False)

#PPA - 10
# The police are trying to track a criminal based on the evidence available at a crime site. Their main clue is a vehicle's damaged number plate. 
# Only the string TN07 is visible. The format of the registration number is AA00AA00,
# where the first two letters are alphabets, next two are numbers, next two are again alphabets followed by two numbers at the end.
# A number plate is picked from a database of registration numbers and is given to you as input. 
# Your task is to determine if this could belong to the criminal or not. 
# Print True if the number plate contains TN07 and False otherwise.
num_plate = input()
if(num_plate[:4] == "TN07" or num_plate[4:] == "TN07"):
    print(True)
else:
    print(False)

#PPA - 11
# Accept two integers a and b as input and print the absolute difference of both the numbers. 
# For example, if a=9,b=8, then the absolute difference is 9−8=1. So, your output should be 1.
# You should be able to solve this problem using the concepts covered in this week.
a = int(input())
b = int(input())
square = (a-b)**2
root = square**0.5
print(int(root)) #As the above line will give result in floating value

#PPA-12
# You are given a string and two non-negative integers as input. 
# The two integers specify the start and end indices of a substring in the given string. 
# Create a new string by replicating the substring a minimum number of times so that the resulting string is longer than the input string.
# The input parameters are the string, start index of the substring and the end index of substring (endpoints inclusive) each on a different line.
string = input()
start = int(input())
end = int(input())
new_word = string[start:end+1]
total_length = len(string)
min_rep = total_length // (end - start + 1) + 1
print(new_word*min_rep)

#PPA-13
# Accept a positive integer x as input, compute the value of this continued fraction and store the result in a variable named cfrac. 
# We will round off your answer to exactly two decimal places. You don't have to print the output to the console, we will take care of that.
x = int(input())
x0 = x + 1/x 
x1 = x + 1/x0
x2 = x + 1/x1 
x3 = x + 1/x2 
cfrac = x + 1/x3 
print(cfrac)