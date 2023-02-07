import logging
import traceback

# try:
#     a = [1,2,3,]
#     val = a[4]
# except IndexError as e:
#     # include stack trace in the logger, exc_info=True
#     logging.error(e, exc_info=True)

try:
    a = [1,2,3,]
    val = a[4]
except:
    # include stack trace in the logger, exc_info=True
    logging.error('The error is %s', traceback.format_exc())


# 2:37:17