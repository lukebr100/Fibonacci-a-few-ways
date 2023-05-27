def forfib(n):
    if isinstance(n, int) == 1 and n >= 0:
        if n == 0:
            forfib = [0]
            return forfib
        elif n == 1:
            forfib = [0, 1]
            return forfib
        else:
            forfib = [0, 1] + [0] * (n - 1)
            for i in range(n - 1):
                forfib[i + 2] = forfib[i + 1] + forfib[i]
                
            return forfib
    else:
        print("n must be a non-negative integer")
