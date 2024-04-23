import logging
import sys


import logging.config

FORMAT = "[%(levelname)s  %(name)s %(module)s:%(lineno)s - %(funcName)s() - %(asctime)s]\n\t %(message)s \n"
TIME_FORMAT = "%d.%m.%Y %I:%M:%S %p"
logging.config.fileConfig(fname='logger/config.ini', disable_existing_loggers=False)

logger = logging.getLogger('projeto')
