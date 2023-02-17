# 04:47:52
# a process pool can be used to manage multiple processes
# a process pool object controls a pool of worker processes
# to which jobs can be submitted

# and it can manage the available processes for you and split
# data into smaller chunks, which can then be processed 
# in parallel by different processes. 

from multiprocessing import Pool

def cube(number):
    return number * number * number

if __name__ == "__main__":
    
    numbers = range(10)
    pool = Pool()
    
    # important methods : map, apply, join, close
    result = pool.map(cube, numbers)
    
    # pool.apply(cube, numbers[0])

    # allocate pools, split data, run (asynchronous) this method in parallel, and return result

    # automatically allocate the maximum number of available processes for you
    # and create different processes
    # so typically, this will create as many processes as you have cores on your machine
    # it will split this iterable into an equal sized chunks,
    # and submit this to this functiion
    # function is now executed in parallel

    pool.close()
    # wait for pool to process all the calculations and return results
    pool.join()
    
    print(result)