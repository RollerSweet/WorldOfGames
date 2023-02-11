import random
import time
import re
import os

def generate_sequence(difficulty):
    sequence = random.sample(range(1, 101), difficulty)
    print("Memorize the following numbers:", sequence)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    return sequence

def get_list_from_user(difficulty):
    while True:
        input_string = input(f'Enter {difficulty} numbers separated by spaces: ')
        if len(input_string.split()) != difficulty:
            print("You should enter exactly", difficulty, "numbers.")
            continue
        if not bool(re.match("^[0-9 ]*$", input_string)):
            print("You should enter only numbers.")
            continue
        input_list = [int(x) for x in input_string.split()]
        return input_list

def is_list_equal(list1, list2):
    if len(list1) != len(list2):
        return "You Lost!"
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return "You Lost!"
    return "You Won!"

def play(difficulty):
    sequence = generate_sequence(difficulty)
    user_sequence = get_list_from_user(difficulty)
    return is_list_equal(sequence, user_sequence)
