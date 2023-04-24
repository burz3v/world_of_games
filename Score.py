from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    try:
        with open(SCORES_FILE_NAME, "r") as file:
            old_score = int(file.read())

        new_score = old_score + POINTS_OF_WINNING

        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(new_score))

    except FileNotFoundError:
        with open(SCORES_FILE_NAME, "w+") as file:
            file.write(str(POINTS_OF_WINNING))
