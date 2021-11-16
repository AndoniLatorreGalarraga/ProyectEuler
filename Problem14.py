def collatz(n):
    if n%2 == 0:
        return int(n/2)
    return 3*n+1

maxLength = 0
maxN = 1
for n in range(1,1000000):
    nSave = n
    length = 0
    while True:
        if n == 1:
            break
        n = collatz(n)
        length += 1
    if maxLength < length:
        maxLength = length
        maxN = nSave
print(maxN)