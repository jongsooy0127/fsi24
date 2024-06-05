# 1. Create a function that asks the user for radius and height of a
#     cylinder and the function will return the volume of that cylinder.
#     Use the math library for pi!
import math
def volume_cylinder():
    radius = int(input("Enter the radius: "))
    height = int(input("Enter a height: "))
    return math.pi * (radius ** 2) * height

# print("Volume: ", volume_cylinder())

# 2. Create a function that will generate a random number up to 1000 and
#     ask the user to guess the number. Let the user know if the guess is
#     higher or lower than the target number. Keep allowing the user to
#     guess, but stop after a correct guess, or after 10 wrong guesses.
import random

def guess_number():
    guess = 0
    playing = True
    answer = str(random.randint(1,1001))
    while playing:
        user_guess = input("Guess a number between 1 and 1000: ")
        if user_guess == answer:
            print(f"Congratulations! You win! It took you {guess} tries")
            playing = False
        elif guess == 9:
            print("Game over! You used up all of your 10 guesses")
            playing = False
        elif user_guess == "q":
            print(f"User has quit the game. The answer was {answer}")
            playing = False
        elif user_guess > answer:
            print("Your guess is higher than the answer")
            guess += 1
        elif user_guess < answer:
            print("Your guess is lower than the answer")
            guess += 1

# guess_number()

# 3. Create a function that will generate a random date in the year 2024
#     and ask the user to guess the date. (For simplicity, have the user
#     enter in the format 'mm-dd'.) Note that the function should be able
#     to generate 02-29, but not 02-30. However, it should be able to
#     generate 01-31. And so on, for the rest of the valid days of the year.
#     The guessing continues until the user guesses the correct date or
#     types 'q' as an input to quit. 

import datetime

def guess_month_date():
    playing = True
    start_date = datetime.date(2024,1,1)
    end_date = datetime.date(2024,12,31)
    num_days   = (end_date - start_date).days + 1
    print(num_days)
    rand_days   = random.randint(1, num_days+1)
    print(rand_days)
    answer = str(start_date + datetime.timedelta(days=rand_days))
    print(answer)
    while playing:
        user_guess = input("Guess the random date using the format 'mm-dd': ")
        if user_guess == "q":
            print(f"User has quit the game. The answer is {answer}")
            playing = False
        if "2024-"+user_guess == answer:
            print("Congratulations! You win!")
            playing = False
            
# guess_month_date()

# 4. Create a function that asks the user for a date in 'yyyy-mm-dd' format
#     and print out the day of the week for that date. (eg. "Monday",
#     "Tuesday", etc.
def get_day():
    # receive_day = input("Enter a date using the format 'yyyy-mm-dd' to find out the date")
    # receive_day = receive_day.split("-")
    # receive_day = [int(num) for num in receive_day]
    # users_date = datetime.time(receive_day[0],receive_day[1],receive_day[2])
    # print(users_date.strftime('%A'))

    user_input = input("4: Give me a date (yyyy-mm-dd)")
    user_date = datetime.date.fromisoformat(user_input)

    print("4:", user_date.strftime('%A'))

get_day()

#===============================SOLUTION=======================================

#3.
