import logging

try:
    print(a)
except:
    logging.exception("Error occured while printing")