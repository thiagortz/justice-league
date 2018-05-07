import os

APP_NAME = 'JUSTICE_LEAGUE'
PORT = int(os.environ.get('PORT', 5000))
DEBUG_MODE = os.environ.get('DEBUG', False)
BLUEPRINT_VERSION = '/v1'

SMAN = {
    "url_api": os.getenv('{}_SMAN_URL'.format(APP_NAME))
}
