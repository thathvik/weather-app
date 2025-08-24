import requests

from http import HTTPStatus
from urllib.parse import urljoin

from typing import Tuple, Optional
from requests import Response

from src.open_weather_api.open_api_weather_endpoint import OpenApiWeatherEndpoint

from src.constants import (
    OPEN_WEATHER_API_KEY, OPEN_WEATHER_API_BASE_URL, OPEN_WEATHER_API_GEOCODING_ENDPOINT,
    OPEN_WEATHER_API_GEOCODING_OUTPUT_LIMIT, STR_LAT, STR_LON, STR_LIMIT, STR_Q, STR_APIID, STR_UNITS, 
    STR_METRIC, STR_IMPERIAL
)

from src.logger import get_logger

logger = get_logger(__name__)


class OpenWeatherApiConnector:

    def __init__(self):
        self.BASE_URL   = OPEN_WEATHER_API_BASE_URL
        self.API_KEY    = OPEN_WEATHER_API_KEY

        self.WEATHER_DATA_ENDPOINT  = OpenApiWeatherEndpoint.FREE_ENDPOINT
        self.GEOCODING_ENDPOINT     = OPEN_WEATHER_API_GEOCODING_ENDPOINT


    def get_temperature_for_location(self, location: str, units) -> float:

        latitude, longitude = self.get_location_coordinates(location)
        temperature = self.get_temperature(latitude, longitude, units)
        
        return temperature


    def get_temperature(self, latitude: float, longitude: float, units: str = STR_METRIC) -> float:

        api_response_json = self._make_weather_api_call(latitude, longitude, units)
        
        temperature = self.WEATHER_DATA_ENDPOINT.extract_temperature_from_response(api_response_json)
        temperature = round(temperature, 2)

        return temperature


    def get_location_coordinates(self, location_str: str) -> Tuple[float, float]:
        latitude: Optional[float] = None
        longitude: Optional[float] = None

        api_response_json = self._make_geocoding_api_call(location_str)
        latitude, longitude = self._extract_coordinates_from_api_reponse(api_response_json)

        return latitude, longitude
    

    def _make_weather_api_call(self, latitude: float, longitude: float, units: str) -> dict:
        logger.debug(f"+_make_weather_api_call()")

        params = {
            STR_LAT   : latitude,
            STR_LON   : longitude, 
            STR_UNITS : units,
            STR_APIID : self.API_KEY
        }

        response = self._make_api_call(self.WEATHER_DATA_ENDPOINT.value, params)
        api_response_json = response.json()

        if not isinstance(api_response_json, dict):
            msg = f"_make_weather_api_call(): Expected an dict from the response json. Received {type(api_response_json)=} {api_response_json=}"
            logger.error(msg)
            raise ValueError(msg)

        logger.debug(f"-_make_weather_api_call()")
        return api_response_json


    def _make_geocoding_api_call(self, location_str: str) -> list[dict]:
        logger.debug(f"+_make_geocoding_api_call()")

        params = {
            STR_Q     : location_str,
            STR_LIMIT : OPEN_WEATHER_API_GEOCODING_OUTPUT_LIMIT,
            STR_APIID : self.API_KEY
        }

        response = self._make_api_call(self.GEOCODING_ENDPOINT, params)
        api_response_json = response.json()

        if not isinstance(api_response_json, list):
            msg = f"_make_geocoding_api_call(): Expected an list from the response json. Received {type(api_response_json)=} {api_response_json=}"
            logger.error(msg)
            raise ValueError(msg)
        
        logger.debug(f"-_make_geocoding_api_call()")
        return api_response_json

    
    def _make_api_call(self, end_point: str, params: dict) -> Response:
        logger.debug(f"+_make_api_call()")

        url = urljoin(self.BASE_URL, end_point)
        response = requests.get(url, params=params)

        # Pythonic approach, exception is raised in case of a bad response
        if response.status_code != HTTPStatus.OK:
            logger.error(f"_make_api_call(): Request was not successfull. Response Status code: {response.reason} : {response.status_code}")
            response.raise_for_status()

        logger.debug(f"-_make_api_call()")
        return response
    
    
    def _extract_coordinates_from_api_reponse(self, api_response_json: list[dict], object_index: int = 0) -> Tuple[float, float]:
        logger.debug(f"+_extract_coordinates_from_api_reponse()")
        assert isinstance(api_response_json, list), f"_extract_coordinates_from_api_reponse(): Expected list recevied {type(api_response_json)}"

        # Taking a more traditional coding (Java and C) approach for this method for validation
        latitude: Optional[float] = None
        longitude: Optional[float] = None

        if len(api_response_json) > object_index:
            location_object = api_response_json[object_index]

            if isinstance(location_object, dict) and STR_LAT in location_object and STR_LON in location_object:
                latitude = location_object[STR_LAT]
                longitude = location_object[STR_LON]

                latitude = float(latitude)
                longitude = float(longitude)
            
            else:
                msg = f"_extract_coordinates_from_api_reponse(): '{STR_LAT}' '{STR_LON}' not present in the location object in the response. Received {location_object=}"
                logger.error(msg)
                raise ValueError(msg)
            
        else:
            msg = f"_extract_coordinates_from_api_reponse(): '{object_index}' is out of range in the geocoding api response object. Received {len(api_response_json)=}"
            logger.error(msg)
            raise ValueError(msg)
        
        logger.debug(f"-_extract_coordinates_from_api_reponse()")
        return latitude, longitude


if __name__ == "__main__":
    # Simple test to run locally and check the functionality.
    # Unittests coming soon.
    test_location = "Boston"
    open_weather_api_connector = OpenWeatherApiConnector()
    temperature = open_weather_api_connector.get_temperature_for_location(test_location, STR_IMPERIAL)
    print(temperature)
