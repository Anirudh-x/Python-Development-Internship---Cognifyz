# Guessing Game

import random

num = random.randint(1, 100) # Generate random number between 1 to 100

while True:
    guess = int(input("\nEnter Your Guess : ")) # User input
    
    # Condition to check if the guess is same as generated number
    if num == guess : 
        print(f"\nYou got the Correct Guess. The Number is {num}")
        break

    elif num < guess:
        print("\nWrong Guess !\nHint : Too High")

    elif num > guess:
        print("\nWrong Guess !\nHint : Too Low")

    else:
        print("! Invalid Guess !")