import time


def measure_loop(n):
    start = time.time()
    a = range(n)
    for item in a:
        print(item, end=" ")
    end = time.time()
    print("\n{} is the time taken for execution".format(end - start))


if __name__ == "__main__":
    measure_loop(10000)
