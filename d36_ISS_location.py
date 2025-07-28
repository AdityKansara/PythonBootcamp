import smtplib
import requests
import datetime as dt

MYLAT = 12.9716
MYLNG = 77.5946
myemail = "adity.kansara36@gmail.com"
password = ""
msg = """Subject:Look Up!\n\n ISS is going! <3\n\n"""

params = {"lat": MYLAT, "lng": MYLNG, "formatted": 0}


def notify():
    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        con.login(user=myemail, password=password)
        con.sendmail(from_addr=myemail, to_addrs=myemail, msg=msg)


def is_iss_overhead():
    spaceres = requests.get(url="http://api.open-notify.org/iss-now.json", verify=False)
    spaceres.raise_for_status()
    spacedata = spaceres.json()["iss_position"]
    iss_lat = float(spacedata["latitude"])
    iss_lng = float(spacedata["longitude"])

    if MYLAT - 5 <= iss_lat <= MYLAT + 5 and MYLNG - 5 <= iss_lng <= MYLNG + 5:
        return True


def is_night():
    res = requests.get(
        url="https://api.sunrise-sunset.org/json", params=params, verify=False
    )
    res.raise_for_status()
    data = res.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    currentHour = dt.datetime.now().hour

    if currentHour >= sunset or currentHour <= sunrise:
        return True
    else:
        return False


if is_night() and is_iss_overhead():
    notify()
else:
    print("Not yet the time!")
