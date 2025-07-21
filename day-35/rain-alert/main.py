import requests, os # type: ignore

API_KEY = os.environ.get("API_KEY")



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
       print("Bring an umbrella")
       break
         
