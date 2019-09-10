import json
import os

CONFIG = json.load(open('../config/default.json'))


def base_url():
    try:
        return os.environ['BASE_URL']
    except KeyError:
        return CONFIG['base_url']
