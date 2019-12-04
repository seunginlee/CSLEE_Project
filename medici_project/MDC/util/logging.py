import logging
import logging.handlers
import sys
#import RotatingFileHandler
sys.path.append('/home/ubuntu/myproject')

def logd():
		log = logging.getLogger('myproject_log')
		log.setLevel(logging.DEBUG)

		formatter = logging.Formatter('[%(levelname)s] (%(filename)s:%(lineno)d) > %(message)s')

		log_max_size = 10 * 1024 * 1024
		log_file_count = 20
		fileHandler = logging.handlers.RotatingFileHandler(filename='MDC/log/log.txt', maxBytes=log_max_size,backupCount=log_file_count)
		streamHandler = logging.StreamHandler()

		fileHandler.setFormatter(formatter)
		streamHandler.setFormatter(formatter)

		log.addHandler(fileHandler)
		log.addHandler(streamHandler)
		return log

if __name__ == '__main__':
    logd().debug('debug')
    logd().info('info')
    logd().warning('warning')
    logd().error('error')
    logd().critical('critical')
