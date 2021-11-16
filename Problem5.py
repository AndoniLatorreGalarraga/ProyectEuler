def gcd(n, m):
    if m < n:
        m, n = n, m
    while n != 0:
        m, n = n, m%n
    return m

def lcm(n, m):
    return n*m/gcd(n, m)

ans = 1
for i in range(2, 21):
    ans = lcm(ans, i)
print(ans)