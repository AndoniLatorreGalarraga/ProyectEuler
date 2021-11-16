names = []
for line in open('Problem22.txt', mode='r'):
    names += line.split(',')

namesFixed = []
for name in names:
    namesFixed.append(name[1:-1])

namesFixed.sort()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum, position = 0, 1
for name in namesFixed:
    s = 0
    for i in range(len(name)):
        s += alphabet.index(name[i]) + 1
    sum += s*position
    position += 1
print(sum)