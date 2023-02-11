import requests
import random

def get_money_interval(difficulty):
    # get the current currency rate from USD to ILS
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"]["ILS"]

    # generate a random number between 1-100
    money = random.randint(1, 100)

    # calculate the interval based on the difficulty
    interval = (money * rate - (5 - difficulty), money * rate + (5 - difficulty))

    return interval, money * rate

def get_guess_from_user():
    while True:
        guess = input("Enter your guess for the value of USD in ILS: ")
        if guess.isnumeric():
            guess = float(guess)
            break
        else:
            print("Please enter a valid number.")
    return guess


def play(difficulty):
    interval, correct_value = get_money_interval(difficulty)
    guess = get_guess_from_user()

    if interval[0] <= guess <= interval[1]:
        print("You won!")
        return True
    else:
        print(f"You lost. The correct value was {correct_value}")
        return False
