import requests

AUTH_TOKEN = 'iefnasffc056'
PIXELA_API_ENDPOINT = 'https://pixe.la/v1/users'
USERNAME = 'sidd'
GRAPH_API_ENDPOINT = f'{PIXELA_API_ENDPOINT}/{USERNAME}/graphs'
GRAPH_ID = 'graph1'

# Authenticate oneself using the header instead of including it on the request body.
graph_API_header = {
    'X-USER-TOKEN': AUTH_TOKEN
}

graph_configuration = {
    'id': GRAPH_ID,
    'name': 'Coding Graph',
    'unit': 'Hours',
    'type': 'float',
    'color': 'sora',
}

response_from_pixela_graph = requests.post(url=GRAPH_API_ENDPOINT, json=graph_configuration, headers=graph_API_header)
print(response_from_pixela_graph.text)
print(response_from_pixela_graph.json())

