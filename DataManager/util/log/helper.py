""" Author : Jae Eun Yoo """

import logging
import logging.handlers


DEBUG 		= 0
INFO 		= 1
WARNING 	= 2
ERROR 		= 3
CRITICAL 	= 4
LOGGING_MSG_FORMAT  = '%(asctime)s$%(levelname)s$%(message)s'
loggers = dict()

# TODO : Implement following functions...
def get_logger(name):
	if loggers.get(name):
		return loggers.get(name)
	else:
		logger = logging.getLogger(name)
		logger.propagate = False
		logger.setLevel(logging.INFO)
		if not len(logger.handlers):
			try:
				log_handler = logging.handlers.RotatingFileHandler(filename='/work/etc/log/%s'%name, maxBytes=LOG_FILE_MAX_SIZE, backupCount=LOG_FILE_MAX_COUNT)
				log_handler.setFormatter(logging.Formatter(LOGGING_MSG_FORMAT))
				logger.addHandler(log_handler)
				loggers.update(dict(name=logger))
			except:
				#TODO:
				# Check if syslogd is working or not, if not should start syslogd forcely, if can not work, save to temp log
				pass
		return logger


def write_syslog_message(level, msg):
	logger = get_logger("system")
	write_message(logger, level, msg)


def write_message(logger, level, msg):
	if level is CRITICAL:
		logger.critical(msg)
	elif level is ERROR:
		logger.error(msg)
	elif level is WARNING:
		logger.warning(msg)
	elif level is INFO:
		logger.info(msg)
	else:
		logger.debug(msg)

	print("[{level}]".format(level=LOG_LEVE_STR[level]), msg)