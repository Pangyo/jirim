
import logging
import logging.handlers

# log instance
logger = logging.getLogger('yunjaekim')
fomatter = logging.Formatter('[%(levelname)s:%(lineno)s] %(asctime)s > %(message)s')

# file name
fileHandler = logging.FileHandler('./Operate.log')
streamHandler = logging.StreamHandler()

# link
fileHandler.setFormatter(fomatter)
streamHandler.setFormatter(fomatter)
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

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