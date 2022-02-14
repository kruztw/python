import logging

#logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.DEBUG)   # version 3.9

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL
logging.basicConfig(filename='output.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m%d%Y %I:%M:%S %p')
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
