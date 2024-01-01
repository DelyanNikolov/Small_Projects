
import datetime as dt
import pandas
import smtplib
import random
MY_EMAIL = ""
MY_PASSWORD = ""


def current_day_and_month():
    current_date = dt.datetime.now()
    day = current_date.day
    month = current_date.month
    return day, month


data = pandas.read_csv("birthdays.csv")
birthday_details = data.to_dict(orient="records")
current_day, current_month = current_day_and_month()
for record in birthday_details:
    if current_day == int(record["day"]) and current_month == int(record["month"]):
        name = record["name"]
        email = record["email"]

letter = random.randint(1, 3)
with open(f"letter_templates/letter_{letter}.txt", "r") as email_content:
    email_text = email_content.read()
    email_text = email_text.replace("[NAME]", name)
    print(email_text)

for record in birthday_details:
    if current_day == record["day"] and current_month == record["month"]:
        name = record["name"]
        email = record["email"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy birthday!\n\n{email_text}"
            )
