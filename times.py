import time
from forfib import forfib
from recfib import recfib
from whilefib import whilefib

def fortime(n):
  start = time.time()
  forfib(n)
  end = time.time()
  elapse = end - start
  return elapse

def rectime(n):
  start = time.time()
  recfib(n)
  end = time.time()
  elapse = end - start
  return elapse


def whiletime(n):
  start = time.time()
  whilefib(i)
  end = time.time()
  elapse = end - start
  return elapse
 
