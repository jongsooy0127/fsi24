"""
Create a dice roll simulator using the random module. If the user inputs roll, 
roll the dice and let the user know what the result is. If the user inputs quit 
or anything other than roll, exit out of loop.
"""
import random
playing = True

while playing:
    user_input = input('Would you like to "roll" or "quit"?')
    if user_input == "roll":
        rand_roll = random.randrange(1,7)
        print(f"You rolled a {rand_roll}")
    elif user_input == "quit":
        print("User has quit")
        playing = False