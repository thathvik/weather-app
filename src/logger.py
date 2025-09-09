import logging
from typing import Optional
from logging import Logger

from src.constants import LOG_LEVEL

def setup_logging(log_level: str=LOG_LEVEL):
    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format='%(asctime)s [%(levelname)s] [%(name)s] (%(filename)s:%(funcName)s:%(lineno)d): %(message)s',
    )


def get_logger(name: Optional[str]=None) -> Logger:
    return logging.getLogger(name)

