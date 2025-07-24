import os, dotenv, requests
from datetime import datetime

dotenv.load_dotenv()

APP_ID = os.getenv("app_id")
API_KEY = os.getenv("api_key")
SHEETY_ENDPOINT = os.getenv('sheety_endpoint')
SHEETY_TOKEN = os.getenv('sheety_token')

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("What exercises did you do today? ")

params = {
    'query': query
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
response.raise_for_status()
exercise_data = response.json()

current_date = datetime.now().strftime("%d/%m/%y")
current_time = datetime.now().strftime("%H:%M:%S")

bearer_headers = {
    "Authorization": f'Bearer {SHEETY_TOKEN}'
}

for exercise in exercise_data['exercises']:
    
    input = {
        'workout': {
            'date': current_date,
            'time': current_time, 
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'], 
            'calories': exercise['nf_calories']
        }
    }

    response = requests.post(SHEETY_ENDPOINT, json=input, headers=bearer_headers)
    print(response.text)
    print(response.status_code)