import json


def load_config(config_file: str = 'config.json') -> dict:
    with open(config_file, 'r') as config_file:
        return json.load(config_file)
