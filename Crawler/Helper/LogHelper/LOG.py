'''
Created on 2016. 5. 14.

@author: yunjae
'''

import logging
import logging.handlers

from Common.Global import Global


# log instance
logger = logging.getLogger('yunjaekim')
fomatter = logging.Formatter('[%(levelname)s:%(lineno)s] %(asctime)s > %(message)s')

def Initialize():
    
    try:
        path =  Global.GetLogFilePath()   

        fileHandler = logging.FileHandler(path + "\Crawler.log")
        streamHandler = logging.StreamHandler()

        # link
        fileHandler.setFormatter(fomatter)
        streamHandler.setFormatter(fomatter)
        logger.addHandler(fileHandler)
        logger.addHandler(streamHandler)

    except:
        return False;
    else:
        return True;

def DEBUG(msg):
    logger.setLevel(logging.DEBUG)
    logger.debug(msg)

def INFO(msg):
    logger.setLevel(logging.INFO)
    logger.info(msg)

def FATAL(msg):
    logger.setLevel(logging.FATAL)
    logger.fatal(msg)
    
def WARN(msg):
    logger.setLevel(logging.WARN)
    logger.warn(msg)