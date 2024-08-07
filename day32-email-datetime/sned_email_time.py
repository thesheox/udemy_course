import datetime as dt
import random
import smtplib

with open("quotes.txt") as reader:
    text=reader.readlines()
    qoute=random.choice(text)

now_time=dt.datetime.now()
minute=now_time.minute

my_email = "thesheox@gmail.com"
password="elkw zstl hlqm uzxx"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    if minute == 3:
        connection.sendmail(from_addr=my_email,to_addrs="shayan.saeidian@gmail.com",msg=f"subject:happy bithday\n\n{qoute}")





