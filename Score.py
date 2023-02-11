import Utils
import os

POINTS_OF_WINNING = lambda difficulty: (int(difficulty) * 3) + int(5)


def add_score(difficulty):
    if not os.path.exists(Utils.SCORES_FILE_NAME):
        current_score = 0
    else:
        with open(Utils.SCORES_FILE_NAME, 'r') as score_file:
            current_score = int(score_file.read().strip())

    new_score = current_score + POINTS_OF_WINNING(difficulty)

    with open(Utils.SCORES_FILE_NAME, 'w') as score_file:
        score_file.write(str(new_score))
