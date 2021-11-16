grid = [[0 for i in range(1001)] for i in range(1001)]
i, j, n = 500, 500, 1
while n<= 1001*1001:
    grid[i][j] = n
    if i <= j and i < 1000 - j:
        j += 1
    elif i == 1000- j and i < j:#
        j += 1
    elif i >= 1000- j and i < j:#
        i += 1
    elif i >= j and i > 1000 -j:
        j -= 1
    elif i <= 1000 - j and i > j:
        i -= 1
    else:
        j += 1
    n += 1

sum = -1
for k in range(1001):
    sum += grid[k][k] + grid[k][1000-k]
print(sum)