import random
player_wins = 0
computer_wins = 0
game_count = 0
def guess_number(): 

    

    player_choice = input("Enter a number between 1 and 3: ")
    computer_choice = random.choice(["1", "2", "3"])
    player = int(player_choice)
    computer = int(computer_choice)

    if player < 1 or player > 3:
        print("\nYou must enter a number between 1 and 3")
        guess_number()
    else:
        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")
        game_count += 1
        print(game_count)


        def decide_winner():

            if player == computer:
                print("you win!")
                player_wins += 1
            else:
                print("You lose!")
                computer_wins += 1

        game_result = decide_winner()
        print(game_result)

    while True:
        print(f"\nScore: You {player_wins} - Computer {computer_wins}")
        print(f"Game count: {game_count}")
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again == 'y':
            guess_number()
        elif play_again == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
guess_number()