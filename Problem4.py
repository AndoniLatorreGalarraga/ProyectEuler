max = 0
for n1 in range(100,1000):
    for n2 in range(100,1000):
        n = str(n1*n2)
        if n == n[::-1]:
            if max < int(n):
                max = int(n)
print(max)