from random import choice
actions = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")

while True:
    player_move = input("Choose: [r]ock, [p]aper or [s]cissors: ").lower()

    if player_move == "r":
        player_choice = actions[0]
    elif player_move == "p":
        player_choice = actions[1]
    elif player_move == "s":
        player_choice = actions[2]
    else:
        print("Invalid choice! Please try again: ")
        continue

    computer_choice = choice(actions)

    print(f"\nYou chose: {player_choice.upper()}, computer chose: {computer_choice.upper()}.\n")

    if player_choice == computer_choice:
        print(f"Both Player and Computer chose {player_choice.capitalize()}.\nIt's a tie!")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    continue_game = input("\nDo you want to try again? ['y' or 'n']: ").lower()
    if continue_game != "y":
        break
