import math

def isPrime(n):
    if n <= 1: return False
    factor = 2
    while factor <= math.sqrt(n):
        if n%factor == 0: return False
        factor += 1
    return True

def isTruncatablePrime(n):
    if not isPrime(n): return False
    s = str(n)
    l = len(s)
    for i in range(1, l):
        if not isPrime(int(s[:i])) or not isPrime(int(s[i:])): return False
    return True

primes, sum , i = 0, 0, 10
while primes < 11:
    if isTruncatablePrime(i):
        primes += 1
        sum += i
    i += 1
print(sum)