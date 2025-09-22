# A simple Rock-Paper-Scissors game in Python 

import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(RPS(2))
playerChoices = input("Enter.. \n1 for Rock \n2 for Paper \n3 for Scissors \n\n")
player = int(playerChoices)
computerchoice = random.choice("123")
computer = int(computerchoice)

if player < 1 or player > 3:
        sys.exit("you must enter 1, 2 or 3")

print("you chose: ", RPS(player).name)
print("computer chose: ", RPS(computer).name)
    
if player == computer:
        print("It's a tie!")
elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("You win!")
else:
        print("You lose!")


