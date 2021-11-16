import math

def isPrime(n):
    factor = 2
    while factor <= math.sqrt(n):
        if n%factor == 0:
            return False
        factor += 1
    return True

sum = 0
for n in range(2,2000000):
    if isPrime(n):
        sum += n

print(sum)