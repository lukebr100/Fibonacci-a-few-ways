import time
def times_recfib(n):
    elapse = [0 for i in range(n)]
    for i in range(n):
        start = time.time()
        recfib(n)
        end = time.time()
        print(elapse[i])
    return elapse
        
