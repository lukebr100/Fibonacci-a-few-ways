from natural_number import natural_number

#function fibonacci sequence using while loop
#input: n, non-negative integer
#output: list of n + 1 fib. numbers (n nontrivial fib. numbers)

def whilefib(n): 
    if natural_number(n) == True:      #checks n is non-negative integer
      F = [0, 1]                                # intialize first two entries
        if n == 0:                              # trivial case, 0th fib num                        
            return [F[0]]                       # retuns list of first entry of F
        elif n == 1:                            #trivial case, 0th, 1st fub num
            return F                            # list of first two fib num
        else:                                   #non-trivial n >= 2
            G = [0 for _ in range(n)]           # initialize list w/ n zeros
            tildeF = F + G                               # concatenated
            i = 0                               # intialize counter
            while i < n:                        # while i is less than n
                tildeF[i + 2] = tildeF[i + 1] + tildeF[i]                   # next fib. number is sum of prev two store into tildeF of (i plus 2)nd entry 
                i = i + 1                       # add to counter
            return tildeF                       # return vector er um list
    else:                                       #executes if n is not valid
        print("n must be a non-negative integer")
