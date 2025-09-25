# A simple Rock-Paper-Scissors game in Python 

import sys
import random
from enum import Enum


def rps(name="player-one"):
        # first function

        game_count = 0 # the count
        player_wins = 0
        computer_wins = 0 

        
        def play_rps():
                nonlocal name
                nonlocal player_wins
                nonlocal computer_wins
                class RPS(Enum):
                        ROCK = 1 
                        PAPER = 2
                        SCISSORS = 3

                # playagain=True 
        
                playerChoices = input(f"\n{name} pls enter.. \n1 for Rock \n2 for Paper \n3 for Scissors \n\n")
                if playerChoices not in ["1", "2", "3"]:
                        print("you must enter 1, 2 or 3")
                        play_rps()

                player = int(playerChoices)
                computerchoice = random.choice("123")
                computer = int(computerchoice)

                if player < 1 or player > 3:
                        sys.exit()

                print(f"\n{name} chose: ", RPS(player).name)
                print(f"computer chose: ", RPS(computer).name + "\n")

                def decide_winner(player, computer):
                        nonlocal player_wins
                        nonlocal computer_wins
                        if player == computer:
                                return "It's a tie!"
                        elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
                                player_wins += 1
                                return f"{name} wins!"
                        else:  
                                computer_wins += 1
                                return f"{name} loses!"
                
                game_result = decide_winner(player,computer)

                print(game_result)
                print(f"\nScore: {name} {player_wins} - Computer {computer_wins}") 
                nonlocal game_count
                game_count += 1

                print(f"\nGame count: {game_count}")

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

        return play_rps()

        # print("Game Over")
        # play_rps()

if __name__ == "__main__":
        import argparse

        parser = argparse.ArgumentParser(
                description="Provides a personized game experience."
        )

        parser.add_argument(
                "-n", "--name",metavar="name",
                required=True,
                help="the name of the player"
        )
       
        args = parser.parse_args()

        rock_paper_scissors = rps(args.name)
        rock_paper_scissors()