import logging
import logging.config
from os import path
from conf.config import get_settings

logger=None
def Logger():
    global logger
    if logger is None:
        zLogFile = get_settings().LOGFILE_PATH
        zLogConfFile = get_settings().LOGCONF_PATH
        import os.path
        import os
        if not os.path.isfile(zLogFile):
     
            directory = os.path.dirname(zLogFile)

            if not os.path.exists(directory):
                try:
                    os.makedirs(directory)
                except OSError as e:
                    print(f"An error occurred while creating the directory '{directory}': {e}")


            if not os.path.isfile(zLogFile):

                try:
                    with open(zLogFile, "w") as file:
                        print(f"The file '{zLogFile}' has been created.")
                except IOError:
                    print(f"An error occurred while creating the file '{zLogFile}'.")

        logging.config.fileConfig(fname= zLogConfFile)
        logger = logging.getLogger('logfile')
        logger.info('Log file Created')
        return logger
    else:
        return logger

