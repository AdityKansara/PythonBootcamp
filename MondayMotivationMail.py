import smtplib
import random
import datetime as dt

myemail = "adity.kansara36@gmail.com"
password = ""
msg = """Subject:Monday Motivation\n\n"""

today = dt.datetime.now()
if today.weekday() == 0:
    with open("Resources/motivationalQuotes.txt", "r") as f:
        quotes = f.readlines()
        msg += random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        con.login(user=myemail, password=password)
        con.sendmail(from_addr=myemail, to_addrs="xyz@gmail.com", msg=msg)
