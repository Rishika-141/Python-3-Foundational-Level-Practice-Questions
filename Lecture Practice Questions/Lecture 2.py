# For Loop Questions
# Accept integer n, and print Hello n times
n = int(input())
for i in range(n):
    print("Hello")

# Print Natural Number upto n
num = int(input())
for i in range(1, num+1):
    print(i)

# Reverse for loop, Print n to 1
n1 = int(input())
for j in range(n1, 0, -1):
    print(j)

# Take a number as input and print its table
n = int(input())
print(f'The table of {n} is as follows: ')
for k in range(n, (n*10)+1, n):
    print(k)

# Sum upto n terms
# 5 = 1+2+3+4+5 = 15
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# Factorial of the number
n = int(input())
fact = 1
for i in range(n, 0, -1):
    fact *= i
print(fact)

# Print sum of all even & odd numbers in the range seperately
num = int(input())
even_sum = 0
odd_sum = 0
for i in range(1, num+1):
    if(i % 2 == 0):
        even_sum += i
    else:
        odd_sum += i
print(f'The sum of all even numbers within range specified is: {even_sum}')
print(f'The sum of all odd numbers within range specified is: {odd_sum}')

# Print all the factors of the number
input_num = int(input())
for j in range(1, input_num + 1):
    if(input_num % j == 0):
        print(f'The factors of {input_num} is {j}')
    else:
        pass

# Accept a number and check if it is a perfect number or not
# Perfect num = A number whose sum of all factors is the number itself
number = int(input())
sum = 0
for fact in range(1, number):
    if(number % fact == 0):
        sum += fact
    else:
        continue

if sum == number:
    print(f'{number} is a Perfect Number')
else:
    print(f'{number} is not a Perfect Number')

# Check whether the number is prime or not
num = int(input())
for divisor in range(2, num):
    if(num % divisor == 0):
        print(f'{num} is not a Prime Number')
        break
else:
    print(f'{num} is a Prime Number')

# Reverse a string without using in-built function
string = input()
word = string.lower()
reverse_string = ''
for i in range(len(string)-1, -1, -1):
    reverse_string += word[i]
print(reverse_string)

# Check whether the string is Pallindrome or not
string = input()
word = string.lower()
reverse_word = ''
for i in range(len(string)-1, -1, -1):
    reverse_word += word[i]

if(reverse_word == word):
    print(f'{word} is a Pallindrome')
else:
    print(f'{word} is not a Pallindrome')

# Count all letters, digits, and special symbols from a given string
# Given str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total Count of char, digits and symbols
# Chars = 8
# Digits = 3
# Symbols = 4
str1 = input()
chars = 0
digits = 0
symbols = 0

for i in str1:
    if(i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or i in 'abcdefghijklmnop'
    'qrstuvwxyz'):
        chars += 1
    elif(i in '1234567890'):
        digits += 1
    else:
        symbols += 1

print(f'Total char count: {chars}')
print(f'Total digits count: {digits}')
print(f'Total symbols count: {symbols}')

