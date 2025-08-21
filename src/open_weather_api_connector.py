from typing import Optional

from src.constants import OPEN_WEATHER_API_KEY
from src.logger import get_logger

logger = get_logger(__name__)


class OpenWeatherApiConnector:

    def __init__(self):
        self.base_url = ""
        self.geocoding_extention = ""
        self.API_KEY = OPEN_WEATHER_API_KEY


    # maybe not needed
    def _verify_connection(self):
        pass


    def get_location_coordinates(self):
        pass


    def get_temperature_for_location(self, location: str) -> str:
        temperature: Optional[str] = None
        return temperature


    def get_temperature(self):
        pass


    def _make_weather_api_call(self):
        pass


    def _make_geocoding_api_call(self):
        pass

    
    def _make_api_call(self):
        pass
