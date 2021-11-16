import math

def divisors(n):
    ans = 0
    for i in range(1, round(math.sqrt(n)+1)):
        if n%i == 0:
            if n/i == i:
                ans += 1
            else:
                ans += 2
    return ans

n = 1
while True:
    tri = n*(n+1)/2
    if divisors(tri) >= 500:
        break
    n += 1
print(tri)