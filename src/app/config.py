import os

APP_NAME = 'JUSTICE_LEAGUE'
PORT = int(os.environ.get('PORT', 5000))
DEBUG_MODE = os.environ.get('DEBUG', False)
BLUEPRINT_VERSION = '/v1'
VERSION = '1.0.0'

SECRET_KEY = os.environ.get('{}_SECRET_KEY', '7ghzgwkLGV3JTiJM5LJSz3YuS8zUCBjG')


SUPER_MAN = {
    "url_api": os.getenv('{}_SUPER_MAN_URL'.format(APP_NAME))
}


THE_FLASH = {
    "url_api": os.getenv('{}_THE_FLASH_URL'.format(APP_NAME))
}

SOLOMON_GRUNDY = {
    "url_api": os.getenv('{}_SOLOMON_GRUNDY_URL'.format(APP_NAME))
}