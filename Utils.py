import os

SCORES_FILE_NAME = "Scores.txt"

BAD_RETURN_CODE = "ERROR - THE FILE IS NOT EXISTS"

def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')