""" Rock Paper Scissors
----------------------------------------
"""

import random
import os
import re

os.system('cls' if os.name=='nt' else 'clear')

while (1 < 2):
    print("\n")
    print("Rock, Paper, Scissors - Shoot!")
    user_choice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]",user_choice):
        print("Please choose a letter:")
        print("[R]ock, [S]cissors or [P]aper")
        continue
    #Echo the user's choice
    print("You chose: " + user_choice)
    choices = ["R","P","S"]
    opponent_choice = random.choice(choices)
    print("Computer chose: " + opponent_choice)
    if opponent_choice == str.upper(user_choice):
        print("Tie!")
    elif opponent_choice == "R" and user_choice.upper() == "S":
        print("Rock beats scissors! you lose!")
        continue
    elif opponent_choice == "S" and user_choice.upper() == "P":
        print("Scissors beats paper! you lose!")
        continue
    elif opponent_choice == "P" and user_choice.upper() == "R":
        print("Paper beats rock! you lose!")
        continue
    else:
        print("You win!")