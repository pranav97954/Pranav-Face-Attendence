def g(n,a):
    while n>=0:
        if a>=2**n:
            yield 1
            a-=2**n
        else:
            yield 0
        n-=1
    return
for e in g(6,25):
    print(e,end='')