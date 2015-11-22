import time

t = time.time()
# do stuff

for x in range(0,10000000):
    y = 1


elapsed = time.time() - t

print(elapsed)

