def hello(n):
    fact =1
    for x in range(1, n+1):
        fact = fact * x
    return fact

print(hello(3))

