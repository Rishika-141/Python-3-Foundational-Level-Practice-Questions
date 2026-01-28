#GRPA - 1
# Accept five words as input and print the sentence formed by these words after adding a space between consecutive words and a full stop at the end.
word1 = input()
word2 = input()
word3 = input()
word4 = input()
word5 = input()
print(word1 + ' ' + word2 + ' ' + word3 + ' ' + word4 + ' ' + word5 + '.')

#GRPA - 2
# Accept the date in DD-MM-YYYY format as input and print the year as output.
date = input()
print(date[6:])

#GRPA - 3
#Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers.
sequence = input()
n1 = int(sequence[0])
n2 = int(sequence[2])
n3 = int(sequence[4])
n4 = int(sequence[6])
n5 = int(sequence[-1])
print(n1*n2*n3*n4*n5)

#GRPA - 4
# Assume that several IITs start offering online degrees across multiple branches. The email-id of a student is defined as follows:
# branch_degree_year_roll@student.onlinedegree.institute.ac.in
# For example, if the email-id is CS_BT_21_7412@student.onlinedegree.iitm.ac.in, 
# then this student is from the computer science branch, pursuing a BTech degree from IITM, starting from the year 2021, with 7412 as the roll number. 
# branch, degree and year are codes of length two, while roll and institute are codes of length four. 
# Accept a student's email-id as input and print the following details, one item on each line:
# (1) Branch
# (2) Degree
# (3) Year
# (4) Roll number
# (5) Institute
email = input()
print("Branch: " + email[0:2])
print("Degree: " + email[3:5])
print("Year: " + email[6:8])
print("Roll number: " + email[9:13])
print("Institute: " + email[35:39])

#GRPA - 5
# Accept two positive integers x and y as input. 
# Print the number of digits in x^y. 
# You should be able to solve this problem using the concepts covered in week-1.
x = int(input())
y = int(input())
output = x**y
digits = len(str(output))
print(int(digits))

#GRPA - 6
# Accept two positive integers M and N as input. There are two cases to consider:
# (1) If M < N, then print M as output.
# (2) If M >= N, subtract N from M. Call the difference M1. 
# If M1 >= N, then subtract N from M1 and call the difference M2. 
# Keep doing this operation until you reach a value k, such that, Mk < N. 
# You have to print the value of Mk as output. 
# You should be able to solve this problem using the concepts covered in week-1.
M = int(input())
N = int(input())
if(M < N):
    print(M)
else:
    print(M % N)
