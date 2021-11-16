import math

def isPrime(n):
    factor = 2
    while factor <= math.sqrt(n):
        if n%factor == 0:
            return False
        factor += 1
    return True

factor = 2
while factor <= math.sqrt(600851475143):
    if isPrime(factor):
        if 600851475143%factor == 0:
            largest = factor
    factor += 1
print(largest)