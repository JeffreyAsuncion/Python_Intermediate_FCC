# Queues are excellent for thread safe 
# and process safe data exchanges and data processing 
# in multi threaded or mutli processing environments

# recap, how we can create and start multiple threads,
# then, we will learn how we can share data between threads
# and how to use locks to prevent race conditions.
# we will also learn what is a daemon process
# and how we can use a queue for thread safe data exchanges

# a Queue is a linear data structure 
# that follows the FIFO == first in first out


from threading import Thread, Lock
from queue import Queue
import time




if __name__ == "__main__":

    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    # 3 2 1 -->
    first = q.get()
    print(first)

    # with threads, use .task_done()
    # this tell that we are done processing wiht this object, and to continue
    q.task_done()

    # .join() blocks until all items in the queue have been gotten and processed
    q.join()

    # check if queue is empty
    # q.empty() # returns True / False

    print('end main')

