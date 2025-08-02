from dotenv import load_dotenv #type:ignore
import requests, os # type: ignore
from twilio.rest import Client  # type: ignore

load_dotenv()
API_KEY = os.environ.get("API_KEY")
TO_NUM = os.environ.get("TO_NUM")
FROM_NUM = os.environ.get("FROM_NUM")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")



params = {
    "lat": 20.159364,
    'lon': 105.922412,
    'appid': API_KEY,
    'cnt': 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
for forecast in weather_data['list']:
   condition_code = forecast['weather'][0]['id']
   if (condition_code < 700):
       client = Client(account_sid, auth_token)
       message = client.messages.create(
               body="Bring an umbrella. It's going to rain!",
               to=TO_NUM,
               from_=FROM_NUM,
           )
       print(message.status)
       break