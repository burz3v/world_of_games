import CurrencyRouletteGame
import MemoryGame
import GuessGame
import time
from Score import add_score
from Utils import screen_cleaner


def welcome(name):
    welcome_message = f"""
Hello {name} and welcome to the World of Games (WoG).
Here you can find many cool games to play.
"""
    return welcome_message


def load_game():
    print("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
""")
    while True:
        chosen_game = input(f"Please enter the number between 1 to 3: ")
        if chosen_game != "1" and chosen_game != "2" and chosen_game != "3":
            print(f"Only numbers from 1 to 3 are accepted!")
        else:
            chosen_game = int(chosen_game)
            break
    while True:
        difficulty = input(f"Please choose game difficulty from 1 to 5: ")
        if difficulty != "1" and difficulty != "2" and difficulty != "3" and difficulty != "4" and difficulty != "5":
            print(f"Only numbers from 1 to 5 are accepted!")
        else:
            difficulty = int(difficulty)
            break
    print(f"\nTHE GAME STARTS")
    if chosen_game == 2:
        print(f"\nGUESS GAME")
        if_win = GuessGame.play(difficulty)
        if if_win:
            print("You won!")
            add_score(difficulty)
            play_again()
        else:
            print("You lose!")
    elif chosen_game == 1:
        print(f"\nMEMORY GAME\nGET READY TO REMEMBER NUMBERS!")
        time.sleep(3)
        if_win = MemoryGame.play(difficulty)
        if if_win:
            print("You won!")
            add_score(difficulty)
            play_again()
        else:
            print("You lose!")
    elif chosen_game == 3:
        print(f"\nCURRENCY ROULETTE GAME")
        if_win = CurrencyRouletteGame.play(difficulty)
        if if_win:
            print("You won!")
            add_score(difficulty)
            play_again()
        else:
            print("You lose!")


def play_again():
    while True:
        restart = input(f"Do you want to play again? (Y/N)? ")
        if restart != "Y" and restart != "y" and restart != "N" and restart != "n":
            print("Please type Y or N")
        elif restart == "Y" or restart == "y":
            screen_cleaner()
            load_game()
        else:
            break
