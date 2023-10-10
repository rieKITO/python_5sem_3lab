import logging
import sys

logging.basicConfig(level=logging.INFO, filename='logs\\infos.log', filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')
consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger = logging.getLogger()
logger.addHandler(consoleHandler)
