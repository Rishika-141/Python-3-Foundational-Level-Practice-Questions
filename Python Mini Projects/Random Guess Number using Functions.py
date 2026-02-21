# Random Guessing Number using Functions

import random
random_num = random.randint(1, 100) # Here it will consider till number 100 

def guess_number_game():
    tries = 0

    while True:
        guess_number = int(input("Enter the number you guessed: "))
        
        if guess_number == random_num:
            tries += 1
            print(f'{guess_number} is the correct guess, You have found this in {tries} tries.')
            break

        elif random_num < guess_number:
            tries += 1
            print("Oops!, Try to guess a number a little smaller than this")
        
        else:
            tries += 1
            print("Oops!, Try to guess a number a little greater than this")
        
guess_number_game()








