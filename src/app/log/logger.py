import logging

FORMAT = '[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s - %(funcName)20s()] : %(message)s'
DATE_FMT = '%m-%d %H:%M:%S'

logging.basicConfig(level=logging.INFO,
                    format=FORMAT,
                    datefmt=DATE_FMT)


class Logger(object):
    def __init__(self, context):
        self._context = context

    def get_logger(self):
        return logging.getLogger(self._context)
