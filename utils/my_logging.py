import logging
import sys
import os
import logging.handlers

# Logging levels ----> logging.DEBUG < logging.INFO < logging.WARNING <
#                                   logging.ERROR < logging.CRITICAL
# There are 5 log methods defined for each of the above 5 types
# For a specific log level, all the msgs with = or greater log level are logged
#
# Ex: log level is set to WARNING, msgs with DEBUG and INFO are ignored and
# only with WARNING, ERROR and CRITICAL are printed

FORMAT_STRING = ("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:"
                 "%(lineno)d — %(message)s")


def my_console_logger(logger_name, level=logging.DEBUG):
    """
    Method to return a custom console logger with the given name and level
    """
    logger = logging.getLogger(logger_name)
    console_handler = get_console_handler()
    logger.setLevel(level)
    logger.addHandler(console_handler)
    return logger


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    log_format = logging.Formatter(FORMAT_STRING)
    console_handler.setFormatter(log_format)
    return console_handler


def get_file_handler(filename):
    file_handler = logging.FileHandler(filename)
    log_format = logging.Formatter(FORMAT_STRING)
    file_handler.setFormatter(log_format)
    return file_handler


def my_custom_file_logger(logger_name, level=logging.INFO, folder="logs", add_console_logger=True):
    """
    Method to return a custom file logger with the given logger_name.
    if add_console_logger is set, it will add a console logger along with file logger
    folder: holds the folder name to store the log file. Default value is 'logs'
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    if folder[-1] != "/":
        folder = folder + "/"

    os.makedirs(folder, exist_ok=True)
    logger.addHandler(get_file_handler(folder + logger_name))

    if add_console_logger:
        logger.addHandler(get_console_handler())

    return logger


if __name__ == "__main__":
    # sample implementation
    critical_logger = my_console_logger("critical_log", level=logging.CRITICAL)
    critical_logger.critical("Printing critical message from critical logger")
    critical_logger.debug("Printing debug message from critical logger")

    warning_logger = my_console_logger("warning_log", level=logging.WARNING)
    warning_logger.critical("Printing critical message from warning logger")
    warning_logger.warning("Priniting warning messsage from warning logger")
    warning_logger.debug("Printing debug message from warning logger")

    debug_logger = my_console_logger("debug_log", level=logging.DEBUG)
    debug_logger.critical("Printing critical message from debug logger")
    debug_logger.warning("Printing warning message from debug logger")
    debug_logger.debug("Printing debug message from debug logger")

    my_logger = my_custom_file_logger("File1.log")
    my_logger.info("This is an info message")
