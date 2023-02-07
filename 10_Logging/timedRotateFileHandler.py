import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#when s(seconds) m(minutes) h(hours) d(day) midnight, w0(monday)
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)


for _ in range(6):
    logger.info('Hello, world!')
    time.sleep(5)