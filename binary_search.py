import utils.my_logging as my_logging
import math

logger = my_logging.my_console_logger(__name__, level=10)


def binary(array, find, start, end):
    if(start > end):
        return "Not Found"
    mid = math.floor((start + end) / 2)
    logger.debug("start:{0}\tend:{1}\tmid:{2}\t".format(start, end, mid))
    if array[mid] == find:
        return "Found {1} at index {0}".format(mid, array[mid])
    elif find > mid:
        return binary(array, find, mid+1, end)
    else:
        return binary(array, find, start, mid-1)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1100]
    logger.info(binary(array, 1100, 0, len(array)-1))
