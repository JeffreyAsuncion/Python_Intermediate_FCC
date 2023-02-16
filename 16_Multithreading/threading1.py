# recap, how we can create and start multiple threads,
# then, we will learn how we can share data between threads
# and how to use locks to prevent race conditions.
# we will also learn what is a daemon process
# and how we can use a queue for thread safe data exchanges

from threading import Thread, Lock
import time
database_value = 0

def increase(lock):
    global database_value

    with lock:
        local_copy = database_value
        # simulate processing and processing time
        local_copy += 1 
        time.sleep(0.1)
        # write processing back to global database_value
        database_value = local_copy

    # lock.acquire()

    # local_copy = database_value
    # # simulate processing and processing time
    # local_copy += 1 
    # time.sleep(0.1)
    # # write processing back to global database_value
    # database_value = local_copy

    # lock.release()



if __name__ == "__main__":

    lock = Lock()
    print(f'start value {database_value}')

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'end value {database_value}')

    print('end main')