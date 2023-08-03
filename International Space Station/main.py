import requests
from datetime import datetime
import smtplib
from config import EMAIL_DOMAIN, SENDERS_EMAIL, PASSWORD
import time

# Details of locations in London, Ontario, Canada.
# Change it to your location by simply getting the values from any internet site.
MY_LATITUDE = 42.984924
MY_LONGITUDE = -81.245277


def get_position_of_iss():
    """
    This function calls the API and gets the current position of International Space Station in terms
    of Longitude and Latitude.
    :return: Float
    """

    iss_api_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_api_response.raise_for_status()
    iss_data = iss_api_response.json()

    # Converting the values into
    latitude_of_iss = float(iss_data["iss_position"]["latitude"])
    longitude_of_iss = float(iss_data["iss_position"]["longitude"])

    print(f"Current Latitude of ISS: {latitude_of_iss}\nCurrent Longitude of ISS: {longitude_of_iss}\n")

    return latitude_of_iss, longitude_of_iss


def get_your_sunset_sunrise_time():
    """
    This function calls the API passing certain parameters into the API call and fetching the sunrise
    and sunset times of the current location.
    Those times are based on the Latitude and the Longitude values.
    :return: bool
    """

    response = requests.get(f"https://api.sunrisesunset.io/json?lat={MY_LATITUDE}&lng={MY_LONGITUDE}")
    response.raise_for_status()
    data = response.json()

    sunrise_hour, sunset_hour = 0, 0

    # Converting in 24 hours format.
    if 'PM' in data['results']['sunrise']:
        sunrise_hour = (int(data['results']['sunrise'][0]) + 12) % 24

    else:
        sunrise_hour = int(data['results']['sunrise'][0])

    if 'PM' in data['results']['sunset']:
        sunset_hour = (int(data['results']['sunset'][0]) + 12) % 24

    else:
        sunrise_hour = int(data['results']['sunset'][0])

    print(f"Sunrise at Current Location: {sunrise_hour}")
    print(f"Sunset at Current Location: {sunset_hour}")

    current_hour = datetime.now().hour
    print(f"Current hour: {current_hour}")

    # This checks whether it is dark or not.
    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True

    return False


def check_coordinates(iss_lat, iss_long) -> bool:
    """
    This function compares latitude and longitude to that of the ISS. If they are in range, then it will
    return True otherwise False.
    :return: bool
    """

    min_detection_latitude, max_detection_latitude = MY_LATITUDE - 5, MY_LATITUDE + 5
    min_detection_longitude, max_detection_longitude = MY_LONGITUDE - 5, MY_LONGITUDE + 5

    is_in_latitude_range, is_in_longitude_range = False, False

    if min_detection_latitude <= iss_lat <= max_detection_latitude:
        is_in_latitude_range = True

    if min_detection_longitude <= iss_long <= max_detection_longitude:
        is_in_longitude_range = True

    if is_in_latitude_range and is_in_longitude_range:
        return True

    return False


def send_email():
    """
    This function sends the email to the user whenever the International Space Station is within the
    range of the user and given that it is nighttime.
    Invoked when it is night and when it is in the range of the user's location in terms of latitude
    and longitude.
    :return: None
    """

    alert_message = (f"Subject:International Space Station Overhead!\n\nLook up in the Night Sky "
                     f"and see the International Space Station zooming it's way"
                     f" across the heavens!!")

    with smtplib.SMTP(EMAIL_DOMAIN) as connection:

        # Securing the connection.
        connection.starttls()

        connection.login(user=SENDERS_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDERS_EMAIL, to_addrs=SENDERS_EMAIL, msg=alert_message)


iss_latitude, iss_longitude = get_position_of_iss()
is_currently_dark = get_your_sunset_sunrise_time()
is_in_range = check_coordinates(iss_lat=iss_latitude, iss_long=iss_longitude)

print(f"\nIs ISS in your range? {is_in_range}")
print(f"Is it dark at your location? {is_currently_dark}")

print("\nAPI Powered by SunriseSunset.io")

# Probably will be able to see ISS if it is dark and if it is in one's range.
while True:

    # Runs every 30 seconds.
    time.sleep(30)
    if is_in_range and is_currently_dark:
        send_email()
