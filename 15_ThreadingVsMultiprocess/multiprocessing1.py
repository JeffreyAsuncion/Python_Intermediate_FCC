# Next steps read and try examples
# https://docs.python.org/3/library/multiprocessing.html

from multiprocessing import Process
import os
import time

# dummy example
def square_numbers():
    for i in range(100):
        i * i
        time.sleep(1)
        
processes = []
num_processes = os.cpu_count()

print(num_processes)


# create processes
for i in range(num_processes):
    p = Process(target=square_numbers) 
    # if target has args Process(target=square_numbers, args=())
    processes.append(p)

# start
# this starts each process
for p in processes:
    p.start()

# join
# this means that I want to wait for a process
# to finish. and while waiting block the main thread
# So Block the main thread until these processes are finished
for p in processes:
    p.join()

print('end main')