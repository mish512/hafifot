import json
import logging


def load_config(config_file: str = 'config.json') -> dict:
    with open(config_file, 'r') as config_file:
        return json.load(config_file)


def create_logger(name: str = "__name__", level: int = logging.INFO, log_file: str = 'log.log'):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    logger_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(logger_format)

    logger.addHandler(handler)
    return logger
