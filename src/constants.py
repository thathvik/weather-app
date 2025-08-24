import os
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
OPEN_WEATHER_API_KEY = os.environ.get('OPEN_WEATHER_API_KEY','')

OPEN_WEATHER_API_BASE_URL               = "http://api.openweathermap.org"
OPEN_WEATHER_API_GEOCODING_ENDPOINT     = "geo/1.0/direct"
OPEN_WEATHER_API_GEOCODING_OUTPUT_LIMIT = 5
OPEN_WEATHER_API_DATA_CALL_ENDPOINT_25  = "data/2.5/weather"
OPEN_WEATHER_API_DATA_CALL_ENDPOINT_3_ONE_CALL = "data/3.0/onecall"

VALID_OPEN_WEATHER_API_DATA_ENDPOINTS = [OPEN_WEATHER_API_DATA_CALL_ENDPOINT_25, OPEN_WEATHER_API_DATA_CALL_ENDPOINT_3_ONE_CALL]

OUTPUT_STATEMENT = "OUTPUT: {tempareture}"


# Strings used in open weather api connector
STR_LAT     = "lat"
STR_LON     = "lon"
STR_APIID   = "appid"
STR_Q       = "q"
STR_LIMIT   = "limit"
STR_CURRENT = "current"
STR_TEMP    = "temp"
STR_MAIN    = "main"
STR_UNITS   = "units"

# Unit types
STR_METRIC  = "metric"
STR_IMPERIAL= "imperial"