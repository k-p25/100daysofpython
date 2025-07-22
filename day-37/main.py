import requests, os
from datetime import *

USER = os.environ.get('user')
TOKEN = os.environ.get('token')
GRAPH_ID = os.environ.get('graph_id')

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USER,
    'agreeTermsOfService': 'yes', 
    'notMinor': 'yes',
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USER}/graphs'

graph_params = {
    'id': GRAPH_ID,
    'name': "Exercise Tracker",
    'unit': 'Mins', 
    'type': 'int',
    'color': 'kuro'
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

pixel_endpoint = f'{graph_endpoint}/{GRAPH_ID}'
today = datetime.now()
yesterday = today - timedelta(days=1)

pixel_params = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '50'
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_endpoint = f'{pixel_endpoint}/{yesterday.strftime("%Y%m%d")}'
update_params = {
    'quantity': '30'
}

response = requests.put(url=update_endpoint, json=update_params, headers=headers)
print(response.text)

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
