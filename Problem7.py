import math

def isPrime(n):
    factor = 2
    while factor <= math.sqrt(n):
        if n%factor == 0:
            return False
        factor += 1
    return True

amount = 0
n = 2
while amount != 10001:
    if isPrime(n):
        amount += 1
    n += 1
print(n-1)