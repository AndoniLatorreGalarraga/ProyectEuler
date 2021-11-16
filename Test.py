import math

def isPrime(n):
    factor = 2
    while factor <= math.sqrt(n):
        if n%factor == 0:
            return False
        factor += 1
    return True

def perms(l, s):
    if len(l) == 1:
        return [s + str(l[0])]
    ans = []
    for i in l:
        newL = l.copy()
        newL.remove(i)
        ans = ans + perms(newL, s + str(i))
    return ans

def gcd(n, m):
    if m < n:
        m, n = n, m
    while n != 0:
        m, n = n, m%n
    return m

def lcm(n, m):
    return n*m/gcd(n, m)

def divisors(n):
    ans = 0
    for i in range(1, round(math.sqrt(n)+1)):
        if n%i == 0:
            if n/i == i:
                ans += 1
            else:
                ans += 2
    return ans

def d(n):
    divisors = [1]
    for div in range(2, round(math.sqrt(n))+1):
        if n%div == 0:
            if n/div == div:
                divisors.append(div)
            else:
                divisors += [div, n/div]
    sum = 0
    for div in divisors:
        sum += div
    return sum

def isAmicable(a):
    b = d(a)
    return d(b) == a and a != b
    
def simp(n, m):
    a, b = n, m
    if m < n:
        m, n = n, m
    while n != 0:
        m, n = n, m%n
    return a/m, b/m

def isTruncatablePrime(n):
    if not isPrime(n): return False
    s = str(n)
    l = len(s)
    for i in range(1, l):
        if not isPrime(int(s[:i])) or not isPrime(int(s[i:])): return False
    return True
