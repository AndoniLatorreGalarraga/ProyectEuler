def perms(l, s):
    if len(l) == 1:
        return [s + str(l[0])]
    ans = []
    for i in l:
        newL = l.copy()
        newL.remove(i)
        ans = ans + perms(newL, s + str(i))
    return ans

l = [0, 1, 2, 3, 4, 5, 6, 7,  8, 9]

print(perms(l, '')[999999])