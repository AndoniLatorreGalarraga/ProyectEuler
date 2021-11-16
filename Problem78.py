def f(n, s, a):
    global mem
    if a == n: return 1
    if (n-a, s) in mem: return mem[(n-a, s)]
    ans = 0
    i = s - 1
    while i >= a+s-n and i >= 0:
        ans += f(n, s-i, a+s-i)
        i -= 1
    mem[(n-a, s)] = ans
    return ans
def p(n): return f(n, n,0)
mem = dict()
print(p(10000))