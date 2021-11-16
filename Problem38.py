def perms(l, s):
    if len(l) == 1:
        return [s + str(l[0])]
    ans = []
    for i in l:
        newL = l.copy()
        newL.remove(i)
        ans = ans + perms(newL, s + str(i))
    return ans

class breakException(Exception): pass

try:
    l = perms([9, 8,  7, 6, 5, 4, 3, 2, 1], '')
    for perm in l:
        for i in range (1, 10):
            base = int(perm[:i])
            conc = ''
            for n in range(1, 10):
                conc += str(n*base)
                if conc == perm and n > 1:
                    raise breakException
except breakException:
    pass

print(perm)