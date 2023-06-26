from natural_number import natural_number
# function fibonacci sequence using for loop
# input: n, non-negative integer
# output: list of n + 1 fib. numbers (n nontrivial numbers)

def forfib(n): 
    if natural_number(n) == True:          # exceutes if n is non-negative integer
        F = [0, 1]                                  # base cases
        if n == 0:                                  # trivial case, 0th fib num
            return F.remove(1)                            # remove the element of F that equals 1, the only non-trivial number
        elif n == 1:                                # other trivial case, 0th and 1st fib num's
             return F                               # list of first two fib. numbers
        else:                                       # non-trivial case n >= 2
            G = [0 for _ in range(n)]                # intialize vector of zeros of length n
            tildeF = F + G                           # concatenate first two fib. numbers w/ list of (n - 1) zeros
            for i in range(2, n + 2):                  # for i from zero to n - 2
                tildeF[i] = tildeF[i - 1] + tildeF[i - 2]       # the next fib. number is the sum of the previous two
            return tildeF                           # returns the list of fib nums
    else:                                           # only executes if user inputs invalid 'n'
        print("n must be a non-negative integer") 

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
