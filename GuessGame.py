import random

def generate_number(difficulty):
    return random.randint(1, difficulty)

def get_guess_from_user(difficulty):
    while True:
        guess = input(f'Guess a number between 1 and {difficulty}: ')
        if guess.isnumeric() and 1 <= int(guess) <= int(difficulty):
            break
        else:
            print(f"Invalid game number. Enter number between 1 and {difficulty}: ")
    return guess

def compare_results(user_guess, secret_number):
    if user_guess == secret_number:
        return "You Won!"
    else:
        return "You Lost!"

def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(user_guess, secret_number)