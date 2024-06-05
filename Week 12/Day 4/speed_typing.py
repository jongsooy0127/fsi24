'''
Please type out the word "pneumonoultramicroscopicsilicovolcanoconiosis": wait what???
Please type out the word "pneumonoultramicroscopicsilicovolcanoconiosis": pneumonoultramicroscopisilicovolcanoconiosis
Please type out the word "pneumonoultramicroscopicsilicovolcanoconiosis": pneumonoultramicroscopicsilicovolcanoconiosis
Please type out the word "hippopotomonstrosesquippedaliophobia": hippo....huh?
Please type out the word "hippopotomonstrosesquippedaliophobia": hippopotomonstrosesquippedaliophobia
Congratulations, you are finished!
'''

import time
import random

long_str = ["pneumonoultramicroscopicsilicovolcanoconiosis","hippopotomonstrosesquippedaliophobia","floccinaucinihilipilification", "antidisestablishmentarianism", "pseudopseudohypoparathyroidism", "aequeosalinocalcalinoceraceoaluminosocupreovitriolic"]
answer = long_str[random.randrange(len(long_str))]
playing = True
start = time.time()

print("Welcome to the speed typing challenge! Try to type the provided word as quickly as possible")

while playing:
    user_input = input(f"Please type out the word {answer}: ")
    if answer == user_input:
        end = time.time()
        print(f"Congratulations, you are finished! It took you {round((end-start),2)} seconds")
        playing = False
    elif user_input == "quit":
        print("User has quit the game")
        playing = False
    else: 
        print("Try again!")


