# Accumulation - Accumulating a final result
# sum_until_0: Continuously read integers from standard input until you receive a zero.
# Print the sum of these integers

number = int(input())
sum_until_0 = 0

while(number != 0):
    sum_until_0 += number
    number = int(input())
print(sum_until_0)

# total_price: Continuously read pairs of integers from standard input, representing the quantity and price of items, until you receive the string "END". 
# Print the total price of all items.

quan_price = input()
total_price = 0

while(quan_price != 'END'):
    quantity = int(quan_price[0])
    price = int(quan_price[2:])
    qp = quantity * price
    total_price += qp
    quan_price = input()

print(total_price)

# Filtering - Selecting based on a criterion
# only_ed_or_ing: Continuously read strings from standard input until you encounter the word "STOP" (case insensitive and not included in the output). 
# Print only those strings that end with "ed" or "ing" (case insensitive).

strings = input()

while(strings != 'STOP'):
    if strings[-3:] == 'ing' or strings[-2:] == 'ed':
    #if strings.endswith('ing') or strings.endswith('ed'):
        print(strings)
    strings = input()

# reverse_sum_palindrome: Continuously read positive integers from standard input until you encounter a "-1"(not included in the output). 
# Print only those integers for which the sum of the number and its reverse is a palindrome.

num = int(input())
while(num != -1):
    n = num
    reverse_no = 0
    while(n > 0):
        rem = n % 10
        reverse_no = reverse_no * 10 + rem
        n //= 10
    reverse_sum = num + reverse_no
    n1 = reverse_sum
    reverse_sum_num = 0
    while(n1 > 0):
        remainder = n1 % 10
        reverse_sum_num = reverse_sum_num * 10 + remainder
        n1 //= 10
    if(reverse_sum == reverse_sum_num):
        print(num)
        
    num = int(input())

# Mapping - Applying the same operation to different items
# double_string: Continuously read lines from standard input until an empty line is encountered. 
# Print each line repeated twice.

line = input()
while line != '':
    print(line * 2)
    line = input()

# odd_char: Continuously read strings from standard input until you encounter a string ending with a "."(include that string with the "." in the output). 
# Extract characters at odd positions (starting from 1) of each line, and print the results in a single line separated by spaces.

word = input()
while(word[-1] != '.'):
    print(word[0::2], end=' ')
    word = input()
print(word[0::2], end=' ')

# Filter and Map - Applying an operation to selected items
# only_even_squares: Continuously read numbers from standard input until "NAN" is encountered. 
# Print the square of each number only if it is even.

number = input()

while(number != 'NAN'):
    num = int(number)
    if num % 2 == 0:
        print(num ** 2)
    number = input()

# Filter and Accumulate - Accumulating a result with selected items
# only_odd_lines: Continuously read lines from standard input until "END"(not included in the output) is encountered. 
# Create a string by prepending only the odd lines (starting from 1) with a newline character in between, and print the result which will be the odd lines in reverse order.

result = ''
line_no = 1
while True:
    line = input()
    if line == 'END':
        break
    if line_no % 2:
        result = line + "\n" + result #Prepending the next odd line
    line_no += 1
print(result)