import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

def getWeatherData():

    #build query
    params = {
    'access_key': WEATHER_API_KEY,
    'query': '24060',
    'units':  'f'
    }

    #get request
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    return api_response
    #print('Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))