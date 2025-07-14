import requests # type: ignore
from datetime import datetime 
import smtplib



MY_EMAIL = "anemail@gmail.com"
MY_PWD = "apassword"
MY_LAT = 41.902782
MY_LNG = 12.496365

def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if MY_LAT -5 <= iss_latitude <= MY_LAT + 5 and MY_LNG -5 <= iss_longitude <= MY_LNG:
        return True

def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", parameters)
    response.raise_for_status()
    data = response.json()
    
    sunrise = int(data['results']['sunrise'].split("T")[1].split(':')[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(':')[0])

    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    
if is_iss_overhead() and is_night():
    
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PWD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look Up \n\nThe ISS is above you in the sky."
    )

