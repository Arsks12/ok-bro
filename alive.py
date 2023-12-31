from logging import error as logerror
from os import environ
from time import sleep

from requests import get as rget

HAP = environ.get('HEROKU_APP_NAME', None)
BASE_URL = environ.get('BASE_URL_OF_BOT', None)
try:
    if len(BASE_URL) == 0:
        raise TypeError
except TypeError:
    BASE_URL = f"https://{HAP}.herokuapp.com" if HAP else None
PORT = environ.get('PORT', None)
if PORT is not None and BASE_URL is not None:
    while True:
        try:
            rget(BASE_URL).status_code
            sleep(600)
        except Exception as e:
            logerror(f"alive.py: {e}")
            sleep(2)
            continue
