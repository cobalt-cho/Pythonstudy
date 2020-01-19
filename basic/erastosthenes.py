def eratosthenes(n):
    multiple = set()
    for i in range(2,n+1):
        if i not in multiple :
            yield  i
            multiple.update(range(i*i,n+1,i))

print(list(eratosthenes(234)))