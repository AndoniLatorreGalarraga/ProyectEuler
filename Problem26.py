def simp(n, m):
    a, b = n, m
    if m < n:
        m, n = n, m
    while n != 0:
        m, n = n, m%n
    return a/m, b/m

def length(a, n):
    a, n = simp(a, n)
    aList.append(a)
    aa = a*10%n
    if aa == 0:
        return 0
    if aa in aList:
        return len(aList) - aList.index(aa)
    return length(aa, n)

maxLength = 0
for d in range(2, 1000):
    aList = []
    l = length(1, d)
    if l > maxLength:
        maxD, maxLength = d, l
print(maxD)
