import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "___your email___"
MY_PASSWORD = "___your pasword___"

# Modify to your location lng and lat
# Your latitude
MY_LAT = 6.524379
# Your longitude
MY_LONG = 3.379206


def is_iss_overhead():
    '''Returns True if ISS location relatively corresponds'''
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # when position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    '''Returns True if it's night time'''
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# Loops keeps keeps Code running on the background 
while True:
    # Time machanisn for loop runtime specification
    time.sleep(60)
    # Condition run if both functions are True
    if is_iss_overhead() and is_night():
        connector = smtplib.SMTP("smtp.gmail.com")
        connector.starttls()
        connector.login(user=MY_EMAIL, password=MY_PASSWORD)
        connector.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="___recipient's email (you can send mail to yourself too)___",
            msg="Subject:Look-Up\n\nThe ISS is above you in the sky."
        )
