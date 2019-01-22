import time
start_time = time.time()
print(sum([item for item in range(100000000)]))
end_time = time.time() - start_time
print(end_time)

start_time = time.time()
print(sum(item for item in range(100000000)))
end_time = time.time() - start_time
print(end_time)
