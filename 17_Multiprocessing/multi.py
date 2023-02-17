# we will recap how we can create and start multiple processes.
# then we will learn how we can share data between processes, 
# we will recap how to use locks to prevent race and how to use queues
# we will learn how to use a process pool to easily manage multiple processes.


# This is the how to setup multiprocessing
from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(1)


if __name__ == "__main__":

    processes = []
    num_processes = os.cpu_count()
    # number of CPUs on the machine, Usually a good choice for the number of processes
    

    # create processes and assign a function for each process
    for i in range(num_processes):
        p = Process(target=square_numbers) 
        # if target has args Process(target=square_numbers, args=())
        processes.append(p)

    # start all processes
    for p in processes:
        p.start()

    # wait for all processes to finish
    # block the main program until these processes are finished
    for p in processes:
        p.join()


    print('end main')