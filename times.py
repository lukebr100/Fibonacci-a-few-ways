import time
from methods import forfib, recfib, whilefib

# three fucnctions that intput a natural number
# output 0 elapse: time elapsed to peform a function from methods.py
# output 1 N: list of N fibonacci numbers

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
 
