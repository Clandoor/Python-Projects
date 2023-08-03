import smtplib
import random
import pandas
from datetime import datetime

EMAIL_DOMAIN = 'smtp.gmail.com'
SENDERS_EMAIL = 'test@gmail.com'
PASSWORD = 'xxxxxxxxxxxxxxxx'


def draft_the_letter():
    """
    This function will open a random file, extract the message out of that file.
    Invoked when the current date aligns with any of the employee's birthday.
    :return: String
    """

    file_path = f'letter_templates/letter_{random.randint(1, 6)}.txt'

    try:
        with open(file_path, 'r') as file_pointer:
            birthday_message = file_pointer.read()

            # Replacing the '[NAME]' with the recipient's name.
            birthday_message = birthday_message.replace('[NAME]', employee_name)

    except:
        print("Unexpected Error.")

    return birthday_message


def send_email(recipients_email, birthday_message):
    """
    This function is responsible for sending the email to the intended recipient.
    :return: String
    """

    with smtplib.SMTP(EMAIL_DOMAIN) as connection:

        # Securing the connection
        connection.starttls()

        # Logging in from the email from which we want to send the email.
        connection.login(user=SENDERS_EMAIL, password=PASSWORD)

        try:

            # Encoding to avoid UnicodeEncodeError Exception.
            connection.sendmail(from_addr=SENDERS_EMAIL,
                                to_addrs=recipients_email,
                                msg=birthday_message.encode('UTF-8'))

        except UnicodeEncodeError:
            return "There was an Error. Please check the details again."

        except smtplib.SMTPRecipientsRefused:
            return f"Failed to deliver to {recipients_email}."

        except smtplib.SMTPSenderRefused:
            return f"Failed to send the email from {SENDERS_EMAIL}."

    return "Email Successfully Sent to " + recipients_email


# Fetching the current day and month.
present = datetime.now()
current_day = present.day
current_month = present.month

data_frame = pandas.read_csv('birthdays.csv')

for row in data_frame.index:
    if data_frame.iloc[row]['month'] == current_month and data_frame.iloc[row]['day'] == current_day:
        employee_name = data_frame.iloc[row]['name']
        employee_email = data_frame.iloc[row]['email']

        message = draft_the_letter()
        confirmation = send_email(recipients_email=employee_email,
                                  birthday_message=f"Subject:Happy Birthday!!\n\n{message}")

        print(confirmation)

    else:
        print("No Employees' Birthday Today.")
