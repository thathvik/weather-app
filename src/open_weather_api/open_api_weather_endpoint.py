from enum import Enum

from src.constants import OPEN_WEATHER_API_DATA_CALL_ENDPOINT_25, OPEN_WEATHER_API_DATA_CALL_ENDPOINT_3_ONE_CALL, STR_CURRENT, STR_MAIN, STR_TEMP

from src.logger import get_logger

logger = get_logger(__name__)


class OpenApiWeatherEndpoint(Enum):
    FREE_ENDPOINT = OPEN_WEATHER_API_DATA_CALL_ENDPOINT_25
    PAID_ENDPOINT = OPEN_WEATHER_API_DATA_CALL_ENDPOINT_3_ONE_CALL

    def extract_temperature_from_response(self, api_response_json: dict) -> float:
        """
        Based on the Endpoint picked, a different extract method is called. 

        Another approach would be to create a data object with all the fields extracted as callable class variables.
        Perhaps a class factory to extract the right output object based on the enpoint picked. 
        For the current phase, only temperature is extracted, so this approach is picked to keep it simple. 
        Will improve in future iterations
        """
        logger.debug(f"+extract_temperature_from_response()")
        map_weather_extraction_function = {
            OpenApiWeatherEndpoint.FREE_ENDPOINT: self._extract_main_temperature_from_api_reponse_v2_5,
            OpenApiWeatherEndpoint.PAID_ENDPOINT: self._extract_current_temperature_from_api_reponse_v3_0
        }

        if self in map_weather_extraction_function.keys():
            method = map_weather_extraction_function[self]
        else:
            msg = f"extract_temperature_from_response(): Unexpected Endpoint. Expected {map_weather_extraction_function.keys()=}"
            logger.error(msg)
            raise ValueError(msg)
        
        temperature = method(api_response_json)

        logger.debug(f"-extract_temperature_from_response(): Extracted temperature: {temperature}")
        return temperature


    def _extract_main_temperature_from_api_reponse_v2_5(self, api_response_json: dict) -> float:
        logger.debug(f"+_extract_main_temperature_from_api_reponse_v2_5()")
        assert isinstance(api_response_json, dict), f"_extract_current_temperature_from_api_response_v2(): Expected dict, received {type(api_response_json)=}"

        # Taking a more pythonic approach for this method for validation
        if STR_MAIN not in api_response_json:
            msg = f"_extract_main_temperature_from_api_reponse_v2_5(): '{STR_MAIN}' not available in the weather api reponse. Received {api_response_json.keys()=}"
            logger.error(msg)
            raise ValueError(msg)

        main_weather = api_response_json[STR_MAIN]

        if not isinstance(main_weather, dict) or STR_TEMP not in main_weather:
            msg = f"_extract_main_temperature_from_api_reponse_v2_5(): '{STR_TEMP}' not present in the main_weather object in the response. Received {type(main_weather)=} {main_weather=}"
            logger.error(msg)
            raise ValueError(msg)

        temperature = main_weather[STR_TEMP]
        temperature = float(temperature)

        logger.debug(f"-_extract_main_temperature_from_api_reponse_v2_5()")
        return temperature


    def _extract_current_temperature_from_api_reponse_v3_0(self, api_response_json: dict) -> float:
        logger.debug(f"+_extract_current_temperature_from_api_reponse_v3_0()")
        assert isinstance(api_response_json, dict), f"_extract_current_temperature_from_api_reponse_v3_0(): Expected dict, received {type(api_response_json)=}"

        # Taking a more pythonic approach for this method for validation
        if STR_CURRENT not in api_response_json:
            msg = f"_extract_current_temperature_from_api_reponse_v3_0(): '{STR_CURRENT}' not available in the weather api reponse. Received {api_response_json.keys()=}"
            logger.error(msg)
            raise ValueError(msg)

        current_weather = api_response_json[STR_CURRENT]

        if not isinstance(current_weather, dict) or STR_TEMP not in current_weather:
            msg = f"_extract_current_temperature_from_api_reponse_v3_0(): '{STR_TEMP}' not present in the current_weather object in the response. Received {type(current_weather)=} {current_weather=}"
            logger.error(msg)
            raise ValueError(msg)

        temperature = current_weather[STR_TEMP]
        temperature = float(temperature)

        logger.debug(f"-_extract_current_temperature_from_api_reponse_v3_0()")
        return temperature
