import time
from recfib import recfib

def times_recfib(n):
    start = time.time()
    recfib(n)
    end = time.time()
    elapse = end - start
    return elapse
        
