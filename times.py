import time
from methods import forfib, recfib, whilefib

def fortime(n):
  start = time.time()
  N = forfib(n)
  end = time.time()
  elapse = end - start
  return elapse, N

def rectime(n):
  start = time.time()
  N = recfib(n)
  end = time.time()
  elapse = end - start
  return elapse, N


def whiletime(n):
  start = time.time()
  N = whilefib(n)
  end = time.time()
  elapse = end - start
  return elapse, N
 
