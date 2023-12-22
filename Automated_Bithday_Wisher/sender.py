import datetime as dt
import random
import smtplib

weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}


def current_day_of_week():
    current_date = dt.datetime.now()
    return weekdays[current_date.weekday()]


def random_quote():
    return random.choice(quotes)


with open("quotes.txt", "r") as data:
    quotes = [line.strip() for line in data]

quote = random_quote()
current_day_of_week = current_day_of_week()

my_email = "dido@gmail.com"
password = "asdfgh"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="delian5@abv.bg",
        msg=f"Subject:Motivational quote\n\n Quote for {current_day_of_week}:\n{quote}"
    )
