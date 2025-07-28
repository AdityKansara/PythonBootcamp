import smtplib
import datetime as dt
import pandas as p

myemail = "adity.kansara36@gmail.com"
password = ""
msg = """Subject:Happy Birthday! <3\n\n"""

birthdayData = p.read_csv("Resources/birthday.csv")
birthdayData = birthdayData.to_dict("records")

currentmonth = dt.datetime.now().month
today = dt.datetime.now().day

for x in birthdayData:
    if currentmonth == x["month"] and today == x["date"]:
        with open("Resources/letter.txt", "r") as f:
            lines = f.read()

        lines = lines.replace("[name]", x["name"])
        msg += lines

        with smtplib.SMTP("smtp.gmail.com") as con:
            con.starttls()
            con.login(user=myemail, password=password)
            con.sendmail(from_addr=myemail, to_addrs=x["email"], msg=msg)
