from utils import my_logging
import random


def random_demo():
    my_log = my_logging.my_console_logger(__name__, 20)
    a = [x for x in range(10)]
    my_log.info("Before shuffling:{}".format(a))
    random.shuffle(a)
    my_log.info("After shuffling:{}".format(a))
    my_log.info(random.random())


if __name__ == "__main__":
    random_demo()
