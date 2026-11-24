# We are goig to write a program that generates a random number and asks the user
# to guess it.

# if the players guess is higher than the actual number, the program displays"Lower number please".
# similarly, if the user's guess it too low, the program prints "higher number please" when the user guesses the 
# correct number, the program displays the number of guesses the player used to arrive at the number

import random as r

number = int(r.randint(1,100))
guess = False
guess_count = 0

while not guess:
    guess_no = int(input("Enter Number : "))
    
    if type(guess_no) == int:
        if guess_no > number:
            print("Lower Number Please...")
            guess_count+=1
        elif guess_no < number:
            print("Higher Number Please...")
            guess_count+=1
        elif guess_no == number:
            print(f"Number of Guesses to reach to the number {number} : {guess_count}")
            guess = True
    else:
        print("Wrong Input")