# Context Manager
# great tool for resource management
# they allow you to allocate and release resources
# precisely when you want to




## File open example
with open('notes.txt', 'w') as file:
    file.write('some todoo...')


file = open('notes.txt', 'w')
try:
    file.write('some todoo...')
finally:
    file.close()




## Threading example
from threading import Thread, Lock
import time
database_value = 0

def increase(lock):
    global database_value

    # with lock == context manager
    with lock:
        local_copy = database_value
        # simulate processing and processing time
        local_copy += 1 
        time.sleep(0.1)
        # write processing back to global database_value
        database_value = local_copy

    lock.acquire()

    local_copy = database_value
    # simulate processing and processing time
    local_copy += 1 
    time.sleep(0.1)
    # write processing back to global database_value
    database_value = local_copy

    lock.release()








