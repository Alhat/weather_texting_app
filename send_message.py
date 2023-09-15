import os
from dotenv import load_dotenv
from twilio.rest import Client
import time

load_dotenv()  # Load environment variables from .env file
#Your AccountSID and Auth Token from console.twilio.com
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
MY_PHONE_NUMBER = os.getenv('MY_PHONE_NUMBER')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def sendWeather(weatherData):
# Send a message
    message = client.messages.create(
        body = 'Current temperature in %s is %d°F' % (weatherData['location']['name'], weatherData['current']['temperature']),
        to = MY_PHONE_NUMBER,    # Replace with recipient's number
        from_ = TWILIO_PHONE_NUMBER  # Use a Twilio number you've purchased or verified
    )
    time.sleep(20)
    print("\nmessage status: " + client.messages(message.sid).fetch().status + "\n")

