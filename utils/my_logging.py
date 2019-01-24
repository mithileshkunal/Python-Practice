import logging
import sys
import logging.handlers

# Logging levels ----> logging.DEBUG < logging.INFO < logging.WARNING <
#                                   logging.ERROR < logging.CRITICAL
# There are 5 log methods defined for each of the above 5 types
# For a specific log level, all the msgs with = or greater log level are logged
#
# Ex: log level is set to WARNING, msgs with DEBUG and INFO are ignored and
# only with WARNING, ERROR and CRITICAL are printed.


def my_custom_logger(logger_name, level=logging.DEBUG):
    """
    Method to return a custom logger with the given name and level
    """
    logger = logging.getLogger(logger_name)
    console_handler = logging.StreamHandler(sys.stdout)
    format_string = ("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:"
                     "%(lineno)d — %(message)s")
    log_format = logging.Formatter(format_string)
    console_handler.setFormatter(log_format)
    logger.setLevel(level)
    logger.addHandler(console_handler)
    return logger


if __name__ == "__main__":
    critical_logger = my_custom_logger("critical_log", level=logging.CRITICAL)
    critical_logger.critical("Printing critical message from critical logger")
    critical_logger.debug("Printing debug message from critical logger")

    warning_logger = my_custom_logger("warning_log", level=logging.WARNING)
    warning_logger.critical("Printing critical message from warning logger")
    warning_logger.warning("Priniting warning messsage from warning logger")
    warning_logger.debug("Printing debug message from warning logger")

    debug_logger = my_custom_logger("debug_log", level=logging.DEBUG)
    debug_logger.critical("Printing critical message from debug logger")
    debug_logger.warning("Printing warning message from debug logger")
    debug_logger.debug("Printing debug message from debug logger")
