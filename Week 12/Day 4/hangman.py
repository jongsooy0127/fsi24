'''
Here is the word so far: ****
Guess a letter (5 guesses left): l
Here is the word so far: l***
Guess a letter (4 guesses left): k
Here is the word so far: l**k
Guess a letter (3 guesses left): a
Here is the word so far: l*ak
Guess a letter (2 guesses left): e
You guessed the word!: leak


Here is the word so far: ****
Guess a letter (5 guesses left): f
Here is the word so far: ****
Guess a letter (4 guesses left): a
Here is the word so far: **a*
Guess a letter (3 guesses left): l
Here is the word so far: l*a*
Guess a letter (2 guesses left): x
Here is the word so far: l*a*
Guess a letter (1 guesses left): z
Sorry, you lose, the word was: leak
'''
import random

guess = 6
answer = ["Jaws", "Dune", "Interstellar", "Jumanji", "Frozen", "Martian", "Inception", "Transformer", "Dumbo", "Tarzan", "Up", "Brazil", "IT", "Rocky", "Terminator", "Ants", "Borat", "Taken", "Titanic", "Avatar", "Parasite", "Goodfellas", "Maleficent", "Brave", "Cinderella", "Ratatouille", "Invincible", "Saw", "Alladin", "Shrek", "Ponyo", "Twilight"]
answer = answer[random.randrange(len(answer))].lower()
user_answer = "*" * len(answer)
playing = True
answer = list(answer)
user_answer = list(user_answer)

while playing:
    print(f"Here is the word so far: {"".join(user_answer)}")
    user_guess = input(f"Guess a letter: (You have {guess} attempts left) - ").lower()
    if user_guess in answer:
        for i in range(len(answer)):
            if user_guess == answer[i]:
                user_answer[i] = answer[i]
    elif guess == 1:
        print(f"Sorry you lose. The answer was {"".join(answer).title()}")
        playing = False
    else: guess -= 1
    if user_answer == answer:
        print(f"You guessed the word: {"".join(answer).title()}")
        playing = False

#user_answer = user_answer[:answer.index(user_guess)] + user_guess + user_answer[answer.index(user_guess)+1:]