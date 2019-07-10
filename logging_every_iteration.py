import logging
import sys
import os


def my_custom_logger(logger_name, level=logging.DEBUG, folder="logs"):
    """
    Method to return a custom logger with the given name and level
    """
    logger = logging.getLogger(logger_name)

    folder = folder + "/"
    os.makedirs(folder, exist_ok=True)
    logger.setLevel(level)
    format_string = ("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:"
                     "%(lineno)d — %(message)s")
    log_format = logging.Formatter(format_string)

    # Creating and adding the console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Creating and adding the file handler
    file_handler = logging.FileHandler(folder+logger_name, mode='a')
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":
    for item in range(10):
        logger = my_custom_logger(f"Logger{item}")
        logger.debug(item)
