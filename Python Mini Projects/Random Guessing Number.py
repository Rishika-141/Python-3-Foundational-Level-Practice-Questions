#Random Guessing Number Game - using while loop
# We will create a game for guessing a number randomly that would lie between 1 to 100
# Here we will use random library

import random
random_number = random.randint(1, 100)

no_of_tries = 0

while True: # This would create an infinite loop 

    guessed_number = int(input("Enter the number that you have guessed: "))

    #If you have guessed the right number
    if(random_number == guessed_number):
        no_of_tries += 1
        print(f'Congratulations! You have guessed a right number, {guessed_number} is the correct number in {no_of_tries} trials.')
        break

    #The number you have guessed is smaller than the desired number
    elif(random_number > guessed_number):
        print("Oops!, You are very close to the correct number, Just guess a number greater than the number you have guessed before!")
        no_of_tries += 1

    #The number you have guessed is larger than the desired number
    elif(random_number < guessed_number):
        print("Oops!, You are very close to the correct number, Just guess a number smaller than the number you have guessed before!")
        no_of_tries += 1
    
    #The number you guessed is incorrect
    else:
        print("Sorry, Better luck next time!")
        print("The number you guessed is incorrect.")
        no_of_tries += 1
    


        
