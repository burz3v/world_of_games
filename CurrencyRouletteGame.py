import random, yahoo_fin.stock_info as si
from datetime import datetime, timedelta

def get_money_interval(src, dst, difficulty):
    # construct the currency pair symbol
    symbol = f"{src}{dst}=X"
    # extract minute data of the recent 2 days
    latest_data = si.get_data(symbol, interval="1m", start_date=datetime.now() - timedelta(days=2))
    # get the latest datetime
    last_updated_datetime = latest_data.index[-1].to_pydatetime()
    # get the latest price
    latest_price = latest_data.iloc[-1].close
    amount = random.randint(1, 100)
    converted = (int(latest_price) * amount)
    print(f"-----------------------> {converted}")
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
    converted, amount, high_interval, low_interval = get_money_interval("USD", "ILS", difficulty)
    users_guess = get_guess_from_user(amount)
    if high_interval >= users_guess >= low_interval:
        print("win")
        return True
    else:
        print("lose")
        return False