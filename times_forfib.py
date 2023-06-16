import time
from forfib import forfib

def times_forfib(n):
  start = time.time()
  forfib(n)
  end = time.time()
  elapse = end - start
  return(elapse)
 
