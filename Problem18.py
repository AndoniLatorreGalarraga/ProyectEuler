from os import path


def total(i, j):
    if i == len(tri):
        return 0
    return tri[i][j] + max(total(i+1,j), total(i+1,j+1))

tri = []
for line in open('Problem18.txt', mode='r', newline='\n'):
    tri.append([int(i) for i in line.split()])

print(total(0, 0))