# recap, how we can create and start multiple threads,
# then, we will learn how we can share data between threads
# and how to use locks to prevent race conditions.
# we will also learn what is a daemon process
# and how we can use a queue for thread safe data exchanges


from threading import Thread

def square_numbers():
    for i in range(100):
        i * i

if __name__ == "__main__":
    threads = []
    num_threads = 10

    # create threads
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start threads
    for thread in threads:
        thread.start()

    # join threads: wait for them to complete
    for thread in threads:
        thread.join()

    print('End Main!!!')