from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    try:
        with open(SCORES_FILE_NAME, "r") as file:
            old_score = int(file.read())

        new_score = old_score + points_of_winning

        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(new_score))

    except FileNotFoundError:
        with open(SCORES_FILE_NAME, "w+") as file:
            file.write(str(points_of_winning))
