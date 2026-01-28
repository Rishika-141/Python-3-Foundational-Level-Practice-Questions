# Accept two number and print the greatest b/w them
num1 = int(input())
num2 = int(input())
if(num1 > num2):
    print(f'{num1} is greater than {num2}')
elif(num2 > num1):
    print(f'{num2} is greater than {num1}')
else:
    print("Both are equal")


# Accept the gender from the user as char, and print the 
# respective greeting message, Ex - Good Morning sir (on the basis of gender)
gender = input()
if gender == 'M' or gender == 'm':
    print("Good Morning Sir")
elif gender == 'F' or gender == 'f':
    print("Good Morning Mam")
else:
    print("Unidentified gender")

# Accept an integer and check whether the integer is even or odd
number = int(input())
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Accept the name and age from the user, check if the user is the valid voter or not
# Ex - hello sherry you are a valid voter
name = input()
age = int(input())
if age >= 18:
    print(f'Hello {name}, You are a Valid Voter.')
else:
    print(f'Sorry {name}, You are not a Valid Voter.')

# Accept a year, and check whether it is a leap year or not
# century year hai then check if it is divisible by both 100 and 400
# not a century year then check if it is divisible by 4
year = int(input())
if year % 100 == 0 and year % 400 == 0:
    print(f'{year} is a Leap year')
elif year % 100 != 0 and year % 4 == 0:
    print(f'{year} is a Leap year')
else:
    print(f'{year} is a normal year')

# Take the input of temperature in celsius and print the desired output as following:
temperature = int(input("Please give the Temperature value: "))
if temperature < 0:
    print("Freezing Cold")
elif temperature >= 0 and temperature < 10:
    print("Very Cold")
elif temperature >= 10 and temperature < 20:
    print("Cold")
elif temperature >= 20 and temperature < 30:
    print("Pleasant")
elif temperature >= 30 and temperature < 40:
    print("Hot")
else:
    print("Very Hot")