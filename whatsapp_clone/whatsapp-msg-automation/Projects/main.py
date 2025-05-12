from twilio.rest import Client
from datetime import datetime
import time

# Twilio credentials
account_sid = "AC572844d1fa8292c7cdb02043242c48eb"
auth_token = "c85847182b408049f63f6de3f1ba2402"

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message):
    try:
        message = client.messages.create(
            from_='whatsapp+12792258886',  # Twilio Sandbox Number
            to=f'whatsapp:{+919492169998}',  # Your mobile number
            body=message
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print('An error occurred:', e)

# Hardcoded inputs
name = 'sai anna'
recipient_number = '+919059296341'  # Your mobile number
message = 'hi'

# Input for scheduled time
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24hr format): ')

scheduled_datetime = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
current_datetime = datetime.now()
delay_seconds = (scheduled_datetime - current_datetime).total_seconds()

if delay_seconds <= 0:
    print('The specified time has already passed. Please enter a future time.')
else:
    print(f'Message scheduled to be sent to {name} at {scheduled_datetime}.')
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number, message)
