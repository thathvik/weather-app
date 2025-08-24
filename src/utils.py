from src.constants import WELCOME_MSG, ENTER_LOCATION
from src.logger import get_logger

logger = get_logger(__name__)


def get_location():
    print(WELCOME_MSG)
    user_input = get_user_input()
    return user_input


def get_user_input():
    return input(ENTER_LOCATION)
