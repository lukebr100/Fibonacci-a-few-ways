import time
def times_recfib(n):
    start = time.time()
    recfib(n)
    end = time.time()
    elapse = end - start
    return elapse
        
