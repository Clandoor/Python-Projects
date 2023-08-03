import requests

api_response = requests.get(url='https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean')
api_response.raise_for_status()

question_data = api_response.json()['results']
