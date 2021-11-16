import math

def isPrime(n):
    factor = 2
    while factor <= math.sqrt(n):
        if n%factor == 0:
            return False
        factor += 1
    return True

def isCircularPrime(n):
    if not isPrime(n): return False
    s = str(n)
    l = len(s)
    for i in range(l):
        if not isPrime(int(s[i:] + s[:i])): return False
    return True

count = 0
for i in range(2, 1000001):
    if isCircularPrime(i):
        count += 1
print(count)