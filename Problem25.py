f1 = 1
i = 2
fi = 1
while len(str(fi)) < 1000:
    f1, fi = fi, f1 + fi
    i += 1
print(i)