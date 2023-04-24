import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    print(f"------------------> {secret_number}")
    return secret_number


def get_guess_from_user(difficulty):
    while True:
        number = input(f"Guess the number from 1 to {difficulty}: ")
        if number.isdigit():
            number = int(number)
            break
        else:
            print("Please enter the number ONLY.")
    return number


def compare_results(secret_number, number):
    if secret_number == number:
        return True


def play(difficulty):
    secret_number = generate_number(difficulty)
    number = get_guess_from_user(difficulty)
    if compare_results(secret_number, number):
        print("win")
        return True
    else:
        print("lose")
        return False
