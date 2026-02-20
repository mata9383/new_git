def factor(n):
    if n==0:
        return 1
    return n*factor(n-1)