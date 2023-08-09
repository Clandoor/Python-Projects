# POST Request to the API Endpoint creating the User.

import requests

USERNAME = 'sidd'
AUTH_TOKEN = 'iefnasffc056'
PIXELA_API_ENDPOINT = 'https://pixe.la/v1/users'

user_parameters = {
    'token': AUTH_TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# The 'json' parameter is the actual json data which we will send to the server.
response_from_pixela_user = requests.post(url=PIXELA_API_ENDPOINT, json=user_parameters)
print(response_from_pixela_user.text)
