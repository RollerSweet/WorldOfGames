from GuessGame import play as GuessGamePlay
from MemoryGame import play as MemoryGamePlay
from CurrencyRouletteGame import play as CurrencyRouletteGamePlay

def welcome():
    while True:
        name = input('Please enter your name: ')
        if name.isalpha() and name.strip():
            break
        else:
            print("Invalid input, Please use only letters!.")
    return print(f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play.")


def load_game():
    # Print the game options
    print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")

    # Get the game number from the user
    while True:
        game = input("Enter the game number (1-3): ")
        if game.isnumeric() and 1 <= int(game) <= 3:
            break
        else:
            print("Invalid game number. Please enter a valid number (1-3).")
    while True:
        difficulty = input("Please choose game difficulty from 1 to 5: ")
        if difficulty.isnumeric() and 1 <= int(difficulty) <= 5:
            break
        else:
            print("Invalid difficulty level. Please enter a valid number (1-5).")
    # Start the game
    print(f"Starting game {game} with difficulty {difficulty}\n")

    if game == '1':
        print(GuessGamePlay(int(difficulty)))
    elif game == '2':
        print(MemoryGamePlay(int(difficulty)))
    elif game == '3':
        CurrencyRouletteGamePlay(int(difficulty))

    answer = input('\nDo you want to play another Game?\nType Yes or No: ')
    if answer.lower() == 'yes':
        load_game()
    elif answer.lower() == 'no':
        print("Ok got you!")
    else:
        print("I guess you don't want to play anymore..")
