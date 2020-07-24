def fact(n):
    result=1
    for el in range(1, n+1):
        result*=el
        yield result

for k in fact(5):
    print (k, end=" ")
