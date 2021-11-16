def fact(n):
    if n == 0: return 1
    return n*fact(n-1)

f = dict()
for i in range(10): f[str(i)] = fact(i)

ans, n = 0, 1
while 10**n <= n*f['9']: n += 1

for i in range(10, 10**n):
    s = str(i)
    sum = 0
    for d in s:
        sum += f[d]
    if sum == i: ans += i
print(ans)