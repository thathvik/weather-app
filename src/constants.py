import os
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
OPEN_WEATHER_API_KEY = os.environ.get('OPEN_WEATHER_API_KEY','')

OUTPUT_STATEMENT = "OUTPUT: {tempareture}"