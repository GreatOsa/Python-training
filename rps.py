# A simple Rock-Paper-Scissors game in Python 

import sys
import random
from enum import Enum


def play_rps():
        class RPS(Enum):
                ROCK = 1
                PAPER = 2
                SCISSORS = 3

        # playagain=True

      
        playerChoices = input("\nEnter.. \n1 for Rock \n2 for Paper \n3 for Scissors \n\n")
        if playerChoices not in ["1", "2", "3"]:
                print("you must enter 1, 2 or 3")
                play_rps()

        player = int(playerChoices)
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        if player < 1 or player > 3:
                sys.exit()

        print("\nyou chose: ", RPS(player).name)
        print("computer chose: ", RPS(computer).name + "\n")
                
        if player == computer:
                print("It's a tie!")
        elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
                print("You win!")
        else:
                print("You lose!")
        print("\nplay again?")
        while True: 
          playagain = input("\nY for yes, N for no: ").strip().lower()
          if playagain.lower() not in ['y', 'n']:
                continue
          else:
                break
        if playagain.lower() == 'y':
                return play_rps()
        else:
          print("Thanks for playing!")
          sys.exit("Game Over")

# print("Game Over")
play_rps()


