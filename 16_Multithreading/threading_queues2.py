from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(q, lock):
    while True:
        value = q.get()

        # processing
        with lock:
            print(f'in  {current_thread().name} got {value}')
        q.task_done()

        ## this would break the infinite loop, the daemon below helps break the loop 
        # if <condition>:
        #     break


if __name__ == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        # this daemon helps break the loop, research
        thread.daemon=True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()


    print('end main')

