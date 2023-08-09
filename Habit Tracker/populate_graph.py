import requests
from datetime import datetime, timedelta

AUTH_TOKEN = 'iefnasffc056'
PIXELA_API_ENDPOINT = 'https://pixe.la/v1/users'
USERNAME = 'sidd'
GRAPH_API_ENDPOINT = f'{PIXELA_API_ENDPOINT}/{USERNAME}/graphs'
GRAPH_ID = 'graph1'

POPULATE_GRAPH_ENDPOINT = f'{PIXELA_API_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'

# Authenticate oneself using the header instead of including it on the request body.
graph_API_header = {
    'X-USER-TOKEN': AUTH_TOKEN
}

today = datetime.now()
yesterday = datetime.now() - timedelta(2)

today_formatted_date = today.strftime("%Y%m%d")
yesterday_formatted_date = yesterday.strftime("%Y%m%d")

populate_graph_configuration = {
    'date': today_formatted_date,
    'quantity': input('How many hours of Coding did you do today? ')
}

api_response = requests.post(url=POPULATE_GRAPH_ENDPOINT, headers=graph_API_header, json=populate_graph_configuration)
print(api_response.text)
