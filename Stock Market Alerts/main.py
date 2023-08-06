import smtplib

import requests
from datetime import datetime
from datetime import timedelta
from random import choice
from config import EMAIL_DOMAIN, SENDERS_EMAIL, PASSWORD

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = 'XXXXXXXXXXXX'
NEWS_API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'


def get_stock_data():
    """
    This function fetches the stock data from the 'alphavantage.co' using its API, checks whether there was 5%
    change between yesterday and the day before yesterday, and prints out the appropriate message.
    :return: Float
    """

    alphavantage_api_parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey': ALPHAVANTAGE_API_KEY
    }

    alphavantage_api_response = requests.get(url='https://www.alphavantage.co/query', params=alphavantage_api_parameters)
    alphavantage_api_response.raise_for_status()

    stock_data = alphavantage_api_response.json()

    closing_price_yesterday = float(stock_data['Time Series (Daily)'][yesterday_date]['4. close'])
    closing_price_day_before_yesterday = float(stock_data['Time Series (Daily)'][day_before_yesterday_date]['4. close'])

    difference = closing_price_yesterday - closing_price_day_before_yesterday
    percentage_change = (difference / closing_price_day_before_yesterday) * 100

    print(f"Percentage Difference: {percentage_change}")

    return percentage_change


def get_news():
    """
    This function fetches the news of the specific company associated with the stock data from 'newsapi.org'.
    It then calls the function to send the alert if there is a noticeable change in the stock prices of the
    company.
    :return: str
    """

    newsapi_parameters = {
        'qInTitle': COMPANY_NAME,
        'apiKey': NEWS_API_KEY
    }

    newsapi_response = requests.get(url='https://newsapi.org/v2/everything', params=newsapi_parameters)
    newsapi_response.raise_for_status()

    articles = newsapi_response.json()['articles']

    random_title = choice(articles)['title']
    random_description = choice(articles)['description']

    percentage_change_in_stock = round(get_stock_data(), 2)

    message_to_client = ""

    if percentage_change_in_stock >= 1:
        message_to_client = (f"Subject: {COMPANY_NAME}: 🔺{percentage_change_in_stock}\n\n"
                             f"Headline: {random_title}\n"
                             f"Brief: {random_description}")

    elif percentage_change_in_stock <= -1:
        message_to_client = (f"Subject: {COMPANY_NAME}: 🔻{percentage_change_in_stock}\n\n"
                             f"Headline: {random_title}\n"
                             f"Brief: {random_description}")

    return message_to_client


def send_alert(message_to_client: str):
    """
    This function sends the alert if there are any drastic changes in the stock market.
    :return: None
    """

    if message_to_client == "":
        return

    with smtplib.SMTP(EMAIL_DOMAIN) as connection:

        # Securing the Connection
        connection.starttls()

        connection.login(user=SENDERS_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDERS_EMAIL, to_addrs=SENDERS_EMAIL, msg=message_to_client.encode('UTF-8'))


yesterday_date = str(datetime.now().date() - timedelta(days=1))
day_before_yesterday_date = str(datetime.now().date() - timedelta(days=2))

message_to_send = get_news()
send_alert(message_to_client=message_to_send)
