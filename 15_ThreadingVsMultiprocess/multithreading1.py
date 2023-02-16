# Next steps read and try examples

from threading import Thread
import os
import time

# dummy example
def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)
        
threads = []
num_threads = 10


# create processes
for i in range(num_threads):
    t = Thread(target=square_numbers) 
    # if target has args Process(target=square_numbers, args=())
    threads.append(t)

# start
# this starts each thread
for t in threads:
    t.start()

# join
for t in threads:
    t.join()

print('end main')