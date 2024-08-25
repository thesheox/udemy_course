##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import random
import smtplib

import datetime as dt
import random
import smtplib

import pandas




with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as reader:
    text=reader.read()



now_time=dt.datetime.now()
day=now_time.day
month=now_time.month

data = pandas.read_csv("birthdays.csv")
bithday_data = data.to_dict(orient="records")






my_email = "thesheox@gmail.com"
password="elkw zstl hlqm uzxx"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    for dict in bithday_data:
        if dict["day"] == day and dict["month"] == month:
            my_text = text.replace("[NAME]", dict["name"])
            connection.sendmail(from_addr=my_email, to_addrs="shayan.saeidian@gmail.com",
                                msg=f"subject:happy bithday\n\n {my_text}")










