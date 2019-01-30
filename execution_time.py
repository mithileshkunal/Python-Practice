import time
start = time.time()

a = range(10000)

for item in a:
    print(item, end=" ")

end = time.time()
print("\n{} is the time taken for execution".format(end-start))
