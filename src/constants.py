import os
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
OPEN_WEATHER_API_KEY = os.environ.get('OPEN_WEATHER_API_KEY','')

WELCOME_MSG     = "Welcome to this simple weather app. This app uses the Open Weather API service to get the location coordinates and the temperature for the location entered."
ENTER_LOCATION  = "Please enter a location to get the temperature: "

OUTPUT_STATEMENT = "The temperature at {location} is {tempareture} F"
