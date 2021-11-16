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

def isAmicable(a):
    b = d(a)
    return d(b) == a and a != b

sum = 0
for i in range(1, 10000):
    if isAmicable(i):
        sum += i
print(sum)