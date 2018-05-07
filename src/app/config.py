import os

PORT = int(os.environ.get('PORT', 5000))
DEBUG_MODE = os.environ.get('DEBUG', False)
BLUEPRINT_VERSION = '/v1'

SMAN = {
    "url_api": " http://www.mocky.io/v2"
}
