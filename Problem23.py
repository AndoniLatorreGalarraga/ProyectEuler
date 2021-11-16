import math

def d(n):
    divisors = [1]
    for div in range(2, round(math.sqrt(n))+1):
        if n%div == 0:
            if n/div == div:
                divisors.append(div)
            else:
                divisors += [div, n/div]
    sum = 0
    for div in divisors:
        sum += div
    return sum

abundants = []

for i in range(1, 28123):
    if i < d(i):
        abundants.append(i)

sums = [0]*28124
for i in abundants:
    for j in abundants:
        s = i+j
        if s <= 28123:
            sums[s] = s

sum = 0
for i in range(1,28124):
    if sums[i] == 0:
        sum += i
print(sum)