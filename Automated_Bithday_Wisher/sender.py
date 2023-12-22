import datetime as dt
import random

weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}


def get_current_day_of_week():
    global current_day_of_week
    current_date = dt.datetime.now()
    return weekdays[current_date.weekday()]


current_day_of_week = get_current_day_of_week()
with open("quotes.txt", "r") as data:
    quotes = [line.strip() for line in data]

random_quote = random.choice(quotes)
print(random_quote)
print(current_day_of_week)