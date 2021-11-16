powers = []
for a in range(2, 101):
    for b in range(2, 101):
        i = a**b
        if i in powers:
            continue
        powers.append(i)
print(len(powers))