import os
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = int

def Screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
