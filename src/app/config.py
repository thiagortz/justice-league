import os

APP_NAME = 'JUSTICE_LEAGUE'
PORT = int(os.environ.get('PORT', 5000))
DEBUG_MODE = os.environ.get('DEBUG', False)
BLUEPRINT_VERSION = '/v1'

SUPER_MAN = {
    "url_api": os.getenv('{}_SUPER_MAN_URL'.format(APP_NAME))
}


THE_FLASH = {
    "url_api": os.getenv('{}_THE_FLASH_URL'.format(APP_NAME))
}

SOLOMON_GRUNDY = {
    "url_api": os.getenv('{}_SOLOMON_GRUNDY_URL'.format(APP_NAME))
}