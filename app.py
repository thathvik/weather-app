from src.utils import get_location
from src.open_weather_api_connector import OpenWeatherApiConnector
from src.constants import OUTPUT_STATEMENT

from src.logger import get_logger

logger = get_logger(__name__)

def main() -> None:
    try:
        location_str = get_location()
        weather_api_connector = OpenWeatherApiConnector()
        temperature = weather_api_connector.get_temperature_for_location(location_str)
        print(f"{OUTPUT_STATEMENT.format(**{'location': location_str, 'tempareture': temperature})}")

    except Exception as global_exception:
        logger.error(f"main(): Unable to show weather information. Global Exception Occured: {global_exception}")


if __name__ == '__main__':
    main()
