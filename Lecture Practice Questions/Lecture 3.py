# While loop Questions

# Seperate each digit of the number and print it on the new line.
num = int(input())
while(num > 0):
    n = num % 10
    print(n)
    num = num // 10

# Hence the above code will print the number in reverse order on each line
# But to print it in the right order we can use another approach

# Approach 2
number = int(input())
new_num = str(number)
for i in new_num:
    no = int(i)
    print(f'{no} and {type(no)}')

# Accept a number and print its reverse.
number = int(input())
if(number > 0):
    rev = 0
    while(number > 0):
        rem = number % 10
        rev = rev * 10 + rem
        number //= 10
    print(rev)

elif(number == 0):
    print(0)

else:
    new_num = abs(number)
    reverse = ''
    rev_num = 0
    while(new_num > 0):
        num = new_num % 10
        rev_num = rev_num * 10 + num
        new_num //= 10
    reversed = str(rev_num)
    output = reverse + '-' + reversed
    final_op = int(output)
    print(f'{final_op} and {type(final_op)}')

# Accept a number and check if it is a pallindromic number 
# (if number and its reverse are equal)
number = int(input())
num = abs(number)
new_num = num
reverse = 0
while(new_num > 0):
    remainder = new_num % 10
    reverse = reverse * 10 + remainder
    new_num //= 10
if(num == reverse):
    print(f'{number} is a Pallindromic Number')
else:
    print(f'{number} is not a Pallindromic Number')

#Random Guess Number Game
import random

number = random.randint(1, 10)
trials = 0

while True:

    guess_number = int(input("Enter the number that you have guessed: "))


    if guess_number == number:
        trials += 1
        print(f'You have guessed the right number, {guess_number} is the right guess')
        print(f'The number of trials in which you have guessed the number right is: {trials}')
        break

    elif number < guess_number:
        print("Guess a number a little smaller than the number you have guessed now")
        trials += 1
    
    elif number > guess_number:
        print("Guess a number a little larger than the number you have guessed now")
        trials += 1
    
    else:
        print("You have guessed a wrong number, Better luck next time!!")
        trials += 1