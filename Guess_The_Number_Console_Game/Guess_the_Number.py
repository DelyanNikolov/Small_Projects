from random import randint


print("Welcome to Guess the number game!\n")

number_to_guess = randint(1, 100)
game_message = ""
player_number = 0
game_is_on = True

while game_is_on:
    player_input = input("Guess a number between 1 and 100: ")
    if not player_input.isdigit() or int(player_input) > 100 or int(player_input) < 1:
        print("Invalid number! Try again...")
        continue
    player_number = int(player_input)

    if player_number == number_to_guess:
        game_message = "Correct! You guessed the number!"
        game_is_on = False
    elif player_number > number_to_guess:
        game_message = "Too high. Guess again: "
    elif player_number < number_to_guess:
        game_message = "Too low. Guess again: "

    print(game_message)

    if not game_is_on:
        another_game = input("\nDo yo want to try again? [y] or [n]: ").lower()
        if another_game == "y":
            game_is_on = True
            number_to_guess = randint(1, 100)

