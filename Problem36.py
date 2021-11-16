sum = 0
for i in range(1, 1000001):
    d, b = str(i), bin(i)[2:]
    if d == d[::-1] and b == b[::-1]: sum += i
print(sum)