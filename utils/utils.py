import json
import os
import re

CONFIG = json.load(open('../config/default.json'))


def base_url():
    try:
        return os.environ['BASE_URL']
    except KeyError:
        return CONFIG['base_url']


def browser():
    try:
        return os.environ['BROWSER']
    except KeyError:
        return CONFIG['browser']


def is_currency(value: str) -> bool:
    return bool(re.match(r'\$\d*\.\d{2}$', value))
