import requests
import random
from dateutil.parser import parse


def get_all_exchange_rates_erapi(src):
    url = f"https://open.er-api.com/v6/latest/{src}"
    # request the open ExchangeRate API and convert to Python dict using .json()
    data = requests.get(url).json()
    if data["result"] == "success":
        # request successful
        # get the last updated datetime
        last_updated_datetime = parse(data["time_last_update_utc"])
        # get the exchange rates
        exchange_rates = data["rates"]
    return last_updated_datetime, exchange_rates


def convert_currency_erapi(src, dst, amount):
    # get all the exchange rates
    last_updated_datetime, exchange_rates = get_all_exchange_rates_erapi(src)
    # convert by simply getting the target currency exchange rate and multiply by the amount
    return exchange_rates[dst] * amount


def get_money_interval(difficulty):
    amount = random.randint(1, 100)
    converted = int(convert_currency_erapi("USD", "ILS", amount))
    high_interval = int(converted + (5 - difficulty))
    low_interval = int(converted - (5 - difficulty))
    return converted, amount, high_interval, low_interval


def get_guess_from_user(amount):
    while True:
        users_guess = input(f"Guess how much shekels are {amount} dollars: ")
        if users_guess.isdigit():
            users_guess = int(users_guess)
            break
        else:
            print("Please enter the number ONLY.")
    return users_guess


def play(difficulty):
    converted, amount, high_interval, low_interval = get_money_interval(difficulty)
    users_guess = get_guess_from_user(amount)
    if high_interval >= users_guess >= low_interval:
        return True
    else:
        return False
