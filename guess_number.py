from itertools import count
import random


def play_guess_number(name="player-one", count=5):
  
    player_wins = 0
    computer_wins = 0
    game_count = 0
    # This runs only once when game_count is 0
    print(count)
    def guess_number(): 
        nonlocal name, count
        nonlocal player_wins, computer_wins, game_count
        player_choice = input(f"{name}, pls enter a number between 1 and 3: ")
        computer_choice = random.choice(["1", "2", "3"])
        player = int(player_choice)
        computer = int(computer_choice)

     

        if player < 1 or player > 3:
            print("\nYou must enter a number between 1 and 3")
            guess_number()
        else:
            print(f"{name} chose: {player}")
            print(f"Computer chose: {computer}")
            game_count += 1
            game_count_percent = (game_count / count) * 100 
            print(f"Game count percentage: {game_count_percent}%")
        def decide_winner():
            nonlocal player_wins, computer_wins
            if player == computer:
                print(f"{name} wins!")
                player_wins += 1
            else:
                print(f"{name} loses!")
                computer_wins += 1

        decide_winner()
        # game_result = decide_winner()
        # print(game_result)
    guess_number()
  
    print(f"\nScore: You {player_wins} - Computer {computer_wins}")
    print(f"Game count: {game_count}")  

    play_again_choice = True
    while play_again_choice:
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again == 'y':
            guess_number()
            continue
        elif play_again == 'n':
            print("Thanks for playing!")
            play_again_choice = False
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

  



import argparse

parser = argparse.ArgumentParser(
            description="Provides a personized game experience."
    )

parser.add_argument(
            "-n", "--name",metavar="name",
            required=True,
            help="the name of the player"
    )
parser.add_argument(
            "-c", "--count",metavar="count",
            required=False,default=5,type=int,
            help="the number of rounds to play"
    )
    
args = parser.parse_args()
play_guess_number(args.name, args.count)