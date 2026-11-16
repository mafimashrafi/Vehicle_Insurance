from src.logger import logging
from src.exception import MyException
import sys

# logging.debug("This is a Debug message")
# logging.info("This is an Info message")
# logging.warning("This is a Warning message")
# logging.error("This is an Error message")
# logging.critical("This is a Critical message")

try:
    a = 1+"z"
except Exception as e:
    logging.error(e)
    raise MyException(e, sys) from e