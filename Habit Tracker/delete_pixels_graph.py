import requests
from datetime import datetime

AUTH_TOKEN = 'iefnasffc056'
PIXELA_API_ENDPOINT = 'https://pixe.la/v1/users'
USERNAME = 'sidd'
GRAPH_API_ENDPOINT = f'{PIXELA_API_ENDPOINT}/{USERNAME}/graphs'
GRAPH_ID = 'graph1'

today = datetime.now()
today_formatted_date = today.strftime("%Y%m%d")

DELETE_GRAPH_ENDPOINT = f'{GRAPH_API_ENDPOINT}/{GRAPH_ID}/{today_formatted_date}'

# Authenticate oneself using the header instead of including it on the request body.
graph_API_header = {
    'X-USER-TOKEN': AUTH_TOKEN
}

delete_response = requests.delete(url=DELETE_GRAPH_ENDPOINT, headers=graph_API_header)
print(delete_response.text)

