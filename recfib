# input: n a natural number
# output: list of fibonacci numbers of length n + 1

def recfib(n):
    if natural_number(n) == True:            # executes only for non-negative integers
        if n == 0:                                    # base case 0
            return [0]
        elif n == 1:                                  # base case 1
            return recfib(0) + [1]
        else:                                         # non-trivial cases, n >= 2
            return  recfib(n - 1)   + [recfib(n - 1)[n - 1] + recfib(n - 2)[n - 2]]            # the previous list of fib. numbers concatenated with
    else:                                                                                      # a list of the sum of the last entries two function values
        print("n must be a non-negative integer")    # executes only for non-natural numbers
print(recfib(10))                                     # list of 3 non trivial fibonacci numbers
