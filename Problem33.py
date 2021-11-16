import itertools

def simp(n, m):
    a, b = n, m
    if m < n:
        m, n = n, m
    while n != 0:
        m, n = n, m%n
    return a/m, b/m

digits = [1, 2, 3, 4, 5, 6,  7, 8, 9]
fracs = []
for a, b, c, d in itertools.product(digits, repeat = 4):
    if 10*a + b >= 10*c + d: continue
    e = 10*a + b
    f = 10*c + d
    if a == d:
        ee = b
        ff = c
    elif a == c:
        ee = b
        ff = d
    elif b == d:
        ee = a
        ff = c
    elif b == c:
        ee = a
        ff = d
    else: continue
    if e*ff == ee*f:
        fracs.append((ee, ff))
num, dem = 1, 1
for i, j in fracs:
    num *= i
    dem *= j
print(simp(num, dem)[1])

