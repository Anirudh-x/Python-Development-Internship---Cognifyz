# Number Guesser

import random

num = random.randint(1, 1000) # Generate random number between 1 to 1000

while True:
    guess = int(input("\nEnter Your Guess : "))
    
    if num == guess :
        print(f"\nYou got the Correct Guess. The Number is {num}")
        break

    elif num < guess:
        print("\nWrong Guess !\nHint : Too High")

    elif num > guess:
        print("\nWrong Guess !\nHint : Too Low")

    else:
        print("! Invalid Guess !")