def perms(l, s):
    if len(l) == 1:
        return [s + str(l[0])]
    ans = []
    for i in l:
        newL = l.copy()
        newL.remove(i)
        ans = ans + perms(newL, s + str(i))
    return ans

l = [1, 2, 3, 4, 5, 6, 7,  8, 9]
sum = 0
prods = []
for perm in perms(l, ''):
    for i in range(1, 8):
        a = int(perm[:i])
        for j in range(i+1, 9):
            b = int(perm[i:j])
            if a > b:
                continue
            c = int(perm[j:])
            if a*b == c and c not in prods:
                prods.append(c)
                sum += c
print(sum)