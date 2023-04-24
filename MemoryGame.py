import random
import time
import os


def generate_sequence(difficulty):
    random_numbers = []
    for i in range(0, difficulty):
        number = random.randint(1, 101)
        random_numbers.append(number)
    print(random_numbers)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    return random_numbers


def get_list_from_user(difficulty):
    user_numbers = []
    print(f"Please enter {difficulty} numbers.")
    for i in range(0, difficulty):
        while True:
            number = input("Please enter the number: ")
            if number.isdigit():
                number = int(number)
                break
            else:
                print("Please enter the number ONLY.")
        user_numbers.append(number)
    return user_numbers


def is_list_equal(random_numbers, user_numbers):
    random_numbers.sort()
    user_numbers.sort()
    if random_numbers == user_numbers:
        return True
    else:
        return False


def play(difficulty):
    random_numbers = generate_sequence(difficulty)
    user_numbers = get_list_from_user(difficulty)
    if is_list_equal(random_numbers, user_numbers):
        print("win")
        return True
    else:
        print("lose")
        return False
