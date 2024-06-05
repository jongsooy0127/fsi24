import random
'''
guess a number between 1 and 10: 5
Too low...
guess a number between 1 and 10: 9
Too high...
guess a number between 1 and 10: 7
Too high...
guess a number between 1 and 10: 6
You guessed 6 correctly! It took you 4 guesses
'''
guess = 1
playing = True
answer = random.randint(1,10)

while playing:
    user_input = int(input("Guess a number between 1 and 10: "))
    if user_input < answer:
        guess += 1
        print("Too low...")
    elif user_input > answer:
        guess += 1
        print("Too high...")
    elif user_input == answer:
        print(f"You guessed {answer} correctly! It took you {guess} {"guess" if guess==1 else "guesses"}")
        playing = False