# Different log levels
# different configuration options
# how to use different log handler
# how to capture stack trace
# how to use rotating file handler

# Next steps
# https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

# https://docs.python.org/3/library/logging.html
import logging
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S'
)   # this is ensure the lowestlevel to be printed, datetime, and name

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')    # printed wo basic config
# logging.error('This is an error message')       # printed wo basic config
# logging.critical('This is a critical message')  # printed wo basic config

import helper

