from art import logo
import random

def play_game():
    print(logo)
    number = random.randint(1, 100)
    level_correct = False
    while not level_correct:
        level = input("Welcome to number guessing game. Choose 'easy' or 'hard'. ").lower()
        if level == "easy":
            steps = 10
            level_correct = True
        elif level == "hard":
            steps = 5
            level_correct = True
        else:
            print("Invalid input. Choose again.")

    print("The number is between 1 and 100.")
    continue_guess = True
    while continue_guess:
        if steps > 0:
            guess = int(input(f"Guess a number. You have {steps} step(s) left."))
            steps -= 1
            if guess == number:
                continue_guess = False
            elif guess > number:
                print("It is too big.")
            elif guess < number:
                print("It is too small.")
        elif steps == 0:
            continue_guess = False

    if guess == number:
        print(f"You win. You have {steps} step(s) left.")
    else:
        print(f"You have {steps} step(s) left. You lose.")

play_again = True
while play_again:
    choose_again_invalid = True
    while choose_again_invalid == True:
        choose_play_again = input("Would you like to guess a number? Type 'y' to continue, 'n' to exit. ").lower()
        if choose_play_again == "y":
            choose_again_invalid = False
            play_game()
        elif choose_play_again == "n":
            choose_again_invalid = False
            play_again = False
        else:
            print("Invalid input. Type again.")