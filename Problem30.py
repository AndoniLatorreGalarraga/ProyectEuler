sum = 0
for i in range(2,1000000):
    s = str(i)
    p = 0
    for j in range(len(s)):
        p += int(s[j])**5
    if p == i:
        sum += i
print(sum)