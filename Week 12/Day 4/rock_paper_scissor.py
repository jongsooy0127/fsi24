'''
rock, paper, or scissors?: paper
Your opponent chose: scissors
You lose...

rock, paper, or scissors?: rock
Your opponent chose: paper
You lose...

rock, paper, or scissors?: scissors
Your opponent chose: rock
You lose...

rock, paper, or scissors?: rock
Your opponent chose: rock
rock, paper, or scissors?: rock
Your opponent chose: scissors
You win!
'''
import random

opponent_choice = ["rock", "paper", "scissor"][random.randrange(3)]
user_choice = input("Rock, paper, or scissor?: ").lower()

if opponent_choice == "rock" and user_choice == "scissor":
    print("You lose...")
    print(f"Opponent's choice was {opponent_choice}")
elif opponent_choice == "paper" and user_choice == "rock":
    print("You lose...")
    print(f"Opponent's choice was {opponent_choice}")
elif opponent_choice == "scissor" and user_choice == "paper":
    print("You lose...")
    print(f"Opponent's choice was {opponent_choice}")
elif opponent_choice == user_choice:
    print("It's a tie!")
    print(f"Opponent's choice was {opponent_choice}")
elif opponent_choice == "rock" and user_choice == "paper":
    print("You win!")
    print(f"Opponent's choice was {opponent_choice}")
elif opponent_choice == "paper" and user_choice == "scissor":
    print("You win!")
    print(f"Opponent's choice was {opponent_choice}")
elif opponent_choice == "scissor" and user_choice == "rock":
    print("You win!")
    print(f"Opponent's choice was {opponent_choice}")
else: print("Invalid option!")