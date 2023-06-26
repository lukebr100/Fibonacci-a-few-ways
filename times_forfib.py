import time
from forfib import forfib
from recfib import recfib

def times_forfib(n):
  start = time.time()
  forfib(n)
  end = time.time()
  elapse = end - start
  return elapse

def times_recfib(n):
  start = time.time()
  recfib(n)
  end = time.time()
  elapse = end - start
  return elapse
 
