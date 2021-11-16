import math

def isPrime(n):
    factor = 2
    while factor <= math.sqrt(n):
        if n%factor == 0:
            return False
        factor += 1
    return True

maxN = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        if abs(b) >= a:
            if abs(b) - a <= maxN:
                continue
        elif abs(b) <= maxN:
            continue
        cons, n = 0, 0
        while True:
            p = n*n + a*n + b
            if p < 0:
                break
            if not isPrime(p):
                break
            n += 1
        if n > maxN:
            maxN = n
            maxProd = a*b
print(maxProd)