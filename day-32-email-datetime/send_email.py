import smtplib
import email
import email.utils
my_email = "thesheox@gmail.com"
password="elkw zstl hlqm uzxx"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="shayan.saeidian@gmail.com",msg="subject:happy bithday\n\n"
                                                                                    "hi shayan happy birthday")
