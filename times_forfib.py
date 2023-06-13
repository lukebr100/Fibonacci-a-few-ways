import time

def times_forfib(n):
  elapse = [0 for i in range(100)]

  for i in range(n):
    start = time.time()
    forfib(n)
    end = time.time()
    elapse[i] = end - start
    print(elapse[i])
  
 return(elapse)
 
